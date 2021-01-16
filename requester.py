from googlesearch import search
from data_models import Data, DataFrame, Answer
from scrapper import scrap_data
from utils import save_to_json


def get_query():
    query = ["error: incompatible types: String cannot be converted to int",
             "TypeError: unsupported operand type(s) for +: 'int' and 'str'"]
    return query


def send_requests(site):
    data = Data()

    for q in get_query():
        dataframe = DataFrame(q)
        for j in search(q+f" site:{site}", tld="co.in", num=2, stop=2, pause=2):
            dataframe.add_answer(scrap_data(j).__dict__)
        data.add_dataframe(dataframe.__dict__)

    save_to_json("data.json", data.__dict__)


if __name__ == "__main__":
    send_requests("stackoverflow.com")
