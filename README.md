Чек лист разработки проекта
 «Доска объявлений»:

1.	Создать проект. 
2.	Подключить статику. 
3.	Подключить шаблоны. 
4.	Создать модели: 
a.	Модель «объявление»;
b.	Модель «отклик».
5.	Создать путь хранения файлов и прописать пути к их хранению. 
6.	Создать шаблон страницы для визуализации. 
7.	Создать представления:
a.	Главная страница «список объявлений».
b.	Детали объявления.
c.	Создать объявление.
d.	Редактировать объявление.
e.	Удалить объявление.
f.	Отображение откликов в объявлении
g.	Создание откликов
h.	Удаление откликов.
i.	Принятие откликов.
8.	Настроить авторизацию.
9.	Настроить рассылки.


КРИТЕРИИ ОЦЕНИВАНИЯ

•	Модели спроектированы корректно, нет ошибок в связях, лишних моделей и полей — 3 балла
•	Представления написаны в соответствии с логикой техзадания, модели используются эффективно — 5 баллов
•	Авторизация и регистрация работают корректно, код приходит на e-mail — 3 балла
•	Письма отправляются по правильным событиям — 5 баллов

Техническое задание:
	
	Нам необходимо разработать интернет-ресурс для фанатского сервера одной известной MMORPG — что-то вроде доски объявлений. Пользователи нашего ресурса должны иметь возможность зарегистрироваться в нём по e-mail, получив письмо с кодом подтверждения регистрации. После регистрации им становится доступно создание и редактирование объявлений. Объявления состоят из заголовка и текста, внутри которого могут быть картинки, встроенные видео и другой контент. Пользователи могут отправлять отклики на объявления других пользователей, состоящие из простого текста. При отправке отклика пользователь должен получить e-mail с оповещением о нём. Также пользователю должна быть доступна приватная страница с откликами на его объявления, внутри которой он может фильтровать отклики по объявлениям, удалять их и принимать (при принятии отклика пользователю, оставившему отклик, также должно прийти уведомление). Кроме того, пользователь обязательно должен определить объявление в одну из следующих категорий: Танки, Хилы, ДД, Торговцы, Гилдмастеры, Квестгиверы, Кузнецы, Кожевники, Зельевары, Мастера заклинаний.
	Также мы бы хотели иметь возможность отправлять пользователям новостные рассылки.
Разбор ТЗ:

1.	регистрация по e-mail с подтверждением кодом
2.	создание и редактирование объявлений после регистрации.
3.	состав объявления
•	заголовок
•	текст внутри
•	картинки, видео, другой контент
4.	пользователи могут оставлять отклики на объявления (только текст)
5.	сообщение на мыло об отклике
6.	своя страница с откликами с фильтром, может удалять и принимать отклики (с уведомлением)
7.	категории объявлений:
•	Танки,
•	Хилы, 
•	ДД, 
•	Торговцы, 
•	Гилдмастеры, 
•	Квестгиверы, 
•	Кузнецы, 
•	Кожевники, 
•	Зельевары, 
•	Мастера заклинаний

8.	новостные рассылки пользователям.

