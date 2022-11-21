<h2 align="center">API test_project YOKO</h2>


**Ссылки**:
- [Telegram](https://t.me/ddos_att)

### Описание проекта:
API для мобильного приложения, в котором полевой сотрудник заказчика будет выполнять визиты в магазины.


### Инструменты разработки

**Стек:**

- VM: Doker
- PL: Python
- Packaging/Dependency management: Poetry
- Freamework: FastApi + GraphQL(Strawberry)
- DB: Postgresql
- Alembic 


## Разработка

##### 1) Сделать форк репозитория и поставить звездочку)

##### 2) Клонировать репозиторий

    git clone https://github.com/stybayev/test_yoko

##### 3) Запуск приложений Docker со всеми контейнерами

    sudo docker-compose -f docker-compose.yml up -d

##### 4) Применить миграции с alembic в БД :

    docker-compose run app alembic upgrade head
    
##### 5) Восстановить БД тестовыми данными из файла dump_test_yoko.sql (который лежит в корне проекта)

    cat dump_test_yoko.sql | docker exec -i your-db-container psql -U postgres

## Интерфейс приложения

##### 1) Документацию API в Swaggger с описанием всех роутов можно посмотреть по ссылке 

    http://0.0.0.0:8000/docs

##### 2) Интерфейс GraphQL(Strawberry) можно посмотреть по ссылке
    
    http://0.0.0.0:8000/graphql

##### 3) Также можете посмотреть структуру БД через Интерфейс pgAdmin4
##### Сначала перейдите по ссылке
    
    http://0.0.0.0:8000/graphql

##### Введите логин (admin@admin.com) и пароль (admin)
    
![Image alt](https://prnt.sc/boCrU3K7twQm!)