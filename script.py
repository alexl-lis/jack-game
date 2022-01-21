import tkinter
from tkinter import ttk
from tkinter.constants import DISABLED, NORMAL
from turtle import back, bgcolor, width
from venv import create
from Quiz import Quiz
from time import sleep

from Player import Player
from Story import Story

story = Story()
player = Player()

window = tkinter.Tk()
window.title("Информатика")
window.geometry("600x600")

menu = ttk.Notebook(window)

statusTab = ttk.Frame(menu)
menu.add(statusTab, text = "Статус")

def getStory():
    statusText.configure(text=story.getCurrentChapter()["text"])
    img.configure(file=f'./images/jack/{story.getCurrentChapter()["imageUrl"]}')
    if "enable" in story.getCurrentChapter():
        quizes[story.getCurrentChapter()["enable"]].enable()
        quizButtons[story.getCurrentChapter()["enable"]]["state"] = NORMAL


statusText = tkinter.Label(statusTab, text=story.getCurrentChapter()["text"], font="Verdana 12 ")
statusText.grid(column=1, row=0, columnspan=3)

canvas = tkinter.Canvas(statusTab, height=300, width=300)
img = tkinter.PhotoImage(file = f'./images/jack/{story.getCurrentChapter()["imageUrl"]}') 
image = canvas.create_image(0, 0, anchor='nw',image=img)
canvas.grid(column=1, row=1, columnspan=3)

def nextStory():
    story.currentChapter += 1
    getStory()

nextButton = tkinter.Button(statusTab, text="Далее", command=nextStory)
nextButton.grid(column=2, row=2, columnspan=1)

mapTab = ttk.Frame(menu)
menu.add(mapTab, text="Карта")

gameMap = tkinter.Canvas(mapTab, height=900, width=900, bg = 'white')

map = tkinter.PhotoImage(file = './images/map.png') 
gameMap.create_image(0, 0, anchor='nw',image=map)

for i in range(17):
    gameMap.create_line(50*(i + 1), 0, 50*(i + 1), 900, dash=(2,4), fill="white")
    gameMap.create_line(0, 50*(i + 1), 900, 50*(i + 1), dash=(2,4), fill="white")

spriteImage = tkinter.PhotoImage(file = './images/jack/sprites/up.png')
gameMap.create_image(player.x * 50, player.y * 50, anchor='nw',image=spriteImage)

def renderMap():
    gameMap.create_image(0, 0, anchor='nw',image=map)
    for i in range(17):
        gameMap.create_line(50*(i + 1), 0, 50*(i + 1), 900, dash=(2,4), fill="white")
        gameMap.create_line(0, 50*(i + 1), 900, 50*(i + 1), dash=(2,4), fill="white")
    gameMap.create_image(player.x * 50, player.y * 50, anchor='nw',image=spriteImage)

def move(event):
    if(event.keycode == 39):
        player.moveRight(1)
        spriteImage.configure(file = './images/jack/sprites/right.png')
        renderMap()
    elif(event.keycode == 38):
        player.moveUp(1)
        spriteImage.configure(file = './images/jack/sprites/up.png')
        renderMap()
    elif(event.keycode == 37):
        player.moveLeft(1)
        spriteImage.configure(file = './images/jack/sprites/left.png')
        renderMap()
    elif(event.keycode == 40):
        player.moveDown(1)
        spriteImage.configure(file = './images/jack/sprites/down.png')
        renderMap()


gameMap.bind("<Key>", move)

gameMap.pack()


quizTab = ttk.Frame(menu)
menu.add(quizTab, text = "Викторина")

menu.pack(expand=1, fill="both")

quizes = [
    Quiz("Проверка", 
    [
        {
            "question" : "Сколько символов в двоичной системе счисления?",
            "answers" : [
                "8",
                "1",
                "2",
                "20"
            ],
            "correct" : 2
        },
        {
            "question" : "Сколько будет 2 в 5ой степени?",
            "answers" : [
                "8",
                "16",
                "32",
                "10"
            ],
            "correct" : 2
        },
        {
            "question" : "Какая часть компьютера отвечает за скорость выполнения задач?",
            "answers" : [
                "Процессор",
                "Видеокарта",
                "Материнская плата",
                "Жесткий диск"
            ],
            "correct" : 0
        },
        {
            "question" : "Минимальная единица измерения информации?",
            "answers" : [
                "Байт",
                "Кбайт",
                "Мбайт",
                "Бит"
            ],
            "correct" : 3
        },
        {
            "question" : "Сколько битов в байте?",
            "answers" : [
                "1024",
                "8",
                "12",
                "16"
            ],
            "correct" : 1
        }
    ]),
    Quiz("Витокрина 2", [
        {
            "question" : "А",
            "answers" : [
                "Б",
                "В",
                "Г",
                "Я"
            ],
            "correct" : 2
        },
        {
            "question" : "Почему?",
            "answers" : [
                "Потому",
                "не знаю",
                "Ладно",
                "Почему?"
            ],
            "correct" : 2
        }
    ])
]

currentQuiz = False

quizButtons = []

def clearQuizTab():
    for widget in quizTab.winfo_children():
        widget.destroy()

def showQuizes():
    clearQuizTab()
    i = 0
    for quiz in quizes:
        quizButton = tkinter.Button(quizTab, text=quiz.title, command=lambda i=i: showQuiz(i))
        if quiz.disabled:
            quizButton["state"] = DISABLED
        quizButtons.append(quizButton)
        quizButton.pack()
        i += 1

showQuizes()

quizAnswers = []

quizText = False

def nextQuestion(ans):
    global quizText
    if ans == quizes[currentQuiz].getCurrentQuestion()["correct"]:
        quizes[currentQuiz].score +=1
    if quizes[currentQuiz].currentQuestion != len(quizes[currentQuiz].chapters) - 1:
        quizes[currentQuiz].currentQuestion += 1
        quizText.configure(text=quizes[currentQuiz].getCurrentQuestion()["question"])
        for i in range(4):
            print(quizes[currentQuiz].getCurrentQuestion()["answers"])
            quizAnswers[i].configure(text=quizes[currentQuiz].getCurrentQuestion()["answers"][i])
    else:
        for quizAnswer in quizAnswers:
            quizAnswer.destroy()
            if quizes[currentQuiz].score == 1:
                b = "балл"
            elif quizes[currentQuiz].score in [2,3,4]:
                b = "балла"
            elif quizes[currentQuiz].score in [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]:
                b = "баллов"
        quizText.configure(text=f"Вы набрали {quizes[currentQuiz].score} {b}!")
        backButton =tkinter.Button(quizTab, text = "Назад", command=showQuizes)
        backButton.pack()


def showQuiz(i):
    clearQuizTab()
    global currentQuiz
    global quizText
    currentQuiz = i
    quizText = tkinter.Label(quizTab, text=quizes[i].getCurrentQuestion()["question"], font="Verdana 14")
    quizText.pack()
    for i in range(4):
        quizAnswer = tkinter.Button(quizTab, text=quizes[currentQuiz].getCurrentQuestion()["answers"][i], command=lambda ans=i: nextQuestion(ans))
        quizAnswer.pack()
        quizAnswers.append(quizAnswer)
    


window.mainloop()