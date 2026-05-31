# Документация API News Portal

## Базовый URL

    http://127.0.0.1:8000/api/

## Аутентификация

Получение токена:

**POST** `/api/token/`

Параметры:

``` json
{
  "username": "your_username",
  "password": "your_password"
}
```

Ответ:

``` json
{
  "token": "xxxxxxxxxxxxxxxxxxxxxxxx"
}
```

Для авторизованных запросов:

``` http
Authorization: Token xxxxxxxxxxxxxxxxxxxxxxxx
```

------------------------------------------------------------------------

## Пользователи

### Получить список пользователей

**GET** `/api/users/`

### Получить пользователя по ID

**GET** `/api/users/{id}/`

### Создать пользователя

**POST** `/api/users/`

Пример:

``` json
{
  "username": "ivan",
  "first_name": "Иван",
  "last_name": "Иванов",
  "email": "ivan@example.com",
  "password": "12345678"
}
```

### Изменить пользователя

**PUT** `/api/users/{id}/`

или

**PATCH** `/api/users/{id}/`

### Удалить пользователя

**DELETE** `/api/users/{id}/`

------------------------------------------------------------------------

## Новости

### Получить список новостей

**GET** `/api/news/`

### Получить новость по ID

**GET** `/api/news/{id}/`

### Создать новость

**POST** `/api/news/`

Пример:

``` json
{
  "title": "Заголовок",
  "summary": "Краткое описание",
  "content": "Текст новости"
}
```

### Изменить новость

**PUT** `/api/news/{id}/`

или

**PATCH** `/api/news/{id}/`

### Удалить новость

**DELETE** `/api/news/{id}/`

------------------------------------------------------------------------

## Используемые маршруты

-   `/api/news/`
-   `/api/users/`
-   `/api/token/`

Маршруты зарегистрированы через `DefaultRouter`:

``` python
router.register(r'news', NewsViewSet, basename='api-news')
router.register(r'users', UserViewSet, basename='api-users')
```
