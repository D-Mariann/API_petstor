import json
import requests

url = 'https://petstore.swagger.io/v2'
status = {
    'status' : 'available'
}
headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}
user = {
    "id": 0,
    "username": "rrraaawr",
    "firstName": "Ivan",
    "lastName": "Stringovich",
    "email": "rrraaa@yandex.ru",
    "password": "123321",
    "phone": "81231234569",
    "userStatus": 0
}
login = {'email' : user['email'], 'password': user["password"]}
pet = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "Mars"
  },
  "name": "cat",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "Marsic"
    }
  ],
  "status": "available"
}

def try_exept(res):
    status = res.status_code
    try:
        result = res.json()
    except:
        result = res.text
    return status, result

def get_available_pets(url, status, func):
    res = requests.get(f"{url}/pet/findByStatus?status={status}",
                   headers = {'accept': 'application/json'})
    result = func(res)
    return status, result

def create_user(url, user, headers, func):
    user = json.dumps(user)
    res = requests.post(url + '/user', headers=headers, data=user)
    result = func(res)
    return result

def login_user(url, login, headers, func):
    res = requests.get(url + '/user/login', headers=headers, data=login)
    result = func(res)
    return result

def upd_user(url, username, headers, func):
    data = {
    "id": 0,
    "username": "rrraaawr",
    "firstName": "Ivan",
    "lastName": "Stringovich",
    "email": "rrraaa@yandex.ru",
    "password": "123321",
    "phone": "89263333333",
    "userStatus": 0
}
    res = requests.put(f'{url}/user/{username}', headers=headers, json=data)
    result = func(res)
    return result

def post_pet(url, pet, headers, func):
    pet = json.dumps(pet)
    res = requests.post(url + '/pet', headers=headers, data=pet)
    result = func(res)
    return result

def delete_pet(url, petId, func):
    res = requests.delete(f'{url}/pet/{petId}')
    result = func(res)
    return result

print(get_available_pets(url, status, try_exept))
print(create_user(url, user, headers, try_exept))
print(login_user(url, login, headers, try_exept))
post_pet = post_pet(url, pet, headers, try_exept)
petId = post_pet[1]['id']
print(delete_pet(url, petId, try_exept))
print(upd_user(url, user['username'], headers,try_exept))