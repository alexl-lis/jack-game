class Story:
    chapters = [
        {
            "text" : "Привет, меня зовут Джек. Я буду помогать тебе проходить игру!"
            "Начнем. Давай для начала повторим тему"
            "Двоичная система счисления",
            "imageUrl" : "main.png"
        },
        {
            "text" : "Двоичная система — это один из видов позиционных систем счисления. Основание данной системы равно двум, то есть используется только два символа для записи чисел.",
            "imageUrl" : "run.png"
        },
        {
            "text" : "Основанием двоичной системы счисления является число 2. В двоичном коде могут содержаться только два символа: 0 и 1. То есть число 12 не является числом из двоичной системы счисления.Пример числовой последовательности:0,1,10,11,100,101,110,111 и т.д.",
            "imageUrl" : "run.png" 
        },
        {
            "text" : "Двоичная система счисления используется для кодирования различных символов в компьютере",
            "imageUrl" : "main.png"
        },
        {
            "text" : "Теперь перейди во вкладку 'Викторина' и пройди Викторину по теме 'Двоичная система счисления' для того, чтобы продвинуться дальше. В случае возникновения трудностей, перейди на карту и найди подсказки!",
            "imageUrl" : "run.png",
            "enable" : 0
        },
        {
            "text" : "Перейдем к следующей теме под названием 'Алгебра логики'"
            "Начнем. Алгебра логки - это раздел математики, изучающий высказывания, рассматриваемые со стороны их логических значений (истинности или ложности) и логических операций над ними."
            "Двоичная система счисления",
            "imageUrl" : "main.png"
        },
        {
            "text" : "Существует логическое умножение, сложение, а также отрицание",
            "imageUrl" : "run.png"
        },
        {
            "text" : "Логическим отрицанием называют логическую операцию, имеющую название 'Инверсия'. Логическим умножение - 'Конъюнкция', а логическое сложение называют 'Дизъюнкция' ",
            "imageUrl" : "run.png" 
        },
        {
            "text" : "Это три основных логических операции и их понятия. Теперь для того, чтобы усвоить прочитанное перейди во вкладу 'Викторины' и пройди тест. В случае возникновения трудностей перейди на карту и собери подсказки!",
            "imageUrl" : "main.png"
        },
        {
            "text" : "Теперь перейди во вкладку 'Викторина' и пройди Викторину по теме 'Двоичная система счисления' для того, чтобы продвинуться дальше. В случае возникновения трудностей, перейди на карту и найди подсказки!",
            "imageUrl" : "run.png",
            "enable" : 1
        },
        {
            "text" : "Перейдем к следующей теме под названием 'Информация'"
            "Начнем. Информация - это сведения об объектах окружающей среды, их параметрах, свойствах и состоянии, которые уменьшают имеющуюся о них степень неопределенности, неполно-ты знаний.",
            "imageUrl" : "main.png"
        },
        {
            "text" : "Кодированием информации можно назвать преобразование информации из одной формы представления в другую, другими словами, это операция преобразования знаков или групп знаков одной знаковой системы в знаки или группы знаков другой знаковой системы.",
            "imageUrl" : "run.png"
        },
        {
            "text" : "Чтобы принимать информацию в других видах, существует Обработка информации. Это  вся совокупность операций (сбор, ввод, запись, преобразование, считывание, хранение, уничтожение, регистрация),",
            "imageUrl" : "run.png" 
        },
        {
            "text" : "Информация, которая нужна в данный момент является актуальной",
            "imageUrl" : "main.png"
        },
        {
            "text" : "Теперь перейди во вкладку 'Викторина' и пройди Викторину по теме 'Информация' для того, чтобы продвинуться дальше. В случае возникновения трудностей, перейди на карту и найди подсказки!",
            "imageUrl" : "run.png",
            "enable" : 2
        },
        {
            "text" : "Последнее, о чем мы вспомним, это Excel"
            "Начнем. Основная функция электронных таблиц - выполнение расчета по формулам",
            "imageUrl" : "main.png"
        },
        {
            "text" : "Электронная таблица позволяет представлять данные в виде диаграмм, графиков.",
            "imageUrl" : "run.png"
        },
        {
            "text" : "Одним из основных элементов электронной таблицы являются ячейки.",
            "imageUrl" : "run.png" 
        },
        {
            "text" : "Примерами электронных таблиц можут служить программы, такие как Excel, Quattropro и Superkalk.",
            "imageUrl" : "main.png"
        },
        {
            "text" : "Теперь перейди во вкладку 'Викторина' и пройди Викторину по теме 'Excel' для того, чтобы завершить игру . В случае возникновения трудностей, перейди на карту и найди подсказки!",
            "imageUrl" : "run.png",
            "enable" : 3
        },
        {
            "text" : "Поздравляю, Вы прошли игру!",
            "imageUrl" : "lie.png"
        }

        
    ]
    currentChapter = 0

    def getCurrentChapter(self):
        return self.chapters[self.currentChapter]
