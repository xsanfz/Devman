from idlelib.replace import replace
from email.message import EmailMessage
my_name = "Сергей"
friend_name = "Дмитрий"
website = "https://dvmn.org/profession-ref-program/sergey.myamin/TK540/"
letter = EmailMessage()
letter['From'] = 'rewaqz1@yandex.ru'
letter['To'] = 'Am1dok@yandex.ru'
letter['Subject'] = 'Приглашение!'




my_str = ("""Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.""")
my_str = my_str.replace('%friend_name%', friend_name)

my_str = my_str.replace('%my_name%',my_name)

my_str = my_str.replace('%website%', website)

my_str = my_str.replace('%friend_name%', friend_name)

letter.set_content(my_str, subtype='plain', charset='utf-8')





my_str = my_str.replace('%website%', website)

my_str = my_str.replace('%friend_name%', friend_name)

my_str = my_str.replace('%my_name%',my_name)

print(letter.set_content)