# VOD Application

### Genre Service API Architecture
- Runs on :5001
  - Admin CRUD API
    - [GET] => api/genres?page=1 (All genres)
    - [GET] => api/genres/{id} (Show a genre)
    - [POST] => api/genres (Create a genre)
    - [PUT] => api/genres/{id} (Update a genre)
    - [DELETE] => api/genres/{id} (Delete a genre)
  - Frontend API
    - [GET] => api/genres/{genre_slug}/films?page=1 (See genre's films)

### Content Service API Architecture
- Runs on :5000
    - Admin CRUD API
        - [GET] => api/films?page=1 (All films)
        - [GET] => api/films/{id} (Show a film)
        - [POST] => api/films (Create a film)
        - [PUT] => api/films/{id} (Update a film)
        - [DELETE] => api/films/{id} (Delete a film)
    - Frontend API
        - [GET] => api/films/genre/{genre_id}?page=1 (See genre's films)

## Stack
* **Flask**
* **PostgreSQL**
* **Redis**
* **Docker**

### Requirements for local installation

- Docker

### Installation
```
  chmod +x install.sh && ./install.sh
```

# Endpoints Collection
- Import vod.postman_collection.json to your postman, and you can easily see all endpoints 
