# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método etático (❌self, ❌cls)
class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None        
        self.password = None

    def set_user(self, user): # setter
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def create_user_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection
    
    @staticmethod
    def log(msg):
        return f'Log: {msg}'

c1 = Connection.create_user_auth('erick', '1234')
# c1.set_user('erick')
# c1.set_password('123')
print(Connection.log('Logging in...'))
print(c1.user)
print(c1.password)

try:
    c1 = Connection.create_user_auth('erick', '1234')
    print(Connection.log('Logging in...'))
except:
    print(Connection.log('Logging FAILED!'))
