import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

try:
    response = requests.get(URL)
    response.raise_for_status()
    content = response.text
except requests.RequestException as e:
    print(f"An error occurred while fetching the URL: {e}")
else:
    soup = BeautifulSoup(content, "html.parser")
    
    headings = soup.find_all(name="h3", class_="title")
    movie_titles = [heading.getText() for heading in headings]
    
    with open("movies.txt", "w", encoding="utf-8") as file:
        for n in range(len(movie_titles) - 1, 0, -1):
            file.write(f"{movie_titles[n]}\n")
    print("Movie titles have been successfully written to movies.txt.")
    

