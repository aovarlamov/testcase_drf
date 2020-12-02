# API для системы опросов пользователей
Цель спроектировать и разработать API для системы опросов пользователей (Test Case ООО Фабрика Решений)

## Функционал для администратора системы:

* авторизация в системе (регистрация не нужна)
* добавление/изменение/удаление опросов. Атрибуты опроса: название, дата старта, дата окончания, описание. После создания поле "дата старта" у опроса менять нельзя
* добавление/изменение/удаление вопросов в опросе. Атрибуты вопросов: текст вопроса, тип вопроса (ответ текстом, ответ с выбором одного варианта, ответ с выбором нескольких вариантов)

## Функционал для пользователей системы:

* получение списка активных опросов
* прохождение опроса: опросы можно проходить анонимно, в качестве идентификатора пользователя в API передаётся числовой ID, по которому сохраняются ответы пользователя на вопросы; один пользователь может участвовать в любом количестве опросов
* получение пройденных пользователем опросов с детализацией по ответам (что выбрано) по ID уникальному пользователя

## Технологии
  * python3.8
  * Django2.2.10
  * djangorestframework3.12.2

## Установка
  ```
  git clone https://github.com/aovarlamov/testcase_drf.git testcase_drf
  cd testcase_drf/
  pip install -r requirements.txt
  cd testcase_drf/
  python3.8 manage.py makemigrations
  python3.8 manage.py migrate
  python3.8 manage.py createsuperuser
  python3.8 manage.py runserver
  ```

## API документация

### Админ панель Django
* URL: http://localhost:8000/admin/

### Поплучить токен для входа: 
* Метод запроса: GET
* URL: http://localhost:8000/api/login/
* Переменные: 
    * username: 
    * password: 
* Пример:
```
curl --location --request GET 'http://localhost:8000/api/login/' --form 'username=%username' --form 'password=%password'
```

### Создать опрос:
* Метод запроса: POST
* URL: http://localhost:8000/api/poll/create/
* Переменные:
    * userToken: Токен пользователя
    * poll_name: Назавание опроса
    * pub_date: Дата публикации в формате YYYY-MM-DD HH:MM:SS
    * end_date: Дата окончания опроса в формате YYYY-MM-DD HH:MM:SS
    * poll_description: Описание опроса
* Пример: 
```
curl --location --request POST 'http://localhost:8000/api/poll/create/' --header 'Authorization: Token %userToken' --form 'poll_name=%poll_name' --form 'pub_date=%pub_date' --form 'end_date=%end_date --form 'poll_description=%poll_description'
```

### Обновить опрос:
* Метод запроса: PATCH
* URL: http://localhost:8000/api/poll/update/[poll_id]/
* Параметры:
    * poll_id: id опроса 
* Переменные:
    * userToken: Токен пользователя
    * poll_name: Название опроса
    * end_date: Дата окончания опроса в формате YYYY-MM-DD HH:MM:SS
    * poll_description: Описание опроса
* Пример:
```
curl --location --request PATCH 'http://localhost:8000/api/poll/update/[poll_id]/ --header 'Authorization: Token %userToken' --form 'poll_name=%poll_name' --form 'end_date=%end_date --form 'poll_description=%poll_description'
```

### Удалить опрос:
* Метод запроса: DELETE
* URL: http://localhost:8000/api/poll/delete/[poll_id]
* Параметры:
    * poll_id: id опроса 
* Переменные:
    * userToken: Токен пользователя
Пример:
```
curl --location --request DELETE 'http://localhost:8000/api/poll/delete/[poll_id]/' --header 'Authorization: Token %userToken'
```

### Просмотр всех опросов:
* Метод запроса: GET
* URL: http://localhost:8000/api/poll/view/
* Переменные:
    * userToken: Токен пользователя
* Пример:
```
curl --location --request GET 'http://localhost:8000/api/poll/view/' --header 'Authorization: Token %userToken'
```

### Просмотр активных опросов:
* Метод запроса: GET
* URL: http://localhost:8000/api/poll/view/active/
* Переменные:
    * userToken: Токен пользователя
* Пример:
```
curl --location --request GET 'http://localhost:8000/api/poll/view/active/' --header 'Authorization: Token %userToken'
```

### Создать вопрос:
* Метод запроса: POST
* URL: http://localhost:8000/api/question/create/
* Переменные:
    * userToken: Токен пользователя
    * poll: id опроса
    * question_text: Текст вопроса
    * question_type: Тип вопроса: `текс`, `несколько вариантов` or `один вариант`
* Пример:
```
curl --location --request POST 'http://localhost:8000/api/question/create/' header 'Authorization: Token %userToken' --form 'poll=%poll' --form 'question_text=%question_text' --form 'question_type=%question_type
```

### Обновить вопрос:
* Метод запроса: PATCH
* URL: http://localhost:8000/api/question/update/[question_id]/
* Параметры:
    * question_id: id вопроса
* Переменные:
    * userToken: Токен пользователя
    * poll: id опроса
    * question_text: Текст вопроса
    * question_type: Тип вопроса: `текс`, `несколько вариантов` or `один вариант`
* Пример:
```
curl --location --request PATCH 'http://localhost:8000/api/question/update/[question_id]/' header 'Authorization: Token %userToken' --form 'poll=%poll' --form 'question_text=%question_text' --form 'question_type=%question_type
```

### Удалить вопрос:
* Метод запроса: DELETE
* URL: http://localhost:8000/api/question/delete/[question_id]/
* Параметры:
    * question_id: id вопроса
* Переменные:
    * userToken: Токен пользователя
* Пример:
```
curl --location --request DELETE 'http://localhost:8000/api/question/delete/[question_id]/' header 'Authorization: Token %userToken' --form 'poll=%poll' --form 'question_text=%question_text' --form 'question_type=%question_type
```


### Создать выбор:
* Метод запроса: POST
* URL: http://localhost:8000/api/choice/create/
* Переменные:
    * userToken: Токен пользователя
    * question: id вопроса
    * choice_text: Текст выбора
* Пример:
```
curl --location --request POST 'http://localhost:8000/api/choice/create/' --header 'Authorization: Token %userToken' --form 'question=%question' --form 'choice_text=%choice_text'
```

### Обновить выбор:
* Метод запроса: PATCH
* URL: http://localhost:8000/api/choice/update/[choice_id]/
* Параметры:
    * choice_id
* Переменные:
    * userToken: Токен пользователя
    * question: id вопроса
    * choice_text: Текст выбора
* Пример:
```
curl --location --request PATCH 'http://localhost:8000/api/choice/update/[choice_id]/' --header 'Authorization: Token %userToken' --form 'question=%question' --form 'choice_text=%choice_text'
```


### Удалить выбор:
* Метод запроса: DELETE
* URL: http://localhost:8000/api/choice/delete/[choice_id]/
* Параметры:
    * choice_id
* Переменные:
    * userToken: Токен пользователя
* Пример:
```
curl --location --request DELETE 'http://localhost:8000/api/choice/delete/[choice_id]/' --header 'Authorization: Token %userToken' --form 'question=%question' --form 'choice_text=%choice_text'
```


### Создать ответ:
* Метод запроса: POST
* URL: http://localhost:8000/api/answer/create/
* Переменные:
    * userToken: Токен пользователя
    * user_id: id пользователя
    * poll: id опроса
    * question: id вопроса
    * choice: id выбора
    * answer_text: Текст ответа
* Пример:
```
curl --location --request POST 'http://localhost:8000/api/answer/create/' --header 'Authorization: Token %userToken' --form 'poll=%poll' --form 'question=%question' --form 'choice=%choice --form 'answer_text=%answer_text'
```

### Обновить ответ:
* Метод запроса: PATCH
* URL: http://localhost:8000/api/answer/update/[answer_id]/
* Параметры:
    * answer_id: id ответа
* Переменные:
    * userToken: Токен пользователя
    * user_id: id пользователя
    * poll: id опроса
    * question: id вопроса
    * choice: id выбора
    * answer_text: Текст ответа
* Пример:
```
curl --location --request PATCH 'http://localhost:8000/api/answer/update/[answer_id]' --header 'Authorization: Token %userToken' --form 'poll=%poll' --form 'question=%question' --form 'choice=%choice --form 'answer_text=%answer_text'
```

### Удалить ответ:
* Метод запроса: DELETE
* URL: http://localhost:8000/api/answer/delete/[answer_id]/
* Параметры:
    * answer_id: id ответа
* Переменные:
    * userToken: Токен пользователя
    * user_id: id пользователя
    * poll: id опроса
    * question: id вопроса
    * choice: id выбора
    * answer_text: Текст ответа
* Пример:
```
curl --location --request DELETE 'http://localhost:8000/api/answer/delete/[answer_id]' --header 'Authorization: Token %userToken' --form 'poll=%poll' --form 'question=%question' --form 'choice=%choice --form 'answer_text=%answer_text'
```

### Просмотр ответов по ID:
* Метод запроса: GET
* URL: http://localhost:8000/api/answer/view/[user_id]/
* Параметры:
    * user_id: id пользователя
* Переменные:
    * userToken: Токен пользователя
* Пример:
```
curl --location --request GET 'http://localhost:8000/api/answer/view/[user_id]' --header 'Authorization: Token %userToken'
```

  
