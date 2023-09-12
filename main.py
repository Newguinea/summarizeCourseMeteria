import os
from langchain.text_splitter import RecursiveCharacterTextSplitter


def read_file_content(filepath):
    """Read and return the content of the given file."""
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()


def write_to_file(filepath, content):
    """Write the content to the specified file. If the file exists, it will be removed before writing."""
    file_path = filepath[:filepath.rindex('/') + 1]
    file_name = filepath[filepath.rindex('/') + 1:]
    file_out_name = "output_" + file_name
    output_path = file_path + file_out_name

    # Remove the file if it already exists
    if os.path.exists(output_path):
        os.remove(output_path)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)


def generate_prompt(file_content, prompt="this is the recording of the class, summary all the content detailed"):
    """
    Generate prompt content based on a given prompt and file content.

    Parameters:
    - file_content (str): Content from the input file.
    - prompt (str): Prompt string to prepend the summary.

    Returns:
    - out (str): Generated content with prompt.
    """

    # Process the content
    text = file_content.replace("\n", " ")
    text_splitter = RecursiveCharacterTextSplitter(separators=[" ", "\n", "\t"],
                                                   chunk_size=10000,
                                                   chunk_overlap=3000)
    docs = text_splitter.create_documents([text])

    # Create the output content
    out = ""
    for doc in docs:
        out += prompt + "\n"
        out += str(doc)
        out += "\n \n \n"

    return out


# Example Usage
input_path = './text/5506/28_aug.txt'
prompt = 'this is the recording of the class, summary all the content detailed'

content = read_file_content(input_path)
generated_content = generate_prompt(content, prompt=prompt)
write_to_file(input_path, generated_content)
