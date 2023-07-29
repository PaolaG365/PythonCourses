import re
'''
it's broken with <html>\n<head><title>News</title></head>\n<body><p><a href="https://softuni.bg">
SoftUni</a>aims   to provide free real-world practical\n training for young people who want to turn into\n
skillful Python software engineers.</p></body>\n</html>
'''

pattern = re.compile(r"<title>(.+)</title>")
content_pattern = re.compile(r"<body>(.+)</body>")

whitespaces = re.compile(r" +")
new_line_tab = re.compile(r"\\n|\\t")
tags = re.compile(r"<[^>]*>")

text = input()

title = re.search(pattern, text)
content = re.search(content_pattern, text)

title = re.sub(whitespaces, " ", re.sub(new_line_tab, "", re.sub(tags, "", title.group())))
content = re.sub(whitespaces, " ", re.sub(new_line_tab, "", re.sub(tags, "", content.group())))

print(f"Title: {title}")
print(f"Content: {content}")
