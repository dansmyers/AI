# Lab: Embeddings


## Create accounts


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
