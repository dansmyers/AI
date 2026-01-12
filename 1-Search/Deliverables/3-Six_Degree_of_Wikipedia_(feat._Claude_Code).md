# Six Degrees of Wikipedia (feat. Claude Code)

<img src="https://substackcdn.com/image/fetch/$s_!PAxG!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa137509b-3774-4b96-8727-66f4cf7ae376_1920x1080.png" width="600px" />

*Retro-futurism is when you run the world's most powerful AI in the plain text terminal. Via [The Discourse](https://thediscourse.co/p/claude-code).

## Overview

It's a bit old-fashioned at this point, but you might have heard of the [Six Degrees of Kevin Bacon](https://en.wikipedia.org/wiki/Six_Degrees_of_Kevin_Bacon): the idea that any actor can be linked to Kevin Bacon through shared film roles. The general concept is the **six degrees of separation**, which theorizes that almost everyone on Earth is separated by at most six personal connections. Similar ideas exist in other fields:

- The [Erdős number](https://en.wikipedia.org/wiki/Erd%C5%91s_number) measures the distance of a researcher from the prolific 20th Century Hungarian mathematician Paul Erdős, who was known for having a huge number of collaborators. Erdős himself has a number of 0. Anyone who co-authored a paper with Erdős has a number of 1, their co-authors have number of 2, and so forth. Mine is 5.

- The Sabbath number connects musicians to the members of Black Sabbath, which had a huge number of lineup changes during the 70s and 80s. Members of Black Sabbath have a number of 0. Anyone who collaborated with a member on a recording or performance has a number of 1, and so forth.

- For the true Rennaisance man or woman, there's the [Erdős-Bacon-Sabbath number](https://news.asu.edu/20160126-creativity-lawrence-krauss-erdos-bacon-sabbath-score), which adds the three scores. Physicist Stephen Hawking and futurist Ray Kurzweil both have an 8 (Hawking appeared as a guest voice overdub on a Pink Floyd album and Kurzweil appeared at a concert with Tori Amos). Brian May, guitarist of Queen, has a 9.

A more recent version of the game is the Six Degrees of Wikipedia: connect one article to another by following a chain of links. This leads directly to the [Wikipedia speedrun](https://wikispeedruns.com/) where the goal is to connect articles as fast as possible.

In this project you're going to write a web app that can solve Wikipedia connections. This will let us practice using state-based search on a bigger application. Along the way, you'll also get to try:

- Making a basic web application with a front-end, back-end, and API
- Making API calls to retrieve Wikipedia pages
- Using *bidirectional iterative deepening* to make the search more efficient
- Caching search results

## Claude Code

The other major part of this project is using **Claude Code**, an AI programming tool made by Anthropic. Claude Code is an *agentic AI*, meaning that it runs in a loop, can use tools, make plans, and evaluate its own progress. As we'll see, it has the ability to take a general spec for a program and convert it to code in a frankly mind-blowing way.

The instructions below will show you how to set up Claude Code and work through a basic project. You'll then get to work on adding some more features on your own.

## Details

- Create a web application that can complete Wikipedia article chains.

- The front end is simple: two input boxes for the titles of the start and end articles. Use HTML, CSS, vanilla JavaScript. Complex frameworks are unnecessary.

- The backend shoud be written in Python Flask. It will define an API to receive inputs from the front end and return the results of searches. Working out the design of this API is part of the project.

- Use the Wikimedia API to retrieve the content of Wikipedia pages. When you retrieve a page, parse its content to extract its links, which become part of the frontier set of the search. Fetching pages dynamically using the API is slower than using a pre-computed database of page links, but the database of page-to-page links for Wikipedia is too large for us to feasibly use for this project.

- Use the *bidirectional iterative deepening* search algorithm. The method runs two iterative deepening searches, one starting at the source and the other at the end, looking for a node where they meet in the middle. Bidirectional search can be significantly faster than a single-direction search but you have to be able to work backwards from the goal in order to implement it.

- Don't implement any caching of results for the first version.

- Using a single thread to manage the search is fine; you don't need multiple threads running in parallel.

- Make whatever other reasonable choices seem necessary in order to implement the project.

## Claude Code setup

1. Create a new GitHub Codespace

2. Run the following command in your terminal to install the Claude Code application in your workspace
```
curl -fsSL https://claude.ai/install.sh | bash
```

3. Type `claude` in the terminal to start the program

4. You will have to authenticate your account. To do this in Codespaces, I had to follow the link that Claude prints in the terminal, which will prompt you to log in to your Anthropic account. Once you've done that, you should get a key that you can paste back into your terminal.

5. Answer the other setup questions. The defaults should be fine.

At the end, you should see a prompt in your terminal waiting for you to input a command for the agent.

Note: you have three other options for running Claude Code:

- By downloading Claude Desktop and running on your local computer. Depending on the permissions you set, this would allow Claude Code to interact with your personal files. I don't recommend this right now - it's safer to run in a sandboxed environment - but there are many people experimenting with productivity apps built by running agents on their local computers.

- You could also do the terminal install within the Terminal app of your personal computer. This has the same tradeoffs as using the desktop version with a little more power due to running in the terminal.

- By using the web interface. This is sandboxed, but it doesn't have the full features of the terminal version right now.

I'm using the terminal version in this class because it has some useful features that we'll be able to explore in future projects. 


## Process

### Chat about the design

A good strategy is to start by chatting about the project. The goal of this step is to clarify your design and produce a spec document that you'll then use to drive the development process within Claude Code.

I prefer to do this in the regular chat window. Open up a new Claude chat and prompt it to discuss the project with you. Here's an example:
> I want to create a web application that completes Wikipedia chains. It should have the following features:
> 
> *LIST OF FEATURES FROM ABOVE GOES HERE*
>
> Discuss this project with me and help me clarify the design and produce a spec that I can give to my automated coding agent. You don't need to write any code yet, just discuss the project so that we can create a spec.

This should kick off a few rounds of discussion as you work through some design details.

At the end of the discussion, ask Claude to output the spec in Markdown format so you can copy it to your agent.

### `claude.md`

In Claude Code, `claude.md` is the project overview file. It's *automatically loaded* with every request, so it's the place for putting essential information about the project goal, code structure, desired behaviors, style, etc. that you want Claude to have as context.

Create `claude.md` in your Codespace:
```
touch claude.md
```
Copy the project spec from your chat into the file.

### Make a plan



### Develop incrementally

### End-to-end testing


## Extension: Adding a database that caches links





