from bs4 import BeautifulSoup

with open("website.html", "r") as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")

# print(soup.prettify())

print(soup.title)
print(soup.a)
print(soup.find("a"))
print(soup.select_one("a"))
print(soup.find_all("a"))
print(soup.select("a"))

print(soup.find("h1").get("id"))
print(soup.find("h1")["id"]) # same as above

print(soup.find("p").get_text(separator=" ")) # same as .text but args
print(soup.find("p").string) # returns None if tags
print(soup.find('p').text) # returns text without tags

print(soup.find_all("h3", class_="heading")) # class_ is used to avoid conflict with Python keyword

# selectors - 
print(soup.select("li"))  # with list
print(soup.select_one("li")) # with single element

for item in soup.select("li"):
    print(item.get_text())
    
for item in soup.select("a"):
    print(item.get("href"))

company_url = soup.select_one("p a").get("href")
print(company_url)