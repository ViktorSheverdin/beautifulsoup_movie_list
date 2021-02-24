from bs4 import BeautifulSoup
import requests
response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
links = soup.find_all(name='a', class_="storylink")
upvote = soup.find(name="span", class_="score").getText()
print(f"""
Article: {links[0].string}
\nlink: {links[0].get('href')}
\nupvote: {upvote}
""")
# print()
# print(f"Article: {links[0]}")
