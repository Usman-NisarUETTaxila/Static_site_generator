import markdown2 

with open('test.md', 'r', encoding='utf-8') as markdown_file:
    text = markdown_file.read()

html_code = markdown2.markdown(text)

with open('output.html', 'w', encoding='utf-8') as html_file:
    html_file.write(html_code)

