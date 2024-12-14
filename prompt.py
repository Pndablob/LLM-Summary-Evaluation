import os

import pdfplumber
from openai import OpenAI


def openai_connect():
    with open('token.txt', 'r') as file:
        _organisation_tkn, _project_tkn, _open_ai_tkn = file.read().splitlines()

    client = OpenAI(
        organization=_organisation_tkn,
        project=_project_tkn,
        api_key=_open_ai_tkn
    )

    return client


def extract_document_contents(file_path: str) -> str:
    with pdfplumber.open(file_path) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text() + '\n'
        return text


def prompt_llm(document: str, prompt: str, max_tokens: int = 1024):
    client = openai_connect()

    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": f"You are an assistant to summarize a syllabus. Produce an output of the given length in the format:\n"
                               f"Summary of <course prefix> - <course title>: "
                },
                {
                    "role": "user",
                    "content": f"{prompt}\n{document}",
                }
            ],
            model="gpt-4o-mini",
            max_completion_tokens=max_tokens
        )
        return response.to_dict()['choices'][0]['message']['content']
    except Exception as e:
        print("An error occurred:", e)
        return None


with open("prompts.txt") as f:
    prompts = f.readlines()

with open("results.csv", "w") as f:
    for prompt in prompts:
        print(f"starting prompt: {prompt}")
        # prompt syllabus with tables
        has_tables = 'syllabi/has_tables'
        for file in os.listdir(has_tables):
            file_path = os.path.join(has_tables, file)
            document = extract_document_contents(file_path)
            output = prompt_llm(document, prompt)
            f.write(f"{prompt},{file.rstrip('.pdf')},\"{output}\"\n")
            print(f"done with {file}")
            print(output)

        # prompt syllabus without tables
        no_tables = 'syllabi/no_tables'
        for file in os.listdir(no_tables):
            file_path = os.path.join(no_tables, file)
            document = extract_document_contents(file_path)
            output = prompt_llm(document, prompt)
            f.write(f"{prompt},{file.rstrip('.pdf')},\"{output}\"\n")
            print(f"done with {file}")
            print(output)

        print(f"done with {prompt}")
