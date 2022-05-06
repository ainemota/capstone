# Capstone Q3 - ReOff
base_url = https://reoff.herokuapp.com/
# Users
### POST /users/signup
Rota para cadastro de novos usuarios

Request
```json
{
	"name": "Alice",
	"email": "alice_maravilhas@gmail.com",
	"password": "*********",
	"address": {
        "CEP": "30570000",
        "number": "417",
        "complement": "Apt. 401"
	}
}
```
Response - 201 CREATED
```json
{
	"id": "1b9d6bcd-bbfd-4b2d-9b5d-ab8dfbbd4bed",
	"nome": "Alice",
	"email": "alice_maravilhas@gmail.com"
}
```

### GET /users/login
Rota para login de usuarios

Request
```json
{
    "email": "Barbara@kenzie.com",
    "password": "354685777"
}
```
Response - 200 OK
```json
{
	"accessToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY1MTc4NDI3NCwianRpIjoiZDA2ZmExNGItMzc2ZC00NWEwLTlkZGItYjY5NzZlMWM4MjFhIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJpZCI6IjZhZDk3NDJmLTczM2MtNDQyZi1iYjIxLTJmOGIzZjk4YzgwZCIsIm5hbWUiOiJ1c2VyMiIsImVtYWlsIjoidXNlcjJAbWFpbCIsImFkZHJlc3NfaWQiOiI4NmM0MTBiMy1hMjIyLTQ1ZDgtYmZhOC00MDQ1NGIzNGVlZmUifSwibmJmIjoxNjUxNzg0Mjc0LCJleHAiOjE2NTE3ODc4NzR9.zdEgz5hARxgr5SjVrS5hVp1DvBLZ1-ix9XZYCNph36E"
}
```

### GET /users
Lista todos os usuarios cadastrados

header:
{
    Authorization: `Bearer{token}`
}

Response - 200 OK
```json
{
	"data": [
            {
                "id": "1b9d6bcd-bbfd-4b2d-9b5d-ab8dfbbd4bed",
                "nome": "Bruna",
                "email": "bruna@kenzie.com"
            },
            {
                "id": "1b9d6bcd-dbfd-5b2d-9u5d-ab8dfbbd4bed",
                "nome": "Carol",
                "email": "carol_oliveira@gmail.com"
            }
]
}
```

### PATCH /users/<user_id>
Atualiza dados do usuario 

header:
{
    Authorization: `Bearer{token}`
}

Request
```json
{
	"nome": "Brenda",
	"email": "brenda_po@hotmai",
	"password":"2102563"
}
```
Response - 200 OK
```json
{
      "user_updated": {
        "id": "1b9d6bcd-bbfd-4b2d-9b5d-ab8dfbbd4bed",
        "nome": "Brenda",
        "email": "brenda_po@hotmai"
      }
}
```
### DELETE /users/<user_id>
Deleta a conta do usuario

Response - 204 NO CONTENT

# Addresses
### POST /addresses
Cadastra um novo endereço

header:
{
    Authorization: `Bearer {token}`
}

Request
```json
 
{
  "adressess": [
      {
        "CEP": "30570000",
        "numero": "417",
        "complemento": "Apt. 401"
      }
  ]
}
```
Response - 201 CREATED
```json
{

    "id": 257,
    "CEP": "30570000",
    "estado": "Minas Gerais",
    "cidade": "Vila Velha",
    "rua": "Luiz Fernandes Reis",
    "numero": "417",
    "complemento": "Apt. 401"

}
```
### GET /addresses/
Lista os endereços cadastrados

header:
{
    Authorization: `Bearer {token}`
}

Response - 200 OK
```json
{ 
    "resultados": 2,
    "adressess": [
                  {
                      "id": 257,
                      "CEP": "30570000",
                      "estado": "Espírito Santo",
                      "cidade": "Vila Velha",
                      "rua": "Luiz Fernandes Reis",
                      "numero": "417",
                      "complemento": "Apt. 401"
                  },
                  {
                      "id": 258,
                      "CEP": "30570120",
                      "estado": "Minas Gerais",
                      "cidade": "Belo Horizonte",
                      "rua": "Ladeira do amendoim",
                      "numero": "410",
                      "complemento": "Apt. 602"
                  }
              ]
}
```
### PATCH /addresses/<address_id>
Atualiza o endereço cadastrado

header:
{
    Authorization: `Bearer {token}`
}

Request
```json
{
    "CEP": "30550021",
    "numero": 22,
    "complemento": "Apt. 602"
}
```
Response - 200 OK
```json
{
    "data":
    {
        "CEP": "30550021",
        "estado": "Rio de Janeiro",
        "cidade": "Rio de Janeiro",
        "rua": "Av Copacabana",
        "numero": 22,
        "complemento": "Apt. 602"
    }
}
```
### DELETE /addresses/<address_id>
Deleta o endereço que foi cadastrado

header:
{
    Authorization: `Bearer {token}`
}

Response - 204 NO CONTENT

# Rooms

