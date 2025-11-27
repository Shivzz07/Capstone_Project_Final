Template for creating and submitting MAT496 capstone project.

# Overview of MAT496

In this course, we have primarily learned Langgraph. This is helpful tool to build apps which can process unstructured `text`, find information we are looking for, and present the format we choose. Some specific topics we have covered are:

- Prompting
- Structured Output 
- Semantic Search
- Retreaval Augmented Generation (RAG)
- Tool calling LLMs & MCP
- Langgraph: State, Nodes, Graph

We also learned that Langsmith is a nice tool for debugging Langgraph codes.

------

# Capstone Project objective

The first purpose of the capstone project is to give a chance to revise all the major above listed topics. The second purpose of the capstone is to show your creativity. Think about all the problems which you can not have solved earlier, but are not possible to solve with the concepts learned in this course. For example, We can use LLM to analyse all kinds of news: sports news, financial news, political news. Another example, we can use LLMs to build a legal assistant. Pretty much anything which requires lots of reading, can be outsourced to LLMs. Let your imagination run free.


-------------------------

# Project report Template

## Title: [Personalized AI Study Notes & FlashCards Generator]

## Overview

[his project converts long academic PDFs or notes into structured learning content.
Using LangGraph workflow, the system:

1) Extracts text from PDFs

2) Splits into chunks + embeds into vector DB

3) Runs semantic RAG-based retrieval

4) Generates chapter-wise summaries

5) Extracts key concepts and formulas.

6) Tries to auto-create study ready flashcards based on the given data.]

## Reason for picking up this project

This demonstrates prompting, RAG, semantic search, structured output, tool-calling & LangGraph orchestrations which I think matches the course outcomes and the capstone project requirements.

## Plan

I plan to excecute these steps to complete my project.

- [TODO] Step 1: Create repo + add project folder structure

- [TODO] Step 2: Load and preprocess PDF (LangChain PDFLoader)

- [TODO] Step 3: Create text chunks and embeddings

- [TODO] Step 4: Build vector store (FAISS/Chroma)

- [TODO] Step 5: Implement RAG summarization node

- [TODO] Step 6: Build flashcard generation node

- [TODO] Step 7: Connect all with LangGraph

- [TODO] Step 8: Test with sample PDFs + format final output

- [TODO] Step 9: Write final documentation + report

## Conclusion:

I had planned to achieve {this this}. I think I have/have-not achieved the conclusion satisfactorily. The reason for your satisfaction/unsatisfaction.

----------

# Added instructions:

- This is a `solo assignment`. Each of you will work alone. You are free to talk, discuss with chatgpt, but you are responsible for what you submit. Some students may be called for viva. You should be able to each and every line of work submitted by you.

- `commit` History maintenance.
  - Fork this respository and build on top of that.
  - For every step in your plan, there has to be a commit.
  - Change [TODO] to [DONE] in the plan, before you commit after that step. 
  - The commit history should show decent amount of work spread into minimum two dates. 
  - **All the commits done in one day will be rejected**. Even if you are capable of doing the whole thing in one day, refine it in two days.  
 
 - Deadline: Nov 30, Sunday 11:59 pm


# Grading: total 25 marks

- Coverage of most of topics in this class: 20
- Creativity: 5
  
