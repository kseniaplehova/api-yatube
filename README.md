# Yatube API

REST API for Yatube, a small social network: CRUD for posts and comments, read-only groups, token authentication.

> Educational project — Yandex Practicum, Python Developer course.

## Features

- **Token authentication** (DRF `authtoken`): obtain a token at `POST /api/v1/api-token-auth/`, then send `Authorization: Token <token>`.
- **Posts**: full CRUD with optional image upload and optional group; the author is taken from the authenticated user.
- **Comments**: full CRUD nested under a post.
- **Groups**: read-only (list and detail).
- **Permissions**: every endpoint requires authentication; editing and deleting posts and comments is allowed only to their author (custom `IsAuthorOrReadOnly`).
- Author is exposed by username in responses (`SlugRelatedField`).

## Endpoints

All paths are prefixed with `/api/v1/`.

| Method | Path | Description |
| --- | --- | --- |
| POST | `api-token-auth/` | Obtain an auth token (username + password) |
| GET, POST | `posts/` | List / create posts |
| GET, PUT, PATCH, DELETE | `posts/{id}/` | Post detail (write: author only) |
| GET | `groups/`, `groups/{id}/` | Groups |
| GET, POST | `posts/{post_id}/comments/` | Comments of a post |
| GET, PUT, PATCH, DELETE | `posts/{post_id}/comments/{id}/` | Comment detail (write: author only) |

## Tech stack

- Python, Django 5.1.1, Django REST Framework 3.15.2
- SQLite, Pillow 11.0.0
- pytest 8.3.3, pytest-django 4.9.0

## Getting started

```bash
git clone https://github.com/kseniaplehova/api-yatube.git
cd api-yatube
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
cd yatube_api
python manage.py migrate
python manage.py createsuperuser   # needed to have a user to get a token for
python manage.py runserver
```

## Usage example

```bash
# get a token
curl -X POST http://127.0.0.1:8000/api/v1/api-token-auth/ \
  -H "Content-Type: application/json" \
  -d '{"username": "<user>", "password": "<password>"}'

# create a post
curl -X POST http://127.0.0.1:8000/api/v1/posts/ \
  -H "Authorization: Token <token>" \
  -H "Content-Type: application/json" \
  -d '{"text": "Hello, Yatube"}'
```

## Tests

From the repository root:

```bash
pytest
```

Tests live in `tests/` (auth, posts, groups, comments, settings). A Postman collection is available in `postman_collection/`.

## Author

Ksenia Plehova — [GitHub](https://github.com/kseniaplehova)
