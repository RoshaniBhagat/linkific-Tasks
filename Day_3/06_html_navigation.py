from bs4 import BeautifulSoup

with open("navigation.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

container = soup.find("div")

print("Parent of h1:")
print(soup.h1.parent.name)

print("\nChildren of div:")
for child in container.children:
    if child.name:
        print(child.name)

print("\nNext sibling of first paragraph:")
first_para = soup.find("p")
print(first_para.find_next_sibling().text)

print("\nPrevious sibling of link:")
link = soup.find("a")
print(link.find_previous_sibling().text)