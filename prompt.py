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


def prompt_llm(document: str, prompt: str, system_msg: str, max_tokens: int = 1024):
    client = openai_connect()

    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": system_msg
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


def summary():
    with open("summary_prompts.txt") as f:
        prompts = f.readlines()

    with open("summary_results.csv", "w") as f:
        # prompt syllabus with tables
        has_tables = 'syllabi/has_tables'
        for file in os.listdir(has_tables):
            for prompt in prompts:
                print(f"starting prompt: {prompt}")
                file_path = os.path.join(has_tables, file)
                document = extract_document_contents(file_path)
                output = prompt_llm(document, prompt,
                                    f"You are an assistant to summarize a syllabus. Produce an output of the given length in the format:\nSummary of <course prefix> - <course title>: ")
                f.write(f"{prompt}\n{file.rstrip('.pdf')}\n{output}\n")
                print(output)

            print(f"done with {file}")

        # prompt syllabus without tables
        no_tables = 'syllabi/no_tables'
        for file in os.listdir(no_tables):
            for prompt in prompts:
                print(f"starting prompt: {prompt}")
                file_path = os.path.join(no_tables, file)
                document = extract_document_contents(file_path)
                output = prompt_llm(document, prompt,
                                    f"You are an assistant to summarize a syllabus. Produce an output of the given length in the format:\nSummary of <course prefix> - <course title>: ")
                f.write(f"{prompt}\n{file.rstrip('.pdf')}\n{output}\n")
                print(f"done with: {prompt}")
                print(output)

            print(f"done with {file}")


def qa():
    with open("qa_prompts.txt") as f:
        prompts = f.readlines()

    with open("qa_results.csv", "w") as f:
        # prompt syllabus with tables
        has_tables = 'syllabi/has_tables'
        for file in os.listdir(has_tables):
            for prompt in prompts:
                print(f"starting prompt: {prompt}")
                file_path = os.path.join(has_tables, file)
                document = extract_document_contents(file_path)
                output = prompt_llm(document, prompt,
                                    f"You are an assistant to answer questions about a syllabus. Provide concise and accurate answers to the questions below in the following format:\nCourse Title: \nQuestion: \nAnswer: ")
                f.write(f"{prompt}\n{file.rstrip('.pdf')}\n{output}\n")
                print(output)

            print(f"done with {file}")

        # prompt syllabus without tables
        no_tables = 'syllabi/no_tables'
        for file in os.listdir(no_tables):
            for prompt in prompts:
                print(f"starting prompt: {prompt}")
                file_path = os.path.join(no_tables, file)
                document = extract_document_contents(file_path)
                output = prompt_llm(document, prompt,
                                    f"You are an assistant to answer questions about a syllabus. Provide concise and accurate answers to the questions below in the following format:\nCourse Title: \nQuestion: \nAnswer: ")
                f.write(f"{prompt}\n{file.rstrip('.pdf')}\n{output}\n")
                print(f"done with: {prompt}")
                print(output)

            print(f"done with {file}")


if __name__ == '__main__':
    # summary()
    qa()
