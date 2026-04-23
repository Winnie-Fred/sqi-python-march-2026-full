import requests

def fetch_user_data():
    url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(url)

    user_data = response.json()

    return [user_info["username"] for user_info in user_data]
