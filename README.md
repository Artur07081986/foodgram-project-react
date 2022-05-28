
# Сайт с рецептами
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat-square&logo=GitHub%20actions)](https://github.com/features/actions)
[![Yandex.Cloud](https://img.shields.io/badge/-Yandex.Cloud-464646?style=flat-square&logo=Yandex.Cloud)](https://cloud.yandex.ru/)
[![Django-app workflow](https://github.com/Artur07081986/foodgram-project-react/actions/workflows/main.yml/badge.svg)](https://github.com/Artur07081986/foodgram-project-react/actions/workflows/main.yml/badge.svg)

## Описание:

«Продуктовый помощник»
На этом сервисе пользователи смогут публиковать рецепты, подписываться на публикации других пользователей, 
добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, 
необходимых для приготовления одного или нескольких выбранных блюд.

#### Сайт доступен по адресу: http://food-gram.ddns.net/
#### Админка: http://food-gram.ddns.net/admin/


## Пользовательские роли
| Функционал                                                                                                                | Неавторизованные пользователи |  Авторизованные пользователи | Администратор  |
|:--------------------------------------------------------------------------------------------------------------------------|:---------:|:---------:|:---------:|
| Доступна главная страница.                                                                                                | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
| Доступна и работает форма авторизации                                                                                     | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
| Доступна страница отдельного рецепта.                                                                                     | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
| Доступна и работает форма регистрации.                                                                                    | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
| Доступна страница «Мои подписки»                                                                                          | :x: | :heavy_check_mark: | :heavy_check_mark: |
| Можно подписаться и отписаться на странице рецепта                                                                        | :x: | :heavy_check_mark: | :heavy_check_mark: |
| Можно подписаться и отписаться на странице автора                                                                         | :x: | :heavy_check_mark: | :heavy_check_mark: |
| При подписке рецепты автора добавляются на страницу «Мои подписки» и удаляются оттуда при отказе от подписки.             | :x: | :heavy_check_mark: | :heavy_check_mark: |
| Доступна страница «Избранное»                                                                                             | :x: | :heavy_check_mark: | :heavy_check_mark: |
| На странице рецепта есть возможность добавить рецепт в список избранного и удалить его оттуда                             | :x: | :heavy_check_mark: | :heavy_check_mark: |
| На любой странице со списком рецептов есть возможность добавить рецепт в список избранного и удалить его оттуда           | :x: | :heavy_check_mark: | :heavy_check_mark: |
| Доступна страница «Список покупок»                                                                                        | :x: | :heavy_check_mark: | :heavy_check_mark: |
| На странице рецепта есть возможность добавить рецепт в список покупок и удалить его оттуда                                | :x: | :heavy_check_mark: | :heavy_check_mark: |
| На любой странице со списком рецептов есть возможность добавить рецепт в список покупок и удалить его оттуда              | :x: | :heavy_check_mark: | :heavy_check_mark: |
| Есть возможность выгрузить файл (.txt) с перечнем и количеством необходимых ингредиентов для рецептов из «Списка покупок» | :x: | :heavy_check_mark: | :heavy_check_mark: |
| Ингредиенты в выгружаемом списке не повторяются, корректно подсчитывается общее количество для каждого ингредиента        | :x: | :heavy_check_mark: | :heavy_check_mark: |
| Доступна страница «Создать рецепт»                                                                                        | :x: | :heavy_check_mark: | :heavy_check_mark: |
| Есть возможность опубликовать свой рецепт                                                                                 | :x: | :heavy_check_mark: | :heavy_check_mark: |
| Есть возможность отредактировать и сохранить изменения в своём рецепте                                                    | :x: | :heavy_check_mark: | :heavy_check_mark: |
| Есть возможность удалить свой рецепт                                                                                      | :x: | :heavy_check_mark: | :heavy_check_mark: |
| Доступна и работает форма изменения пароля                                                                                | :x: | :heavy_check_mark: | :heavy_check_mark: |
| Доступна возможность выйти из системы (разлогиниться)                                                                     | :x: | :heavy_check_mark: | :heavy_check_mark: |
| Доступна и работает система восстановления пароля.                                                                        | :x: | :heavy_check_mark: | :heavy_check_mark: |
| Изменять пароль любого пользователя.                                                                                      | :x: | :x: | :heavy_check_mark: |
| Создавать/блокировать/удалять аккаунты пользователей.                                                                     | :x: | :x: | :heavy_check_mark: |
| Редактировать/удалять любые рецепты.                                                                                      | :x: | :x: | :heavy_check_mark: |
| Добавлять/удалять/редактировать ингредиенты.                                                                              | :x: | :x: | :heavy_check_mark: |
| Добавлять/удалять/редактировать теги.                                                                                     | :x: | :x: | :heavy_check_mark: |



## Администратор и админ-зона
:one: Все модели выведены в админ-зону с возможностью редактирования и удаление записей.  
:two: Для модели пользователей включена фильтрация списка по имени и email.  
:three: Для модели рецептов включена фильтрация по автору, названию рецепта, тегам.  
:four: На админ-странице рецепта отображается общее число добавлений этого рецепта в избранное.  
:five: Для модели ингредиентов включена фильтрация по названию.  

## Создание пользователя администратором
Пользователя может создать администратор — через админ-зону сайта или через POST-запрос на специальный эндпоинт api/users/ (описание полей 
запроса для этого случая — в документации).  Далее пользователь отправляет POST-запрос с параметрами email и password на эндпоинт /api/auth/token/, 
в ответе на запрос ему приходит token, как и при самостоятельной регистрации.

## Запуск проекта

- Клонировать репозиторий GitHub (не забываем создать виртуальное окружение и установить зависимости):
[https://github.com/Artur07081986/foodgram-project-react.git](https://github.com/Artur07081986/foodgram-project-react.git)

- Создать файл .env в папке проекта:
```
EMAIL_HOST_USER=user@yandex.ru
SECRET_KEY=p&l%385148kl9(vs
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
ALLOWED_HOSTS='*'
```

- в Docker cоздаем образ :

```
docker build -t foodgram .
```
- Собираем контейнеры:
```
docker-compose up -d
```
- В результате должны быть собрано три контейнера, при введении следующей команды получаем список запущенных контейнеров:  
```
docker-compose ps
```  

- Сделать миграции, создать суперпользователя и собрать статику:
```
docker-compose exec backend python manage.py makemigrations
docker-compose exec backend python manage.py migrate
docker-compose exec backend python manage.py createsuperuser
docker-compose exec backend python manage.py collectstatic --no-input 
docker-compose exec backend python manage.py shell 
>>> exec(open("/app/backend/data/filldb.py").read())
>>> quit()
```


### Автор проекта:
_Артур Габидуллин_  
**email:** _ursus110@ya.ru_  
