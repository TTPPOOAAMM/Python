import json

class Authenticate():
    users = [
    {
        'username': 'user',
        'password': 'user',
        'role': 'user',
        'subscription_type': 'Premium',
        'history': ['Киндер Буэно', 'Judas'],
        'created_at': '2024-01-10'
    },
    {
        'username': 'admin_user',
        'password': 'adminpass',
        'role': 'admin'
    }
]
    def authenticate():
        username = input("Введите логин: ")
        password = input("Введите пароль: ")
        for user in Authenticate.users:
            if user['username'] == username and user['password'] == password:
                return user
        print("Неверный логин или пароль.")
        return None





class User():
    tracks = [
    {'title': '100 Barz', 'artist': 'Слава КПСС', 'genre': 'Рэп', 'rating': 9.8},
    {'title': 'Киндер Буэно', 'artist': 'Валентин Дядька', 'genre': 'Рэп', 'rating': 9.9},
    {'title': 'Blinding Lights', 'artist': 'The Weeknd', 'genre': 'Поп', 'rating': 9.5},
    {'title': 'Judas', 'artist': 'Lady Gaga', 'genre': 'Поп', 'rating': 9.2}
    ]
    def view_tracks():
        print("\n--- Доступные треки ---")
        for track in User.tracks:
            print(f"- {track['title']} ({track['artist']}) - Жанр: {track['genre']}, Рейтинг: {track['rating']}")

    def listen_to_track(user):
        User.view_tracks()
        track_title = input("Введите название трека для прослушивания: ")
        for track in User.tracks:
            if track['title'] == track_title:
                user.setdefault('history', []).append(track['title'])
                print(f"Вы слушаете: {track_title} от {track['artist']}.")
                return
        print("Трек не найден.")

    def view_history(user):
        print("\n--- История прослушиваний ---")
        for track in user.get('history', []):
            print(f"- {track}")

    def sort_and_filter_tracks():
        print("\n1. Сортировать по рейтингу")
        print("2. Фильтровать по жанру")
        choice = input("Выберите действие: ")

        if choice == '1':
            sorted_tracks = sorted(User.tracks, key=lambda x: x['rating'], reverse=True)
            for track in sorted_tracks:
                print(f"{track['title']} - Рейтинг: {track['rating']}")
        elif choice == '2':
            genre = input("Введите жанр для фильтрации: ")
            filtered_tracks = filter(lambda x: x['genre'].lower() == genre.lower(), User.tracks)
            for track in filtered_tracks:
                print(f"{track['title']} ({track['artist']}) - Жанр: {track['genre']}")
        else:
            print("Некорректный выбор.")

class Admin():
    def add_track():
        title = input("Введите название трека: ")
        artist = input("Введите исполнителя: ")
        genre = input("Введите жанр: ")
        rating = float(input("Введите рейтинг трека: "))
        User.tracks.append({'title': title, 'artist': artist, 'genre': genre, 'rating': rating})
        print("Трек успешно добавлен.")

    def delete_track():
        track_title = input("Введите название трека для удаления: ")
        global tracks
        User.tracks = [track for track in User.tracks if track['title'] != track_title]
        print("Трек успешно удален.")

    def edit_track():
        track_title = input("Введите название трека для редактирования: ")
        for track in User.tracks:
            if track['title'] == track_title:
                track['artist'] = input("Введите нового исполнителя: ")
                track['genre'] = input("Введите новый жанр: ")
                track['rating'] = float(input("Введите новый рейтинг: "))
                print("Трек успешно обновлен.")
                return
        print("Трек не найден.")



