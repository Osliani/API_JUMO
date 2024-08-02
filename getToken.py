from dotenv import load_dotenv
import requests, os

load_dotenv()

def get_oauth_token():
    key = os.getenv('PUBLIC_ODOO_CLIENT_ID')
    secret = os.getenv('PUBLIC_ODOO_CLIENT_SECRET')

    url = f"{os.getenv('PUBLIC_ODOO_URL')}{os.getenv('PUBLIC_TOKEN_PATH')}"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    body = f'grant_type=client_credentials&client_id={key}&client_secret={secret}'

    response = requests.post(url, headers=headers, data=body)

    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        print(response.json())
        return None

    data = response.json()

    return data


def get_oauth_token_dev():
    key = os.getenv('PUBLIC_ODOO_CLIENT_ID_DEV')
    secret = os.getenv('PUBLIC_ODOO_CLIENT_SECRET_DEV')

    url = f"{os.getenv('PUBLIC_ODOO_URL_DEV')}{os.getenv('PUBLIC_TOKEN_PATH')}"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    body = f'grant_type=client_credentials&client_id={key}&client_secret={secret}'

    response = requests.post(url, headers=headers, data=body)

    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        print(response.json())
        return None

    data = response.json()

    return data


if __name__ == "__main__":
    token = get_oauth_token()
    print(token)
