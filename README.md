# Taskboard – Django REST Framework Task Manager

## Setup
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
Open http://127.0.0.1:8000/ for the UI. API base: http://127.0.0.1:8000/api/tasks/

## Endpoints
| Method | URL | Purpose |
|---|---|---|
| GET | /api/tasks/ | List tasks |
| POST | /api/tasks/ | Create task |
| GET | /api/tasks/<id>/ | Retrieve one |
| PUT / PATCH | /api/tasks/<id>/ | Update (full / partial) |
| DELETE | /api/tasks/<id>/ | Delete |

## Postman
Import `Taskboard.postman_collection.json` (File > Import). Start the server, then run the requests in order.
