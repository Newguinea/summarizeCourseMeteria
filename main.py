import os
from langchain.text_splitter import RecursiveCharacterTextSplitter

openfile = './text/5504/10_may.txt'#please tell where is the file
prompt = "this is a lecture recording, I want you to take notes and summary the knowledge point and brief describe\
 each knowledge point"

file_path = openfile[:openfile.rindex('/') + 1]
file_name = openfile[openfile.rindex('/') + 1:]
file_out_name = "output_" + file_name
with open(openfile, 'r', encoding='utf-8') as file:
    file_content = file.read()


text = file_content
text = text.replace("\n", " ")
text_splitter = RecursiveCharacterTextSplitter(separators=[" ", "\n", "\t"],
                                                       chunk_size=10000,
                                                       chunk_overlap=3000)
docs = text_splitter.create_documents([text])

out = ""
for doc in docs:
    out += prompt + "\n"
    out += str(doc)
    out += "\n \n \n"


if os.path.exists(file_path + file_out_name):
    os.remove(file_path + file_out_name)


with open(file_path + file_out_name, 'w', encoding='utf-8') as f:
    f.write(out)