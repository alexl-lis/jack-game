class Story:
    chapters = [
        {
            "text" : "Привет! Меня зовут Джек! Это игра посвящена информатике!",
            "imageUrl" : "main.png"
        },
        {
            "text" : "Устройство пк",
            "imageUrl" : "run.png"
        },
        {
            "text" : "Отлично! Теперь отвечай на вопросы, при этом ты зарабатываешь очки!",
            "imageUrl" : "run.png" 
        },
        {
            "text" : "Молодец! Теперь беги к восклицательному знаку!",
            "imageUrl" : "main.png"
        },
        {
            "text" : "Ты набрал x очков! Игра Ты прошел игру. Для того, чтобы увеличить свой результат, попробуй пройти игру снова. Для этого перезапусти ее.",
            "imageUrl" : "run.png",
            "enable" : 1
        }
    ]
    currentChapter = 0

    def getCurrentChapter(self):
        return self.chapters[self.currentChapter]
