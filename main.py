import markdown2 
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader(searchpath='./'))
file = env.get_template('base.html')

with open('test.md', 'r', encoding='utf-8') as markdown_file:
    text = markdown_file.read()

html_code = markdown2.markdown(text)

with open('output.html', 'w', encoding='utf-8') as html_file:
    html_file.write(
        file.render(
            content="This is the content"
        )
    )

