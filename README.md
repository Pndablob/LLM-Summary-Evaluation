[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/qve1z1U2)
# Final Project - Exploring LLM Capabilities

## Learning Objectives 
1.	Learn the skill of prompt engineering
2.	Learn how to use prompt templates to automate LLM prompting
3.	Learn how to parse LLM output
4.	Explore the capabilities and limits of LLM

## Project 

In this project, you will team up with 2 other Artificial Intelligence students to form a group that will explore the limits of LLMs (specifically gpt4o-mini). You will be provided with a OpenAI endpoint which you will access via REST requests. You and your colleagues will collaborate in the same GIT repository, be sure to commit often so course staff can monitor your progress. Git commits will also be used as proof of collaboration, this is a group project so one student doing all the work is not allowed and you will be penalized if that is the case. 

Once you have a team, you will brainstorm on an idea that involves generating structured or unstructured text using an LLM. Try out your idea on 383GPT to get a sense of what is possible. Include your findings in your project proposal where you indicate the models capabilties on a single prompt. You are free to choose the discipline, it can be science, poetry, literature, language etc. Write a draft of the idea, providing details on the problem, the dataset that you will use and how you will evaluate the performance of the LLM. Submit a draft on gradescope, a course staff will be assigned to mentor you during the 8 weeks of the project.

There are many datasets available online, a good place to start your search is the huggingface dataset repository. Kaggle and the UCI data repository might also have good datasets to use. You are also free to generate your own dataset. Large datasets require more compute, limit yourself to 300-500 entries. You will need to ensure that the subset of the dataset is balanced. 

Now that you have a balanced dataset, your team needs to come up with different ways to prompt a LLM using your dataset as input. Once you have a list of prompts, you will need to abstract the prompts such that you can iterate through your dataset using your code. We will refer to these prompt abstractions as Prompt Templates. You can review online prompt template repositories to get a good idea. It can be difficult to parse LLM response because of non-standard responses, it is a good idea to manually prompt the LLM first to get a sense of what logic is needed to parse your LLM responses.

Your team will design a human evaluation protocol to measure the performance of the LLM. Depending on your problem, a simple exact match may suffice, other cases may need more robust evaluation. What makes a good, average or bad response? What are the weaknesses/biases of your evaluation? Is your approach reproducible? What are the steps needed to automate your evaluation approach? Your mentors will be there to help with the design choices, but you will need to document what you considered and the justification for the evaluation protocol in your final report. Remember to include actual examples to of the different nuances you uncover. Good luck, we can’t wait to read all the ideas that you will come up with.

## Important Dates 
| Date  | Milestone | Grade  |
| --------- | --------- | --------- |
| 10/4 | Group project details released | -|
| 10/15 | Submit document listing group members. Submit first draft of project idea. Draft should be PDF, max 300 words. | 5%|
| 10/18 | Group mentor assigned. | -|
| 11/01 | Submit final draft for project idea. Draft should be PDF, max 300 words. Approval by group mentor.| 10% |
| 11/30 | At least one update meeting with mentor.| 10% |
| 12/06 | Submit code repository and report for final project. Report should be PDF, max 900 words.| 75%|

## Examples
* Generating SQL code from python panda code
* Generating sentences that rhyme but limited to a specific topic
* Generating a score for CVs given a job description
* Generating a summary of a 383 lecture

## Resources
API: https://platform.openai.com/docs/guides/text-generation

Huggingface Datasets: https://huggingface.co/datasets

Kaggle: https://www.kaggle.com/datasets

UCI Data Reposistory: https://archive.ics.uci.edu/datasets
