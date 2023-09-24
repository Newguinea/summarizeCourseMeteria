from tika import parser # pip install tika
import re

raw = parser.from_file('./pdf/mvp.pdf')
content = raw['content']

# change the `/n+` to ' '
content = re.sub(r'\n+', ' ', content)

print(content)