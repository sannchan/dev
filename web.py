from bs4 import BeautifulSoup

filename = "./ftp/temp/index.php"
line_number = 24

with open(filename, "r") as file:
    for i, line in enumerate(file):
        if i == line_number - 1:
            soup = BeautifulSoup(line, "html.parser")
            p_tag = soup.find("p", {"class": "line3"})
            if p_tag:
                number = int(p_tag.text.replace("円", ""))
                print(number)
            break