import requests
from bs4 import BeautifulSoup
from data_models import Answer


def get_url():
    return 'https://stackoverflow.com/questions/9662346/python-code-to-remove-html-tags-from-a-string'


def scrap_data(URL):
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find(id='answers')
    if results == None:
        print("NO ANSWERS")
        return Answer(URL, None, None, None)
    else:
        result = results.find('div', 'js-post-body')
        votes = results.find('div', class_="ai-center")
        user_name = results.find('div', class_="user-details").find('a')
        with open("scrapped_data.txt", "w") as f:
            f.write(result.get_text()[:500])
        return Answer(URL, result, votes, user_name)


if __name__ == "__main__":
    url = get_url()
    scrap_data(url)
