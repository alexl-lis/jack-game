from sqlite3 import enable_shared_cache
import tkinter
from tkinter import CENTER, ttk, messagebox
from tkinter.constants import DISABLED, NORMAL
import tkinter.font as tkFont
from Quiz import Quiz

quizes = [
    Quiz("Двоичная система счисления", 
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
            "question" : "Для чего используется двоичная система счисления?",
            "answers" : [
                "Для кодирования различных символов в компьютере",
                "Для создания моделей информационных систем",
                "Для решения логических задач",
                "Для передачи данных"
            ],
            "correct" : 0
        },
        {
            "question" : "После числа 111 в двоичном ряду идет число:",
            "answers" : [
                "101",
                "100",
                "112",
                "1000"
            ],
            "correct" : 3
        },
        {
            "question" : "Основанием двоичной системы счисления является число:",
            "answers" : [
                "11",
                "2",
                "12",
                "10"
            ],
            "correct" : 1
        }
    ]),
    Quiz("Алгерба логики", [
        {
            "question" : "Что такое Алгебра логики?",
            "answers" : [
                " это раздел математики, изучающий высказывания, рассматриваемые со стороны их логических значений (истинности или ложности) и логических операций над ними.",
                "это логическая алгебра ",
                "это алгебра с элементами логики",
            ],
            "correct" : 0
        },
        {
            "question" : "Конъюнкция - это",
            "answers" : [
                "это логическая операция, ставящая в соответствие каждым двум простым высказываниям составное высказывание, являющееся истинным тогда и только тогда, когда оба исходных высказывания истинны.",
                "это логическая операция, ставящая в соответствие каждым двум простым высказываниям составное высказывание, являющееся истинным тогда и только тогда, когда оба исходных высказывания ложны.",
                "Не помню",
                "Такого определения нет в алгебре логики"
            ],
            "correct" : 0
        },
        {
            "question" : "Как называется логическое отрицание?",
            "answers" : [
                "Конъюнкция",
                "Дизъюнкция",
                "Инверсия",
            ],
            "correct" : 2
        },
        {
            "question" : "Дизъюнкция - это",
            "answers" : [
                "логическая операция, ставящая в соответствие каждым двум простым высказываниям составное высказывание, являющееся истинным тогда и только тогда, когда оба исходных высказывания истинны.",
                "логическая операция, ставящая в соответствие каждым двум простым высказываниям составное высказывание, являющееся истинным тогда и только тогда, когда оба исходных высказывания ложны.",
                "Такого определения в алгебре логики нет.",
            ],
            "correct" : 1
        }
    ]),
    Quiz("Информация ", [
        {
            "question" : "Что такое информация?",
            "answers" : [
                " это раздел математики, изучающий высказывания, рассматриваемые со стороны их логических значений (истинности или ложности) и логических операций над ними.",
                " сведения об объектах окружающей среды, их параметрах, свойствах и состоянии, которые уменьшают имеющуюся о них степень неопределенности, неполно-ты знаний. ",
                "это один из видов позиционных систем счисления.",
            ],
            "correct" : 1
        },
        {
            "question" : "Кодирование информации - это",
            "answers" : [
                "Преобразование информации из одной формы представления в другую",
                "операция преобразования знаков или групп знаков одной знаковой системы в знаки или группы знаков другой знаковой системы. ",
                "Верно и то и то ",
                "Неверно и то и то"
            ],
            "correct" : 2
        },
        {
            "question" : "Обработка информации –",
            "answers" : [
                "Получение информации",
                "Внесение изменений в набор данных, вычисления, информационный поиск, сортировка, построение графиков и т.п.",
                "вся совокупность операций (сбор, ввод, запись, преобразование, считывание, хранение, уничтожение, регистрация),",
            ],
            "correct" : 2
        },
        {
            "question" : "Информацию, существенную и важную в настоящий момент, называют: ",
            "answers" : [
                " полезной",
                "актуальной",
                "достоверной",
                "объективной"
            ],
            "correct" : 1
        }
    ]),
    Quiz("Excel", [
        {
            "question" : "Основное назначение электронных таблиц-",
            "answers" : [
                "редактировать и форматировать текстовые документы",
                "хранить большие объемы информации",
                "выполнять расчет по формулам",
                "нет правильного ответа"
            ],
            "correct" : 2
        },
        {
            "question" : "Что позволяет выполнять электронная таблица?",
            "answers" : [
                "решать задачи на прогнозирование и моделирование ситуаций",
                "представлять данные в виде диаграмм, графиков",
                "при изменении данных автоматически пересчитывать результат",
                "выполнять чертежные работы"
            ],
            "correct" : 1
        },
        {
            "question" : " Основным элементом электронных таблиц является",
            "answers" : [
                "Цифры",
                "Ячейки",
                "Данные",
            ],
            "correct" : 1   
        },
        {
            "question" : "Какая программа не является электронной таблицей?",
            "answers" : [
                "Excel",
                "Quattropro",
                "Superkalk",
                "Word"
            ],
            "correct" : 3
        }
    ]),
]
from Player import Player
from Story import Story
from Tip import Tip

story = Story()
player = Player()

tips = [
    Tip(6, 6, "Двоичная система счисления", "Женя тупой даун"),
    Tip(10, 10, "Алгебра логики", "Описание 2"),
    Tip(4, 6, "Информация", "Описание 3"),
    Tip(15,11 , "Excel", "Описание 4"),
]

window = tkinter.Tk()
window.title("Информатика")
window.geometry("950x950")

menu = ttk.Notebook(window)

statusTab = ttk.Frame(menu)
menu.add(statusTab, text = "Статус")

def getStory():
    statusText.configure(text=story.getCurrentChapter()["text"])
    img.configure(file=f'./images/jack/{story.getCurrentChapter()["imageUrl"]}')
    if "enable" in story.getCurrentChapter():
        quizes[story.getCurrentChapter()["enable"]].enable()
        quizButtons[story.getCurrentChapter()["enable"]]["state"] = NORMAL


statusText = tkinter.Label(statusTab, text=story.getCurrentChapter()["text"], font="Verdana 12", width=95, wraplength=500, justify=CENTER, bg="#0260E8", fg="white")
statusText.grid(column=1, row=0, columnspan=3)

canvas = tkinter.Canvas(statusTab, height=300, width=300)
img = tkinter.PhotoImage(file = f'./images/jack/{story.getCurrentChapter()["imageUrl"]}') 
image = canvas.create_image(0, 0, anchor='nw',image=img)
canvas.grid(column=1, row=1, columnspan=3)

def nextStory():
    if("enable" in story.getCurrentChapter()):
        if(quizes[story.getCurrentChapter()["enable"]].score < len(quizes[story.getCurrentChapter()["enable"]].chapters)):
            current = story.getCurrentChapter()["enable"]
            messagebox.showwarning("Не пройдено", f"Cначала пройдите викторину под номером {current + 1}")
        else:
            story.currentChapter += 1
            getStory()
    else:
        story.currentChapter += 1
        getStory()

nextButton = tkinter.Button(statusTab, text="Далее", command=nextStory, bg = "#0260E8", fg = "white", font = "Verdana 12")
nextButton.grid(column=2, row=2, columnspan=1)

mapTab = ttk.Frame(menu)
menu.add(mapTab, text="Карта")

gameMap = tkinter.Canvas(mapTab, height=900, width=900, bg = 'white')

map = tkinter.PhotoImage(file = './images/map.png') 
gameMap.create_image(0, 0, anchor='nw',image=map)

for i in range(17):
    gameMap.create_line(50*(i + 1), 0, 50*(i + 1), 900, dash=(2,4), fill="white")
    gameMap.create_line(0, 50*(i + 1), 900, 50*(i + 1), dash=(2,4), fill="white")

tipImage = tkinter.PhotoImage(file='./images/gift.png')

for tip in tips:
    if not tip.picked:
        gameMap.create_image(tip.x *50, tip.y *50, anchor='nw', image=tipImage)

spriteImage = tkinter.PhotoImage(file = './images/jack/sprites/up.png')
gameMap.create_image(player.x * 50, player.y * 50, anchor='nw',image=spriteImage)


def renderMap():
    gameMap.create_image(0, 0, anchor='nw',image=map)
    for i in range(17):
        gameMap.create_line(50*(i + 1), 0, 50*(i + 1), 900, dash=(2,4), fill="white")
        gameMap.create_line(0, 50*(i + 1), 900, 50*(i + 1), dash=(2,4), fill="white")

    for tip in tips:
        if not tip.picked:
            gameMap.create_image(tip.x *50, tip.y *50, anchor='nw', image=tipImage)
        
    gameMap.create_image(player.x * 50, player.y * 50, anchor='nw',image=spriteImage)

def checkTips():
    for tip in tips:
        if(player.x == tip.x and player.y == tip.y):
            return tip
    else:
        return False


def move(event):
    if(event.keycode == 68):
        player.moveRight(1)
        spriteImage.configure(file = './images/jack/sprites/right.png')
    elif(event.keycode == 87):
        player.moveUp(1)
        spriteImage.configure(file = './images/jack/sprites/up.png')
    elif(event.keycode == 65):
        player.moveLeft(1)
        spriteImage.configure(file = './images/jack/sprites/left.png')
    elif(event.keycode == 83):
        player.moveDown(1)
        spriteImage.configure(file = './images/jack/sprites/down.png')
    if checkTips():
        tips[tips.index(checkTips())].picked = True
        showTips()
    renderMap()


window.bind("<Key>", move)

gameMap.pack()

tipTab = ttk.Frame(menu)
menu.add(tipTab, text = "Подсказки")

def clearTips():
    for widget in tipTab.winfo_children():
        widget.destroy()

def showTip(i):
    messagebox.showinfo(tips[i].title, tips[i].description)

def showTips():
    clearTips()
    for i, tip in enumerate(tips):
        if tip.picked:
            font = tkFont.Font(family="Calibri", size=20)
            tipButton = tkinter.Button(tipTab, 
                text=tip.title, 
                bg="#0084ff",
                fg="white",
                font=font,
                command = lambda i=i:showTip(i))
            tipButton.pack()

showTips()

quizTab = ttk.Frame(menu)
menu.add(quizTab, text = "Викторина")

menu.pack(expand=1, fill="both")


currentQuiz = False

quizButtons = []
quizAnswers = []

def clearQuizTab():
    global quizButtons, quizAnswers
    quizAnswers = []
    quizButtons = []
    for quiz in quizes:
        quiz.currentQuestion = 0
    for widget in quizTab.winfo_children():
        widget.destroy()

def showQuizes():
    clearQuizTab()
    i = 0
    for quiz in quizes:
        quizButton = tkinter.Button(quizTab, text=f"{quiz.title} ({quiz.score}/{len(quiz.chapters)})", command=lambda i=i: showQuiz(i), bg="#0084ff", fg="white", width=60)
        if quiz.disabled:
            quizButton["state"] = DISABLED
        quizButtons.append(quizButton)
        quizButton.pack()
        i += 1

showQuizes()


quizText = False

def nextQuestion(ans):
    global quizText
    if ans == quizes[currentQuiz].getCurrentQuestion()["correct"]: 
        quizes[currentQuiz].score +=1
    if quizes[currentQuiz].currentQuestion != len(quizes[currentQuiz].chapters) - 1:
        quizes[currentQuiz].currentQuestion += 1
        quizText.configure(text=quizes[currentQuiz].getCurrentQuestion()["question"])
        for i in range(4):
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
    quizes[i].score = 0
    for i in range(4):
        quizAnswer = tkinter.Button(quizTab, text=quizes[currentQuiz].getCurrentQuestion()["answers"][i], command=lambda ans=i: nextQuestion(ans), width= 90, bg="#0084ff", fg="white", wraplength = 500)
        quizAnswer.pack()
        quizAnswers.append(quizAnswer)
    


window.mainloop()