#!/usr/bin/python3

import requests, json

headers = {'Content-Type':'application/json'}
data = json.dumps({"nome" : "No One"})

response = requests.get('http://127.0.0.1:5000/usuarios')
#print(response.json())
#print(dir(response))

#print(data)
#response = requests.post('http://127.0.0.1:5000/usuarios', data=data, headers=headers)
#print(response.json())

#response = requests.delete('http://127.0.0.1:5000/usuarios/7')
#print(response.json())

print('{0:.^10}{1:.^30}'.format('ID','NOME'))
data = response.json()
#<^> - Alinhado a esquerda,  ao centro e a direita
#print(data['usuarios'])
for X in data['usuarios']:
    if X['id'] % 2 == 0:
        print('{0:^10}{1:^30}'.format(X['id'], X['nome']))
