import re

def converter(text):
    # Cabeçalhos
    ## H1
    text = re.sub(r'^#(\s.*)$', r'<h1>\1</h1>', text, flags=re.MULTILINE)
    ## H2
    text = re.sub(r'^##(\s.*)$', r'<h2>\1</h2>', text, flags=re.MULTILINE)
    ## H3
    text = re.sub(r'^###(\s.*)$', r'<h3>\1</h3>', text, flags=re.MULTILINE)

    # BOLD
    text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)

    # ITALICO
    text = re.sub(r'\*([^\*]*)\*', r'<i>\1</i>', text)

    # LISTA NUMERADA
    text = re.sub(r'^\s*\d+\.\s+(.+)$', r'<li>\1</li>', text, flags=re.MULTILINE)

    # IMAGEM
    text = re.sub(r'!\[([^\]]*)\]\(([^\)]*)\)', r'<img src="\2" alt="\1"/>', text)

    # LINK
    text = re.sub(r'\[([^\]]*)\]\(([^\)]*)\)', r'<a href="\2">\1</a>', text)


    isFirst = True
    hasStarted = False
    finalText = ""
    # Check list
    for line in text.splitlines():
        if line.startswith("<li>") and isFirst:
            finalText += "<ol>\n" + line+"\n"
            isFirst = False
            hasStarted = True
        elif hasStarted and not line.startswith("<li>"):
            finalText += "</ol>\n" + line+"\n"
            isFirst = True
            hasStarted = False
        else:
            finalText += line+"\n"

    return finalText


def main():

    finalHTMLText = """
<!DOCTYPE html>
<html lang="pt PT">
<head>
    <title>Pagina</title>
    <meta charset="utf-8">
</head>
    
<body>
    
"""

    with open("inputFile.md") as file:
        finalHTMLText += converter(file.read())


    finalHTMLText += "\n\n</body>"

    with open("outputFile.html", "w") as file:
        file.write(finalHTMLText)

if __name__ == "__main__":
    main()