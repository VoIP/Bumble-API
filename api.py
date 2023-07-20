import requests


class Bumble:
    def __init__(self):
        self.api_key = 'API_KEY'  # GIVEN AT PURCHASE
        self.endpoint = 'The given Endpoint'  # GIVEN AT PURCHASE
        self.provider_choice_for_number = '5sim'  # CHANGE PROVIDER
        self.five_sim_api = 'API_KEY FOR 5SIM'

    def create_account(self, name, picture_path, age, biography):
        return requests.post(self.endpoint + '/create',
                             json={'api_key': self.api_key, 'number_provider': self.provider_choice_for_number,
                                   'api_key_number': self.five_sim_api,
                                   'picture_path': picture_path, 'name': name, 'age': age,
                                   'proxy': 'http://user:pass@ip:port',
                                   'location': 'latitude longitude', 'gender': 'female or male',
                                   'target': 'men or women',
                                   'email_login': 'email:password', 'biography': biography}).json()['cookies']

    def login(self, phone_number):
        return requests.post(self.endpoint + '/create', json={'api_key': self.api_key, 'phone_number': phone_number,
                                                              'number_provider': self.provider_choice_for_number,
                                                              'api_key_number': self.five_sim_api,
                                                              'proxy': 'http://user:pass@ip:port'}).json()['cookies']

    def swipe(self, cookies, proxies):
        user_id = requests.get(self.endpoint + '/current_swipe', cookies=cookies, proxies=proxies).json()['user_id']
        return requests.post(self.endpoint + '/swipe', cookies=cookies,
                             json={'api_key': self.api_key, 'user_id': user_id, 'like': 'True or False',
                                   'proxy': 'http://user:pass@ip:port'}).json()['status']

    def message(self, cookies, message):
        user_id = \
            requests.get(self.endpoint + '/most_recent', cookies=cookies, headers={'api_key': self.api_key}).json()[
                'user_id']
        return requests.post(self.endpoint + '/message', cookies=cookies,
                             json={'api_key': self.api_key, 'user_id': user_id, 'message': message,
                                   'proxy': 'http://user:pass@ip:port'}).json()['status']

    def update_biography(self, cookies, biography):
        return requests.post(self.endpoint + '/edit_profile', cookies=cookies,
                             json={'api_key': self.api_key, 'biography': biography,
                                   'proxy': 'http://user:pass@ip:port'}).json()['status']

    def verify_account(self, cookies, picture):
        return requests.post(self.endpoint + '/verification', cookies=cookies,
                             json={'api_key': self.api_key, 'verification_picture': picture,
                                   'proxy': 'http://user:pass@ip:port'}).json()['status']
