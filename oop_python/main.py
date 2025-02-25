from Users import *
from Menus import *


def main():
    print("Добро пожаловать в музыкальный сервис!")
    while True:
        user = Authenticate.authenticate()
        if user:
            if user['role'] == 'user':
                Menu.user_menu(user)
            elif user['role'] == 'admin':
                Menu.admin_menu(user)
main()
