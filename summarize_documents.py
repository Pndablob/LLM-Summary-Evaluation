import pdfplumber
from openai import OpenAI
import os


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


def summarize_document(document: str, prompt: str, model: str = "gpt-4o-mini", max_tokens: int = 1024):
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
            model=model,
            max_completion_tokens=max_tokens
        )
        return response.to_dict()['choices'][0]['message']['content']
    except Exception as e:
        print("An error occurred:", e)
        return None


if __name__ == '__main__':
    pass
    # implement storing llm outputs in a json/dictionary

    # has tables
    print("Summarizing documents with tables")
    has_tables = 'syllabi/has_tables'
    for file in os.listdir(has_tables):
        file_path = os.path.join(has_tables, file)
        document = extract_document_contents(file_path)
        summary = summarize_document(document)
        print(summary)

    # # no tables
    # print("\nSummarizing documents without tables")
    # no_tables = 'syllabi/no_tables'
    # for file in os.listdir(no_tables):
    #     file_path = os.path.join(no_tables, file)
    #     document = extract_document_contents(file_path)
    #     summary = summarize_document(document)
    #     print(summary)
    #     print()
