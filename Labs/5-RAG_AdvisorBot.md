# Retrieval Augmented Generation: AdvisorBot

## Overview

This lab will let you practice working with **retrieval augmented generation** (RAG), one of the primary techniques for building customized applications on top of generative AI models. There are, literally, thousands of startups using the basic techniques we're going to cover in this lab and in the next project to build their applications.

The code below is closely adapted from Anthropic's [RAG example using Claude](https://github.com/anthropics/anthropic-cookbook/blob/main/third_party/Pinecone/rag_using_pinecone.ipynb). I've converted their code into a Python scripts, added some more explanatory comments, and streamlined a few things. Check out the rest of the documentation.


## Strategy

The overall goal of RAG is to help a generative model produce better answers by *adding additional relevant information* into the prompt.

For a simple example, imagine using Microsoft's Copilot with your Outlook e-mail. You could ask it questions like, "What did Valerie e-mail me about last Tuesday?", and the system will search your inbox for relevant messages and combine them into a prompt like the following:

```
<CONTENTS OF E-MAIL 1>

<CONTENTS OF E-MAIL 2>

<CONTENTS OF E-MAIL 3>

Using these e-mail messages, answer the question: What did Valerie e-mail me about last Tuesday?
```

The LLM can then use its reasoning powers on the specific information given in the prompt and return an answer to your question.

### Talk to your data

There are *many* startups producing similar "talk to your data" applications that combine an LLM with access to a company's proprietary databases, such as code repositories, documents, sales data, or customer relationship management (CRM) systems. These applications work something like the following:

1. The user submits a query that they want the LLM to answer
2. The RAG system searches the databases for relevant information, then extracts and formats it
3. The system constructs a prompt that combines the user's original question with the additional information from the DB search
4. This is sent to the LLM, which can draw upon the context-specific information in the prompt to guide the answer

Other applications of RAG include providing up-to-date information after the model's training cutoff.

### Aside: RAG vs. huge contexts vs. fine tuning

RAG is not the only approach to building customized LLM apps.

The current leading models, like Google's Gemini, can work with *extremely large context windows* of 1 million tokens, which is enough to process tens of thousands of pages of text in one query. Therefore, in theory, you could just dump your entire database into the context window for every query: Don't worry about picking the "most relevant" information, just give the LLM everything!

Recall that transformer complexity scales quadratically with the size of the context window. Therefore, using huge windows isn't practical for general applications, because the cost and time per query is too high. 

The other option is to *fine tune* your model, by tweaking its weights directly. This is usually done to guide the model towards a specific part of the output space. The most important fine-tuning technique is called **Low-Rank Augmentation** (LoRA), which is used to customize image generators like Stable Diffusion toward particular styles or subjects. For other applications, the general consensus is that fine-tuning is harder that RAG, but doesn't yield better results.


## Architecture

<img src="https://gradientflow.com/wp-content/uploads/2023/10/newsletter87-RAG-simple.png" width="500px" />

*From "Best Practices in Retrival Augmented Generation", [Gradient Flow Substack](https://gradientflow.substack.com/p/best-practices-in-retrieval-augmented)*


The RAG application is built around a vector database like Pinecone that we used in the last lab. The database is populated with embedded "chunks" taken from the raw input documents.

As we'll discuss below, the chunking strategy turns out to be key for the quality of the results.

## Example: AdvisorBot

**AdvisorBot** is an example RAG application that uses information from the Rollins course catalog to answer your advising questions. We're going to write two scripes:

- One to fetch a page of the catalog from the web, chunk it, and insert it into a Pinecone DB

- Another to prompt the user for a query, extract relevant chunks from the DB, and call the Claude API to get an answer

Like the last lab, this is inspired by the examples in the [Anthropic cookbook](https://github.com/anthropics/anthropic-cookbook).

### Claude API

Sign up for an Anthropic account if you haven't done so, then go to the [API console](https://console.anthropic.com/dashboard).

Once you're there, you can get an API key and insert it into the Secrets menu of your Repl.it workspace, following the same instructions we used last time. Claude offers $5 of free API credits to first-time users, which is enough for hundreds of queries, but they expire after two weeks.

Install the `anthropic` module with

```
pip install anthropic
```

in the shell.

### Populate the database

Put the script below in a file named `advisorbot_setup.py`.

```
"""
Setup the AdvisorBot database using a page from the Rollins catalog
"""

#--- Imports
import pandas as pd
from pinecone import Pinecone
from pinecone import ServerlessSpec
import time
import voyageai
from tqdm.auto import tqdm
from time import sleep
import anthropic
import json
import os
import requests
from bs4 import BeautifulSoup

#--- API keys
ANTHROPIC_API_KEY = os.environ['ANTHROPIC_API_KEY']
PINECONE_API_KEY = os.environ['PINECONE_API_KEY']
VOYAGE_API_KEY = os.environ['VOYAGE_API_KEY']


#--- Retrieve HTML file

url = "https://catalog.rollins.edu/content.php?catoid=22&navoid=869"
response = requests.get(url)
page_content = response.text

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(page_content, "html.parser")

# Extract the text from the HTML
text = soup.get_text()

# Clean up the text by removing extra whitespace
text = " ".join(text.split())

# Divide the text into chunks
chunk_size = 100  # Adjust the chunk size as needed
chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]


#--- Setup Pinecone vector database
pc = Pinecone(api_key=PINECONE_API_KEY)
spec = ServerlessSpec(
    cloud="aws", region="us-east-1"
)


#--- Create a new vector database
index_name = 'catalog'
existing_indexes = [
    index_info["name"] for index_info in pc.list_indexes()
]

# check if index already exists (it shouldn't if this is first time)
if index_name not in existing_indexes:
    # if does not exist, create index
    pc.create_index(
        index_name,
        dimension=1024,  # dimensionality of voyage-2 embeddings
        metric='dotproduct',
        spec=spec
    )
    # wait for index to be initialized
    while not pc.describe_index(index_name).status['ready']:
        time.sleep(1)

# connect to index
index = pc.Index(index_name)
time.sleep(1)

# view index stats
print(index.describe_index_stats())


#--- Setup VoyageAI: It's used to create embeddings
vo = voyageai.Client(api_key=VOYAGE_API_KEY)


#--- Embed and insert each chunk
for i, chunk in enumerate(chunks):

  # Embed the chunk
  done = False
  while not done:
      try:
          res = vo.embed(chunk, model="voyage-2", input_type="document")
          done = True
      except:
          sleep(5)

  embed = [record for record in res.embeddings]

  # create unique IDs for each text
  id = [f"chunk_{i}" ]

  # Create metadata dictionary for this chunk
  metadata = [{'content': chunk}]

  to_upsert = list(zip(id, embed, metadata))

  # upsert to Pinecone
  index.upsert(vectors=to_upsert)


# After completing the upload, the DB should contain vectors
print(index.describe_index_stats())
```


Take a look at the code, which is similar to what we used in the last lab. The first half fetches [a page of the catalog](https://catalog.rollins.edu/content.php?catoid=22&navoid=869), then extracts the page content using the Beautiful Soup HTML parser. The following lines are key:

```
# Divide the text into chunks
chunk_size = 100  # Adjust the chunk size as needed
chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
```

This fragment divides the text into chunks of 1024 characters. The size of the chunks is a key parameter:

- Bigger chunks provide more context, but are less focused on one topic
- Smaller chunks are more focused, but it may be harder to find good approximate matches in the database, since it may not be clear what a chunk is "about" 

The second half sets up a Pincone database named `catalog` and populates it with the embedded chunks. Review the last lab for more background on how this works.


### Queries

Big script below that prompts the user for a query, then makes API calls. Put it in a file named `advisor_query.py`.

Before digging into the code, run it a few times and try asking some questions, like, "How do I appeal a grade?". Try to find some questions the bot answers well and some questions that it answers poorly and think about why that might be. Remember that the bot only has access to the one page that we gave it, so it doesn't know eveything about the catalog.

Now look at the code and see if you can follow the flow that a query goes through. What functions are called and in what order?

```
"""
Query the catalog database
"""

#--- Imports
import pandas as pd
from pinecone import Pinecone
from pinecone import ServerlessSpec
import time
import voyageai
from tqdm.auto import tqdm
from time import sleep
import anthropic
import json
import os

#--- API keys
ANTHROPIC_API_KEY = os.environ['ANTHROPIC_API_KEY']
PINECONE_API_KEY = os.environ['PINECONE_API_KEY']
VOYAGE_API_KEY = os.environ['VOYAGE_API_KEY']

def get_completion(prompt):
  """
  Send a promot to Claude and return its response
  """
  
  completion = client.completions.create(
    model="claude-2.1",
    prompt=prompt,
    max_tokens_to_sample=1024,
  )
  
  return completion.completion


def create_keyword_prompt(question):
  """
  Construct a prompt string requesting keywords related to
  the user's question
  """
  
  return f"""\n\nHuman: You help students with academic advising questions. Given a question, generate a list of 5 relevant topics that can be used to search for relevant information in the college's academic catalog.

The question is: {question}

Output your keywords as a JSON that has one property "keywords" that is a list of strings. Only output valid JSON.\n\nAssistant:{{"""


def get_related_entries(question):
  """
  Given a question, get a list of related keywords, then query the DB for
  entries most related to each keyword

  returns: a list of DB chunks related to the given question
  """
  
  keyword_json = "{" + get_completion(create_keyword_prompt(question))
  data = json.loads(keyword_json)
  keywords_list = data['keywords']

  results_list = []
  for keyword in keywords_list:
    # Embed the keyword
    query_embed = vo.embed([keyword], model="voyage-2", input_type="query")
  
    # Find related entries in the DB
    search_results = index.query(vector=query_embed.embeddings, top_k=3, 
                                 include_metadata=True)
    
    # Append related entries to the list of all results
    for search_result in search_results.matches:
      results_list.append(search_result['metadata']['content'])

  return results_list


def format_results(extracted: list[str]) -> str:
  """
  Converts the list of text chunks returned by the keyword search into
  a structured format
  
  The result is a string that looks like this:
    <search_results>
    <item>CONTENTS OF CHUNK 1</item>
    <item>CONTENTS OF CHUNK 2</item>
    <item>CONTENTS OF CHUNK 3</item>
    etc.
    </search_results>
  """
  
  result = "\n".join(
    [
      f'<item index="{i+1}">\n<page_content>\n{r}\n</page_content>\n</item>'
      for i, r in enumerate(extracted)
    ]
  )

  return f"\n<search_results>\n{result}\n</search_results>"

def create_answer_prompt(results_list, question):
  """
  Construct the main RAG prompt that combines results from the DB lookup with
  the user's question
  """
  
  return f"""\n\nHuman: {format_results(results_list)} Using the search results provided within the <search_results></search_results> tags, please answer the following question <question>{question}</question>. \n\nAssistant:"""


if __name__ == '__main__':
  
  # Setup Pinecone vector database
  pc = Pinecone(api_key=PINECONE_API_KEY)
  spec = ServerlessSpec(
      cloud="aws", region="us-east-1"
  )

  # Connect to the database
  index_name = 'catalog'
  index = pc.Index(index_name)
  time.sleep(1)

  # Setup VoyageAI
  vo = voyageai.Client(api_key=VOYAGE_API_KEY)

  # Connect to Claude client
  client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

  # Prompt the user for a query
  print("Hello. I'm AdvisorBot. I'll help answer your questions about Rollins.\n")
  print('What question do you have?\n')
  USER_QUESTION = input('Type your question and press ENTER.\n')

  results_list = get_related_entries(USER_QUESTION)
  
  # Ask Claude to answer the question and print its response
  answer = get_completion(create_answer_prompt(results_list, USER_QUESTION))
  print()
  print(answer)
```

### Query execution

There are two basic steps to query processing:

- Call `get_related_entries`, which takes the query and looks up the most likely related entries in the Pinecone DB
```
results_list = get_related_entries(USER_QUESTION) 
```

- Prompt Claude to synthesize those results with the query and return an answer
```
answer = get_completion(create_answer_prompt(results_list, USER_QUESTION))
```

`get_related_entries` actually contains a second API call, to prompt Claude to convert the user question into a set of relevant search terms, via the `create_keyword_prompt` method. Those search terms are then embedded and then used to search the database for relevant text chunks.

Take a look at the functions that create prompts. Observe that the prompts are just text strings, with the user's query and results information inserted at specific places. This is one of the advantages of wrapping an application around an LLM: tweaking the prompts is easy.


## Jam

Once you have the AdvisorBot working and you've explored the code, try making the following changes.

### Chunk size

Experiment with changing the chunk size in `advisorbot_populate.py`. For each experiment, delete your `catalog` database on the Pinecone dashboard, then rebuild it using `advisorbot_populate.py`.

Try small (100), very small (say, 24), and larger chunks, up to maybe 4096 characters. Ask the same queries for ech What changes do you notice in the quality of the output as you vary the chunk size?


### Prompts

Experiment with editing the query prompts. You can try modifying the output style formatting, or ask the bot to provide a specific perspective. You can ask it to be more concise, or respond to the user in specific ways.

