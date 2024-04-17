# Retrieval Augmented Generation: Part I

## Overview

This lab will let you practice working with **retrieval augmented generation** (RAG), one of the primary techniques for building customized applications on top of generative AI models. There are, literally, thousands of startups using the basic techniques we're going to cover in this lab and in the next project to build their applications.

The code below is closely adapted from Anthropic's [RAG example using Claude](https://github.com/anthropics/anthropic-cookbook/blob/main/third_party/Pinecone/rag_using_pinecone.ipynb). I've converted their code into a single Python script, added some more explanatory comments, and streamlined a few things. Check out the rest of the documentation.


## Strategy

The overall goal of RAG is to help a generative model produce better answers by *adding additional relevant information* into the prompt.

For a simple example, imagine using Microsoft's Copilot with your Outlook e-mail. You could ask it questions like, "What did Valerie e-mail me about last Tuesday?", and the system will search your inbox for relevant messages and combine them into a prompt like the following:

```
<CONTENTS OF E-MAIL 1>

<CONTENTS OF E-MAIL 2>

<CONTENTS OF E-MAIL 3>

Using these e-mail messages, answer the question: What did Valerie e-mail me about last Tuesday?
```

The LLM can then use its reasoning powers on the specific information given in the prompt.

There are *many* startups producing similar "talk to your data" applications that combine an LLM with access to a company's proprietary databases, such as code repositories, documents, sales data, or customer relationship management (CRM) systems. These applications work something like the following:

1. The user submits a query that they want the LLM to answer

2. The RAG system searches the databases for relevant information, then extracts and formats it

3. The system constructs a prompt that combines the user's original question with the additional information from the DB search

4. This is sent to the LLM, which can draw upon the context-specific information in the prompt to guide the answer

Other applications of RAG include providing up-to-date information after the model's training cutoff.


## Architecture

