from googlesearch import search
from libraries.data_models import Data, DataFrame, Answer
from libraries.scrapper import scrap_data
from libraries.utils import save_to_json
from libraries.config import NUM_OF_ANS, SITE


def send_requests(query):
    data = Data()

    for q in query:
        dataframe = DataFrame(q)
        for j in search(q+f" site:{SITE}", tld="co.in", num=NUM_OF_ANS, stop=NUM_OF_ANS, pause=2):
            dataframe.add_answer(scrap_data(j).__dict__)
        data.add_dataframe(dataframe.__dict__)

    save_to_json("data.js", data.__dict__)


if __name__ == "__main__":
    query = ["error: incompatible types: String cannot be converted to int",
             "TypeError: unsupported operand type(s) for +: 'int' and 'str'"]
    send_requests("stackoverflow.com", query)
