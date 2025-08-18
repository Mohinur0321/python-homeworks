import json
import requests


with open("students.json", "r") as f:
    students = json.load(f)


for student in students:
    print(f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")


#2


city = 'Tashkent'
        #, 'London', 'Czech Republic']
api_key = '0dedf962808bb77ca0fc883f728fb1fb'
url = 'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

response = requests.get(url)
my_data = response.json()

print(my_data['name'], my_data['weather']['main']['temp'], str(my_data['main']['humidity']),
        str(my_data['wind']['speed'])]))

#3
import requests
import json

print('1. Yangi kitob qoshish')
print('2. KItob malumotini yangilash')
print('3. Kitob haqidagi malumotni ochirish')

answer = input('Enter number')
if answer == '1':
    with open('library.json') as f:
        my_dict = json.load(f)

    book_id = int(input('Kitobning idsini kiriting: '))
    book_name = input("Kutubxonaga qo'shmoqchi bo'lgan kitob nomini kiriting: ")
    author_name = input("Kitob muallifini kiriting: ")

    for i in my_dict.values():
        i.append({'book_id': book_id, 'book_name': book_name, 'author_name': author_name})


    with open('my_lib', 'w') as f:
        json.dump(my_dict, f, indent = 2)

if answer == '2':
    with open('my_lib') as f:
        data = json.load(f)

    id = int(input('Kitobning idsini kiriting: '))
    name = input('Ozgargan nom')
    author = input('Ozgargan yozuvchi')

    if id == data[id]:
        data[book_name] = name
        data[author] = author
    else:
        print('Bunday id-li kitob mavjud emas')
    
    with open('edited') as f:
        json.dump('my_lib', f, indent = 2)

if answer == '3':
    id = int(input('Kitobning idsini kiriting: '))

    with open('my_lib') as f:
        data = json.load(f)
    data["books"] = [book for book in data["books"] if book["id"] != id]

    with open('my_lib', 'w') as f:
        json.dump('my_lib', f, indent = 2)


import requests

genre = "Adventure"
search_word = "kill"   # instead of exact title, use keyword
result = []

url = f"http://www.omdbapi.com/?s={search_word}&apikey=4bdb38cb"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    if "Search" in data:
        for movie in data["Search"]:
            movie_id = movie["imdbID"]
            details_url = f"http://www.omdbapi.com/?i={movie_id}&apikey=4bdb38cb"
            details = requests.get(details_url).json()

            if genre.lower() in details.get("Genre", "").lower():
                result.append(details["Title"])

print(result)

