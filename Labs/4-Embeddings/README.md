# Lab: Embeddings

## Overview

This lab demonstrates working with text embeddings and vector databases using VoyageAI and Pinecone. It's based on [these examples](https://github.com/anthropics/anthropic-cookbook/blob/main/third_party/Pinecone/rag_using_pinecone.ipynb) developed by Anthropic to illustrate applications of the Claude AI.

## Create accounts

Sign up for an account at [Pinecone](https://docs.pinecone.io/guides/getting-started/quickstart) and [VoyageAI](https://www.voyageai.com/). Once you have accounts you can go to the dashboard for each tool and create an API key.

Copy your API keys into a local text file on your computer. Then stop and wait for me to show you how to do the next part.


## Setup secret API keys

I'll show you how to do this part. Once you have your keys setup in Repl.it, you can access them in your program using:

```
#--- API keys
import os

PINECONE_API_KEY = os.environ['PINECONE_API_KEY']
VOYAGE_API_KEY = os.environ['VOYAGE_API_KEY']
```


## Install libraries

Run this command in the shell to install the necessary libraries.

```
 pip install pinecone-client voyageai
```


## First example: embed a text string

The code below sets up the connection to VoyageAI using the API key that you configured in the previous step. It then calls `vo.embed` to convert a given text string to a vector. The output is a long list of, in this case, 1024 numbers.

Key idea: This embedding, in some sense, captures the holistic essence of the text string. It's a quantitative representation of what the string is "about" in an abstract way. But, beacuse it's now a vector, we can more easily calculate things like distances, similarities, and translations in vector space.

Once you can run the code below, experiment with creating a few more example embeddings.

```
"""
Example of embedding a text string using VoyageAI
"""


#--- Imports
from pinecone import Pinecone
from pinecone import ServerlessSpec
import time
import voyageai
from time import sleep
import os
import requests
from tqdm.auto import tqdm


#--- API keys
PINECONE_API_KEY = os.environ['PINECONE_API_KEY']
VOYAGE_API_KEY = os.environ['VOYAGE_API_KEY']


#--- Initialize Voyage
vo = voyageai.Client(api_key=VOYAGE_API_KEY)


#--- Calculate some example embeddings
texts = ["Happy Fox Day"]

result = vo.embed(texts, model="voyage-2", input_type="document")
print(result.embeddings[0])
```

## Pinecone

Pinecone is a **vector database**. It's optimized to store numerical vectors and perform quick retrievals and comparisons between vectors.

We're going to use Pinecone to store a collection of word embeddings, then demonstrate that it can take a word or phrase and find related concepts.


Add the lines below to initialize Pinecone.

```
#--- Setup Pinecone vector database
pc = Pinecone(api_key=PINECONE_API_KEY)
spec = ServerlessSpec(
    cloud="aws", region="us-east-1"
)


#--- Create a new vector database
index_name = 'words'
existing_indexes = [
    index_info["name"] for index_info in pc.list_indexes()
]

# Check if index already exists (it shouldn't if this is first time)
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
```

Run your program again, then check your Pinecode dashboard. You should see that there is now a database named `words` that's currently empty.


## Embed some words

I could not allow you to graduate without doing one more lab using the word list. The code below pulls `words.txt` as a text file from this repo, then splits it into individual words. For each word, it calls Voyage to calculate an embedding, then inserts the embedding vector along with its associated word into the Pinecone DB we created in the previous step.

```

#--- Get the words.txt file
url = "https://raw.githubusercontent.com/dansmyers/AI/main/Labs/4-Embeddings/words.txt"
response = requests.get(url)
words_string = response.text
words = words_string.split('\n')


#--- Populate the vector database with the list of words
batch_size = 100

for i in tqdm(range(0, len(words), batch_size)):
  # find end of batch
  i_end = min(len(words), i+batch_size)
  words_batch = words[i:i_end]
  print(words_batch)
  
  # create embeddings (try-except added to avoid RateLimitError. Voyage currently allows 300/requests per minute.)
  done = False
  while not done:
      try:
          res = vo.embed(words_batch, model="voyage-2", input_type="document")
          done = True
      except:
          sleep(5)

  embeds = [record for record in res.embeddings]
  # create unique IDs for each text
  ids_batch = [f"word_{idx}" for idx in range(i, i_end)]

  # Create metadata dictionaries for each text
  metadata_batch = [{'word': word} for word in words_batch]

  to_upsert = list(zip(ids_batch, embeds, metadata_batch))

  # upsert to Pinecone
  index.upsert(vectors=to_upsert)


# After completing the upload, the DB should contain vectors
print(index.describe_index_stats())

```


Run the script. It will take a while to load all the vectors.


## Query

Create a new file called `query.py`. The following code queries the example database for words similar to the query. You can run it in another shell window while the previous step is still executing and it will find matches on the set of strings that have already been inserted into the DB.

```
"""
Querying the vector database
"""

#--- Imports
from pinecone import Pinecone
from pinecone import ServerlessSpec
import time
import voyageai
from time import sleep
import os
import requests
from tqdm.auto import tqdm


#--- API keys
PINECONE_API_KEY = os.environ['PINECONE_API_KEY']
VOYAGE_API_KEY = os.environ['VOYAGE_API_KEY']


#--- Initialize Voyage
vo = voyageai.Client(api_key=VOYAGE_API_KEY)


#--- Setup Pinecone vector database
pc = Pinecone(api_key=PINECONE_API_KEY)
spec = ServerlessSpec(
    cloud="aws", region="us-east-1"
)

# connect to index
index_name = 'words'
index = pc.Index(index_name)
time.sleep(1)


#--- Query code
query = "Happy Fox Day"

# Embed the query string
question_embed = vo.embed([query], model="voyage-2", input_type="document")

# Retrieve the top-k similar vectors from the DB
results = index.query(
            vector=question_embed.embeddings, top_k=10, include_metadata=True
          )

# Print
print(results)
```

## Translations in embedding space

Here's a key idea: Embeddings capture not just a *position* for an item in vector space, but also *relationships* between concepts. Therefore, taking the difference between two embeddings corresponds to the "direction" that moves from one concept to another.

The classic example is the embedding difference

```
"woman" - "man"
```

which gives a vector that represents "femaleness" that represents moving in a "feminine" direction within the abstract concept space. Therefore, we should be able to use this translation to change a masculine-coded word to its feminine counterpart. So, for example, in embedding space

```
"boy" + ("woman" - "man")
```

should be close the the emebdding for "girl" and

```
"king" + ("woman" - "man")
```

should be close to "king".

The code below illustrates this concept.

```#--- Using differences in embedding space for conceptual transformations
texts = ["man", "woman", "boy"]

# Embed three words
result = vo.embed(texts, model="voyage-2", input_type="document")
man_embed = result.embeddings[0]
woman_embed = result.embeddings[1]
king_embed = result.embeddings[2]

# Compute element-wise difference between "woman" and "man"
diff_vector = [woman_embed[i] - man_embed[i] for i in range(len(man_embed))]

# Add the difference vector to list3
query_embed = [king_embed[i] + diff_vector[i] for i in range(len(king_embed))]

results = index.query(
            vector=query_embed, top_k=10, include_metadata=True
          )
```

Add it to the end of `query.py` and run it to produce output like the following: "girl" is the top match.

```
{'matches': [{'id': 'word_41056',
              'metadata': {'word': 'girl'},
              'score': 1.00318074,
              'values': []},
             {'id': 'word_11570',
              'metadata': {'word': 'boy'},
              'score': 0.997219622,
              'values': []},
             {'id': 'word_112303',
              'metadata': {'word': 'woman'},
              'score': 0.991101801,
              'values': []},
             {'id': 'word_35568',
              'metadata': {'word': 'female'},
              'score': 0.989245355,
              'values': []},
             {'id': 'word_41062',
              'metadata': {'word': 'girls'},
              'score': 0.972338676,
              'values': []},
             {'id': 'word_35595',
              'metadata': {'word': 'femme'},
              'score': 0.971944571,
              'values': []},
             {'id': 'word_88047',
              'metadata': {'word': 'schoolgirl'},
              'score': 0.96950084,
              'values': []},
             {'id': 'word_35569',
              'metadata': {'word': 'females'},
              'score': 0.969277918,
              'values': []},
             {'id': 'word_54188',
              'metadata': {'word': 'lady'},
              'score': 0.96848762,
              'values': []},
             {'id': 'word_10382',
              'metadata': {'word': 'blonde'},
              'score': 0.967908502,
              'values': []}],
 'namespace': '',
 'usage': {'read_units': 6}}
```

Try experimenting with some other starting words like "king", then try coming up with some other concept pairs and see what results you can construct.
