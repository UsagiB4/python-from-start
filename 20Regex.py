# Regex is used to search pattern or sequence in a string.
import re

some_text = "Hello! this  is Ron. Here is my Email: ronlovecat@dmail.com. \n I have a brother called John. Here's his Email: johntheman@dmail.com."
temp_str = some_text.split('\n')
print(temp_str)

for words in temp_str:
    mail_search = re.search("([\w.-]+)@([\w.-]+)", words)
    print(mail_search.group())

