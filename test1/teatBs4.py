from bs4 import BeautifulSoup

file = open("./百度一下，你就知道.html", "rb")
html = file.read()
bs = BeautifulSoup(html, "html.parser")
print(bs.)
