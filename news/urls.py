from django.urls import path
# Импортируем созданное нами представление
from .views import Postlist, PostDetail, SearchNews

urlpatterns = [
   # path — означает путь.

   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   path('', Postlist.as_view()),
   # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
   # int — указывает на то, что принимаются только целочисленные значения
   path('<int:pk>', PostDetail.as_view()),
   path('search', SearchNews.as_view()), # SearchNews - название класса из views.py

]