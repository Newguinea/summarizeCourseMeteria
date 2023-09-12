from tika import parser # pip install tika

raw = parser.from_file('sample.pdf')
print(raw['content'])