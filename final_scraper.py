import requests
import bs4
from collections import Counter

# Title Text Block
print("GOOGLE SCRAPING USING PY3 AND BS4 \n")

# Accepts Search Keywords from the User
keyword = input("ENTER SEARCH KEYWORDS: ")

# Setting Query Parameters for Search
params = [('q', keyword)]

# Google Search URL
url = "https://google.co.in/search"

# Gets response from the server for the search query
response = requests.get(url=url, params=params)

# Response text from server is parsed using bs4
soup = bs4.BeautifulSoup(response.text, 'lxml')

titles = soup.find_all("h3")

#Result is Displayed

print("\nDISPLAYING FIRST PAGE RESULT TITLES FOR " + keyword + "\n")

x = 0 # counter variable
for title in titles: # loop to display titles
    x = x+1 # counter updated
    TITLE = str(x) + ". " + title.get_text()
    # print(str(x) + ". " + title.get_text())
    # print(title.find_parent('div'))
    URL = title.find_parent('div').find_all("a")[0]['href'][7:]
    # print(title.find_parent('div').find_all("a")[0]['href'][7:])
    # Related urls
    temp_soup = bs4.BeautifulSoup(requests.get(URL).text, "html.parser")

    foundUrls = Counter(
        [link for link in temp_soup.find_all("a", href=lambda href: href and not href.startswith("#"))])
    foundUrls = foundUrls.most_common()

    RELATED_URLS = 'URL | COUNT\n'
    for item in foundUrls:
        # print("%s: %d" % (item[0], item[1]))
        RELATED_URLS += str(item[0]) + " | " + str(item[1]) + " \n "

    # print(len(foundUrls))
    filename = keyword + ".txt"
    with open(filename, "a", encoding="utf-8") as f:
        f.write("%s :\nURL :%s\nRELATED URLS :%s\n\n" % (TITLE, URL, RELATED_URLS))
