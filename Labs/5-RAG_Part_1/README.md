# Retrieval Augmented Generation: Part I

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

