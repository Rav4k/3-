import requests

class NewsAPIClient:
    def __init__(self, base_url, token=None):
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        if token:
            self.session.headers.update({'Authorization': f'Token {token}'})

    def register(self, username, email, password):
        url = f"{self.base_url}/api/users/"
        data = {'username': username, 'email': email, 'password': password}
        response = self.session.post(url, json=data)
        return response.json()

    def login(self, username, password):
        url = f"{self.base_url}/api/token/"
        data = {'username': username, 'password': password}
        response = self.session.post(url, json=data)
        if response.status_code == 200:
            token = response.json().get('token')
            self.session.headers.update({'Authorization': f'Token {token}'})
        return response.json()

    def create_news(self, title, content, summary=''):
        url = f"{self.base_url}/api/news/"
        data = {'title': title, 'content': content, 'summary': summary}
        response = self.session.post(url, json=data)
        return response.json()

    def get_news(self, news_id=None, **params):
        if news_id:
            url = f"{self.base_url}/api/news/{news_id}/"
        else:
            url = f"{self.base_url}/api/news/"
        response = self.session.get(url, params=params)
        return response.json()

    def update_news(self, news_id, **kwargs):
        url = f"{self.base_url}/api/news/{news_id}/"
        response = self.session.patch(url, json=kwargs)
        return response.json()

    def delete_news(self, news_id):
        url = f"{self.base_url}/api/news/{news_id}/"
        response = self.session.delete(url)
        return response.status_code