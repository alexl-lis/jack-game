class Story:
    chapters = [
        {
            "text" : "Привет! Меня зовут Джек! Это игра посвящена информатике!",
            "imageUrl" : "main.png"
        },
        {
            "text" : "Сейчас перейди на вкладку викторина и пройди первую!",
            "imageUrl" : "run.png",
            "enable" : 0
        },
        {
            "text" : "Пройди уровень, чтобы продвинуться дальше",
            "imageUrl" : "run.png" 
        },
        {
            "text" : "4",
            "imageUrl" : "main.png"
        },
        {
            "text" : "я морж",
            "imageUrl" : "run.png" 
        }
    ]
    currentChapter = 0

    def getCurrentChapter(self):
        return self.chapters[self.currentChapter]
