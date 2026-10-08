import csv
import requests

POSTS_URL = "https://jsonplaceholder.typicode.com/posts"

def fetch_and_print_posts():

    response = requests.get(POSTS_URL)

    print(f"Status Code: {response.status_code}")

    if response.status_code != 200:
        return

    datas = response.json()
    for data in datas:
        print(data["title"])


def fetch_and_save_posts():
    response = requests.get(POSTS_URL)

    if response.status_code != 200:
        return

    data_list = []
    datas = response.json()
    for data in datas:
        data_dict = {
            "id": data["id"],
            "title": data["title"],
            "body": data["body"]
        }
        data_list.append(data_dict)

    with open("posts.csv", "w", newline="", encoding="utf-8") as file:
        fields = ["id", "title", "body"]
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        for data in data_list:
            writer.writerow(data)
