Для запуска разархивируйте файл и вызовите в консоли команду
pip install -r requirements.txt
Проект уже включает в себя базу данных с пользователями. У некоторых из них уже (!) есть статистика и сыгранные игры. 
Игра запускается из файла main.py. Рекомендуется не менять относительное расположение файлов в проекте. 
ТЗ: создать приложение-игру Виселица с различными уровнями сложности и возможностью регистрации, логина юзера.
Можно играть также без логина, как гость.
Гость не имеет права разлогиниться и удалять профиль, залогиненный юзер имеет. И наоборот, гость может залогиниться и создать аккаунт, юзер нет.
Игра доступна на трех уровнях сложности, за каждый из которых начисляется свое количество опыта. 
У юзера доступна его статистика по играм, известен его текущий уровень, а также отображается прогресс-бар перехода на следующий уровень.
После выбора сложности начинается игра. Слово выбирается из бд по соответствующей сложности. Одно слово никогда не попадается юзеру дважды.
В процессе отображается количество букв в слове, все нажатые буквы окрашиваются в зеленый/красный в зависимости от наличия их в слове.
В игре доступна подсказка 1 раз за игру. Ошибиться можно не более 10 раз. После каждой ошибки изменяется картинка состояния.
После завершения игры конкретное слово добавляется в стастистику пользователю, появляется статистика по уровню.
Есть возможность вернуться в главное меню.
В конце каждой игры (по ее успешному/неуспешному завершению) слово и результат добавляются к юзеру. Статистика игры и юзера меняются.
По поводу реализации:
Из интересного - файл Logic.py содержит объект логики. Здесь находится вся логика игры, не связанная с отрисовкой.
В файле main.py собрана конфигурация рабочего приложения, включая глобальную переменную user. Автор проекта проконсультировался с методистом
и решил не создавать отдельную сущность-синглтон для этого, а хранить как глобальную переменную, к ней обращаются несколько объектов из классов, 
прописанных в мейне.
Utils.py - отдельный модуль, в котором находится вся работа с базой данных. 
users.sqlite - соответствующая база данных.
