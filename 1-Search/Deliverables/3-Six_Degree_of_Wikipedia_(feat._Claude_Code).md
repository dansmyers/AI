# Six Degrees of Wikipedia (feat. Claude Code)

<img src="https://substackcdn.com/image/fetch/$s_!PAxG!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa137509b-3774-4b96-8727-66f4cf7ae376_1920x1080.png" width="600px" />

*Retro-futurism is when the AI runs in the terminal. Via [The Discourse](https://thediscourse.co/p/claude-code).*

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

Claude Code is not the only powerful AI agent. OpenAI's has one called [Codex](https://chatgpt.com/codex) (using GPT-5.2) and Google has [Antigravity](https://antigravity.google/) (powered by Gemini 3). All three tools are broadly similar, although one agent may be better than another for some kinds of problems.

**For this class, we're going to use Claude Code**.


## Details

- Create a web application that can complete Wikipedia article chains.

- The front end is simple: two input boxes for the titles of the start and end articles. Use HTML, CSS, vanilla JavaScript. Complex frameworks are unnecessary.

- The backend shoud be written in Python Flask. It will define an API to receive inputs from the front end and return the results of searches. Working out the design of this API is part of the project.

- Use the Wikimedia API to retrieve the outgoing links on a particular page. You only need to use article links in the main Wikipedia space; don't follow links to admin pages, discussions, images, etc. Fetching pages dynamically using the API is slower than using a pre-computed database of page links, but the database of page-to-page links for Wikipedia is too large for us to feasibly use for this project.

- Use the *bidirectional iterative deepening* search algorithm. The method runs two iterative deepening searches, one starting at the source and the other at the end, looking for a node where they meet in the middle. Bidirectional search can be significantly faster than a single-direction search but requires working backwards from the goal, which isn't possible for some problems.

- To run the backwards search, you need to find the *incoming* links for a page - the pages that link to it. The Wikimedia API has a feature that returns the backlinks for a given page.

- Cut off the search and return failure if it doesn't complete within a chain of seven articles, corresponding to a max search depth of four.

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

- By downloading [Claude Desktop](https://code.claude.com/docs/en/desktop) and running on your local computer. Depending on the permissions you set, this would allow Claude Code to interact with your personal files. I don't recommend this right now - it's safer to run in a sandboxed environment - but there are many people experimenting with productivity apps built by running agents on their local computers.

- You could also do the terminal install within the Terminal app of your personal computer. This has the same tradeoffs as using the desktop version with a little more power via the command line interface.

- By using the [web interface](https://code.claude.com/docs/en/claude-code-on-the-web). This is sandboxed, but it doesn't have the full features of the terminal version right now.

I'm using the terminal version in this class because it has some useful features that we'll be able to explore in future projects. 


## Process

<img src="https://www.staugustine.com/gcdn/authoring/2016/04/20/NSAR/ghows-LK-dcc0634b-f43a-4659-b025-d059371857a0-d477868b.jpeg" width="400px" />

*Gomek the crocodile being fed a whole nutria at the St. Augustine Alligator Farm. He was one of the largest saltwater crocodiles ever kept in captivity, measuring almost 18 feet long and nearly 2000 pounds. Gomek was surprisingly docile: he was "tame" enough to allow his handlers to enter his habitat and feed him from only 1 meter away. He died of heart disease in 1997 at an estimated age of 70. His preserved body is on permanent display at the Alligator Farm.*

You probably could throw a short prompt into Claude Code and have it build this project in one shot - which is ***completely insane*** - but it will be better in the long run if you cultivate a *structured development process*.

Coding with AI agents is very much an evolving art, but here are a few principles: 

- Claude Code is not your friend. Do not anthropomorphize it. It is like Gomek the crocodile: incredibly strong, surprisingly docile, but fundamentally wild. It will fix your trickiest bug, but also might decide to delete your production database.

- Therefore, **downside protection** is a key part of AI programming. You need to avoid situations where one bad generation can ruin your code. Use version control: start each session with a fresh branch and use frequent commits.

- The Dark Power of AI models is generating huge amounts of code quickly. This Power will tempt you, *but you must resist it*. Keep control of your generations so that you're never too far from a well-understood working version.

- The keys to AI-powered development are the same as regular pre-AI development: Have a clear design, document your choices, keep components encapsulated, think about interfaces, etc. We've talked about all of these things in previous classes.

- Automated testing is essential. Adopt the Cold War strategy of [*Trust, but verify*](https://en.wikipedia.org/wiki/Trust,_but_verify) in your interactions.

- Human review and merging, rather than code generation, becomes the bottleneck.

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

### Specs document

Make a new file called `specs.md`. Copy the complete project spec from your chat into the file. This is the record of the top-level design.

### `claude.md`

In Claude Code, `claude.md` is the project overview file. It's *automatically loaded* with every request, so it's the place for putting essential information about the project goal, code structure, desired behaviors, style, etc. that you want Claude to have as context.

Create `claude.md` in your Codespace:
```
touch claude.md
```

Guides recommend keeping `claude.md` relatively short. Edit it when you identify problems with Claude's understanding of the project/guidelines/style. Here's an example that I asked Claude to generate from the spec:
```
# Wikipedia Chain Finder

## Project Summary
A web app that finds the shortest path of links between two Wikipedia articles using bidirectional search. Flask backend with vanilla JS frontend.

## Core Requirements
- User enters start/end article titles, app finds the shortest link path connecting them
- Maximum search depth: 7 links
- Uses Wikipedia MediaWiki API (no local database)
- Only mainspace articles (namespace 0)—no File:, Wikipedia:, Help:, etc.
- Bidirectional iterative deepening search algorithm

## Architecture
- **Backend**: Python/Flask with background threading for search jobs
- **Frontend**: Vanilla HTML/CSS/JS (no frameworks)
- **Communication**: Polling pattern—POST creates job, GET polls for status every 1-2 seconds

## API Endpoints
- `POST /api/search` — Start search, returns `job_id`
- `GET /api/search/<job_id>` — Poll status, returns progress or results

## Coding Standards
- Keep dependencies minimal (Flask, requests only)
- No classes where simple functions suffice
- Type hints on all function signatures
- Docstrings on public functions
- Handle Wikipedia API pagination (continuation tokens)
- Include reasonable error handling for API failures
- Set a polite User-Agent header for Wikipedia requests
```


### Make a plan

The spec is a description of what you want to build. The next step is to turn that into a plan, with phases and steps that Claude can execute.

In the terminal, prompt Claude Code to read the project description in `specs.md` and generate a step-by-step plan to build it. Output the plan to a file called `plan.md` so you can review it. The plan should break the implementation up into distinct phases that correspond to implementing major features. Make sure that each phase includes testing steps that the project must pass before going on to the next phase.

Read the plan and make sure it looks reasonable before proceeding.


### Develop incrementally

As we said above, you must resist the temptation to one-shot everything. Instead, you want to **build one phase at a time**. Each generation should never be too far from a well-understood version that you can roll back to if necessary.

Start prompting Claude to build the project using the phases in `plan.md`. Make sure to test each phase before moving on to the next.

As you're working, Claude will prompt you to grant permissions for tools like `python3` and `curl`. Go ahead and approve these for the current project. There is an option to `--dangerously-skip-permissions` (aliased to `--yolo`) that lets Claude have full access to the current environment with no checks, but you want to keep control over what it's doing on each step.

If you run into problems, it's often easier to just regenerate the misbehaving component with clearer instructions, rather than trying to fix what you have.

### User testing

You still have to verify that the app works! Run it, and experiment with some article chains. It will be slow, but that's okay for the first version. Fix any problems that come up and make any changes that you want.

## Extension: Adding a database that caches links

Most articles have dozens to hundreds of links. If each link requires a separate API call, then you can easily end up making tens of thousands of requests for even a small search.

Let's improve performance by *caching* page links in a permanent backend database. Every time you read a new page, extract its links and store them in the DB. Then, if you need that page again, you can read its links from the local DB rather than making API requests. In more detail:

- When you need a page, first check if it's in the DB
- If so, query its linked pages from the DB and put them in the frontier
- If not, fetch the page's links using the API, then add them as new entries in the DB so they're now cached for future requests

Note that you're only caching the *links* on a page for the purposes of the search, not the complete page content. Don't worry about checking for page updates or timeliness.

You'll also want a way to apply this to the bidirectional search, so that you can retrieve the backlinks for a page you've seen before. Chat about how to incorporate that into your design. You should be able to do this without creating a separate database of backlinks.

Use Claude Code to modify your app to implement link caching. Use SQLite as the relational database. Follow the same process:

- Chat about the design, DB schema, and other details

- Produce a revised spec that includes information on the database

- Prompt Claude to update the `plan.md` document to include DB caching using the information in the spec

- Build and test incrementally, then test yourself. Try contructing a chain, then running it again to verify that the second version uses the cache and completes much faster.




