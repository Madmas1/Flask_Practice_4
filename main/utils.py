import json


def load_json_data(path):
    with open(path, 'r', encoding="UTF-8") as file:
        return json.load(file)


def search_post_by_substring(posts, substring):
    founded_posts = []
    for post in posts:
        if substring.lower() in post["content"].lower():
            founded_posts.append(post)
    return founded_posts
