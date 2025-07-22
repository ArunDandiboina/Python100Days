from bs4 import BeautifulSoup
import requests

# ETHICS - site.com/robots.txt.


# static
# url = "https://appbrewery.github.io/news.ycombinator.com/"

# live
url = "https://news.ycombinator.com/news"


response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

scores = soup.find_all(name="span", class_="score")
names = soup.find_all(name="span", class_="titleline")
links = soup.select(".title > span.titleline > a")

scores_int = [int(s.get_text().split()[0]) for s in scores]
names_text = [n.get_text() for n in names]
links = [l.get("href") for l in links]   

# print("Scores:", scores_int)
# print("Names:", names_text)
# print("Links:", links)

max_score_index = scores_int.index(max(scores_int))
highest_score = scores_int[max_score_index]
highest_name = names_text[max_score_index]
highest_link = links[max_score_index]

print(f"Highest score: {highest_score}")
print(f"Name: {highest_name}")
print(f"Link: {highest_link}")

# top 3 scores
# top_3_scores = sorted(scores_int, reverse=True)[:3]
# print("Top 3 scores:", top_3_scores)

# for score in top_3_scores:
#     index = scores_int.index(score)
#     print(f"Name: {names_text[index]}, Score: {score}, Link: {links[index]}")