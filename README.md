# foodgram-project
foodgram-project
### Описание проекта

Это онлайн-сервис, где пользователи смогут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.


### Что могут делать неавторизованные пользователи
- Создать аккаунт.
- Просматривать рецепты на главной.
- Просматривать отдельные страницы рецептов.
- Просматривать страницы пользователей.
- Фильтровать рецепты по тегам.

### Что могут делать авторизованные пользователи
- Входить в систему под своим логином и паролем.
- Выходить из системы (разлогиниваться).
- Восстанавливать свой пароль.
- Менять свой пароль.
- Создавать/редактировать/удалять собственные рецепты
- Просматривать рецепты на главной.
- Просматривать страницы пользователей.
- Просматривать отдельные страницы рецептов.
- Фильтровать рецепты по тегам.
- Работать с персональным списком избранного: добавлять/удалять чужие рецепты, просматривать свою страницу избранных рецептов.
- Работать с персональным списком покупок: добавлять/удалять любые рецепты, выгружать файл со количеством необходимых ингредиентов для рецептов из списка покупок.
- Подписываться на публикации авторов рецептов и отменять подписку, просматривать свою страницу подписок.

### Установка

#### Установка docker и docker-compose:

Используйте официальную [инструкцию](https://docs.docker.com/engine/install/).

#### Создайте файл .env с данным содержимым:
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```
#### Запуск приложения:
```
docker-compose up
```
#### Отсановка приложения:
```
docker-compose down
```

### Использование

#### Применение миграции:
```
docker-compose run web python manage.py migrate
```
#### Инициализация стартовых данных:
```
docker-compose run web python manage.py loaddata fixtures/fixtures.json
```
#### Создание суперпользователя Django:
```
docker-compose run web python manage.py createsuperuser
```


#### Страница проекта
```
http://http://130.193.35.12/
```



#### Страница администрирования
```
http://http://130.193.35.12/admin/
```

![example workflow name](https://github.com/maxjazz/foodgram-project/workflows/foodgram/badge.svg)
