# REST API for yatube project
Django Rest Framework API, that include CRUD operations for post and comment models, 
allows create and get user's follows and see existing groups.
## How to start project
Clone and open project via command line:
```
https://github.com/Kirill152251/api_final_yatube.git
```
```
cd yatube_api
```
Create and activate virtual environment:
```
python -m venv venv
```
```
source venv/bin/activate
```
Install dependencies:
```
python3 -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
Complete migrations:
```
python manage.py migrate
```
Star server on local computer:
```
python manage.py runserver
```
After starting server you can see full API documentaion at http://127.0.0.1:8000/redoc/ address.
## Request exapmples
### Getting post with id=1488:

Request address - http://127.0.0.1:8000/api/v1/posts/1488/.

Response:
```
{
  "id": 1488,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```
### Posting comment to post with id = 322:

Request address - http://127.0.0.1:8000/api/v1/posts/322/comments/.

Request body:
```
{
  "text": "some text"
}
```
Response:
```
{
  "id": 322,
  "author": "string",
  "text": "some text",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
```
### Get current user's follows:

Request address - http://127.0.0.1:8000/api/v1/follow/.

Response:
```
[
  {
    "user": "string",
    "following": "string1"
  },
  {
    "user": "string",
    "following": "string2"
  },
  {
    "user": "string",
    "following": "string3"
  }
]
```
