import requests


class Auth:

    def __init__(self, base_url, token):
        self.base_url = base_url
        self.headers = {'Accept': 'application/json',
                        'Authorization': f'OAuth {token}'
                        }

    def get_file(self):
        return requests.get(self.base_url + "/files",
                            headers=self.headers)

    def get_dir(self, path='disk:/'):
        return requests.get(self.base_url,
                            params={"path": f'{path}'},
                            headers=self.headers)
