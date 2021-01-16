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
        if result != None:
            result = result.get_text()
        votes = results.find('div', class_="fd-column").find('div', class_="ai-center")
        if votes != None:
            votes = votes.get_text()
        user_name = results.find('div', class_="user-details").find('a')
        if user_name != None:
            user_name = user_name.get_text()
        with open("scrapped_data.txt", "w") as f:
            f.write(result[:500])
            if user_name != None:
                f.write(user_name)
            if votes != None:
                f.write(votes)
        return Answer(URL, result[:500], votes, user_name)


if __name__ == "__main__":
    url = get_url()
    scrap_data(url)
