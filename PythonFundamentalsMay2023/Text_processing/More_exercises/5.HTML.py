title_article = input()
content_article = input()
comments = input()

print(f"<h1>\n\t{title_article}\n</h1>")
print(f"<article>\n\t{content_article}\n</article>")

while comments != "end of comments":
    print(f"<div>\n\t{comments}\n</div>")
    comments = input()
