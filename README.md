# Django Task Manager

Этот проект предоставляет функционал для управления задачами с возможностью регистрации, авторизации пользователей и взаимодействия с задачами.

## Описание

API включает в себя несколько ключевых функций:

- Регистрация и аутентификация пользователей через API.
- Возможность создания, обновления и удаления задач.
- Возможность фильтрации и поиска задач.
- Простой способ взаимодействия с задачами через RESTful API.

## Стек технологий

- Python
- Django
- Django REST Framework

## Установка

### 1. Клонирование репозитория

```
git clone git@github.com:TeenCreek/todo.git
```

### 2. Создание виртуального окружения

```
python -m venv venv
source venv/bin/activate  # для macOS/Linux
venv\Scripts\activate  # для Windows
```

### 3. Установка зависимостей

```
pip install -r requirements.txt
```

### 4. Применение миграций

```
python manage.py migrate
```

### 6. Создание суперпользователя

```
python manage.py createsuperuser
```

### 7. Запуск сервера

```
python manage.py runserver
```

## API Endpoints

Полный список доступных эндпоинтов: `GET /swagger/`

### 1. Регистрация пользователя

```
POST /api/v1/users/

{
    "username": "new_user",
    "email": "newuser@example.com",
    "password": "securepassword"
}
```

### 2. Просмотр всех задач пользователя

```
GET /api/v1/tasks/

[
    {
        "id": 1,
        "title": "My First Task",
        "description": "Task description",
        "is_completed": false,
        "created_at": "2024-12-09T12:00:00Z",
        "updated_at": "2024-12-09T12:00:00Z",
        "author": "new_user"
    }
]
```
