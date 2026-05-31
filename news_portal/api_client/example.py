from .client import NewsAPIClient

def main():
    client = NewsAPIClient('http://127.0.0.1:8000')  # локально
    # Регистрация
    reg = client.register('testuser', 'test@example.com', 'ComplexPass123')
    print('Register:', reg)
    # Логин
    login = client.login('testuser', 'ComplexPass123')
    print('Login:', login)
    # Создание новости
    news = client.create_news('Мой заголовок', 'Этот текст содержит более пятидесяти символов для валидации.', summary='Кратко')
    print('Created:', news)
    # Получение списка
    all_news = client.get_news()
    print('All news:', all_news)
    # Получение одной новости
    if 'id' in news:
        one = client.get_news(news['id'])
        print('One news:', one)
        # Обновление
        updated = client.update_news(news['id'], title='Новый заголовок')
        print('Updated:', updated)
        # Удаление
        status = client.delete_news(news['id'])
        print('Delete status:', status)

if __name__ == '__main__':
    main()