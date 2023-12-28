import configparser


config = configparser.RawConfigParser()
config.read(".\\configuration\\config.ini")


class Configparser:

        @staticmethod
        def get_url():
            url = config.get('common_data','url')
            return url

        @staticmethod
        def get_username():
            username = config.get('common_data','username')
            return username

        @staticmethod
        def get_password():
            password = config.get('common_data','password')
            return password
