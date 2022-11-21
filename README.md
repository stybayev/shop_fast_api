<h2 align="center">API test_project YOKO</h2>


**Ссылки**:
- [Telegram](https://t.me/ddos_att)
- [Схема базы данных](https://drive.google.com/file/d/1e1Im1R0mAa6WT83LeZyf2n8rYgrAuUY0/view?usp=sharing)

### Описание проекта:
API для мобильного приложения, в котором полевой сотрудник заказчика будет выполнять визиты в магазины.


### Инструменты разработки

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

##### 3) Запуск приложений Docker со всеми контейнерами. В Dockerfile используются многоэтапные сборки для запуска тестовых стадий перед сборкой. Если линтинг или тестирование завершатся неудачно, сборка завершится ошибкой.

    sudo docker-compose -f docker-compose.yml up -d

##### 4) Применить миграции с alembic в БД :

    docker-compose run app alembic upgrade head
    
##### 5) Восстановить БД тестовыми данными из файла dump_test_yoko.sql (который лежит в корне проекта). 
    cat dump_test_yoko.sql | docker exec -i your-db-container psql -U postgres
##### С первого раза БД может не полностью восстановиться, попробуйте применить команду еще раз.

## Интерфейс приложения

##### 1) Документацию API в Swaggger с описанием всех роутов можно посмотреть по ссылке 

    http://0.0.0.0:8000/docs
![](https://github.com/stybayev/test_yoko/blob/main/images/swagger.png?raw=true)

##### 2) Интерфейс GraphQL(Strawberry) можно посмотреть по ссылке
    
    http://0.0.0.0:8000/graphql
![](https://github.com/stybayev/test_yoko/blob/main/images/graphql.png?raw=true)

##### 3) Также можете посмотреть структуру БД через Интерфейс pgAdmin4
##### Сначала перейдите по ссылке
    
    http://0.0.0.0:5050

##### Введите логин (admin@admin.com) и пароль (admin)
![](https://github.com/stybayev/test_yoko/blob/main/images/Screenshot%20at%20Nov%2022%2000-01-34.png?raw=true)

##### Нажмите на Add new server
![](https://github.com/stybayev/test_yoko/blob/main/images/add_new_server.png?raw=true)

##### Во вкладке Generel введите Hostmame/addres (db)
![](https://github.com/stybayev/test_yoko/blob/main/images/general.png?raw=true)

##### Во вкладке Connection введите username (postgres) и password (password), а также Hostmame/addres (db)
![](https://github.com/stybayev/test_yoko/blob/main/images/connection.png?raw=true)

##### После чего вы попадете в интерйес pgAdmin, где можете посмотреть и управлять всей БД
![](https://github.com/stybayev/test_yoko/blob/main/images/tables.png?raw=true)

Copyright (c) 2022-present, stybayev - Doskhan Stybayev
