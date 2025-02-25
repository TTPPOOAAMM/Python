from Users import *

class Menu():
    def user_menu(user):
        while True:
            print("\n--- Меню пользователя ---")
            print("1. Просмотр доступных треков")
            print("2. Прослушивание трека")
            print("3. Просмотр истории прослушиваний")
            print("4. Сортировка и фильтрация треков")
            print("5. Обновление профиля")
            print("6. Выход")
            choice = input("Выберите действие: ")

            if choice == '1':
                User.view_tracks()
            elif choice == '2':
                User.listen_to_track(user)
            elif choice == '3':
                User.view_history(user)
            elif choice == '4':
                User.sort_and_filter_tracks()
            elif choice == '5':
                User.update_profile(user)
            elif choice == '6':
                print("Выход из системы...")
                break
            else:
                print("Некорректный выбор.")
                
    def admin_menu(admin):
        while True:
            print("\n--- Меню администратора ---")
            print("1. Добавление трека")
            print("2. Удаление трека")
            print("3. Редактирование трека")
            print("4. Выход")
            choice = input("Выберите действие: ")

            if choice == '1':
                Admin.add_track()
            elif choice == '2':
                Admin.delete_track()
            elif choice == '3':
                Admin.edit_track()
            elif choice == '4':
                print("Выход из системы...")
                break
            else:
                print("Некорректный выбор.")