#===== Методы для обработки main view =====#


def search_post_by_substring(posts, substring):
    """Метод для поиска постов"""
    # Создаем пустой список в который будут добавлены найденные посты
    founded_posts = []
    # Поиск постка по введеной фразе
    for post in posts:
        if substring.lower() in post["content"].lower():
            founded_posts.append(post)
    # Возращаем найденные посты
    return founded_posts
