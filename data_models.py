class Data:
    def __init__(self):
        self.data = []

    def add_dataframe(self, data):
        self.data.append(data)


class DataFrame:
    def __init__(self, error_name):
        self.errorName = error_name
        self.answers = []

    def add_answer(self, answer):
        self.answers.append(answer)


class Answer:
    def __init__(self, url, answerContent, votes, author):
        self.url = url
        self.answerContent = answerContent
        self.votes = votes
        self.author = author
