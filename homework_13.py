import csv
import requests

url = "http://jsonplaceholder.typicode.com/todos"
response = requests.get(url)
data = response.json()


with open("homework13p1.csv", "w", newline="", encoding="utf-8-sig") as file:
    headers = data[0].keys()

    writer = csv.DictWriter(file, fieldnames=headers, delimiter=";")

    writer.writeheader()
    writer.writerows(data)