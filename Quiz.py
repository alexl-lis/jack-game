class Quiz:
    score = 0
    currentQuestion = 0
    disabled = True

    def __init__(self, title, chapters):
        self.title = title
        self.chapters = chapters

    def getCurrentQuestion(self):
        return self.chapters[self.currentQuestion]

    def enable(self):
        self.disabled = False
