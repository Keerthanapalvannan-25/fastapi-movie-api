from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import uuid

app = FastAPI(title="Movie Collection API")

# Pydantic Model
class Movie(BaseModel):
    name: str
    director: str
    year: int

# In-memory storage
movies: List[dict] = []

# Home
@app.get("/")
def home():
    return {"message": "Movie Collection API is running"}

# CREATE
@app.post("/movies")
def add_movie(movie: Movie):
    movie_dict = movie.dict()
    movie_dict["id"] = str(uuid.uuid4())
    movies.append(movie_dict)
    return movie_dict

# READ ALL
@app.get("/movies")
def get_movies():
    return movies

# READ ONE BY ID
@app.get("/movies/{movie_id}")
def get_movie(movie_id: str):
    for movie in movies:
        if movie["id"] == movie_id:
            return movie
    raise HTTPException(status_code=404, detail="Movie not found")

# UPDATE BY ID
@app.put("/movies/{movie_id}")
def update_movie(movie_id: str, updated_movie: Movie):
    for movie in movies:
        if movie["id"] == movie_id:
            movie.update(updated_movie.dict())
            return movie
    raise HTTPException(status_code=404, detail="Movie not found")

# DELETE BY ID
@app.delete("/movies/{movie_id}")
def delete_movie(movie_id: str):
    for movie in movies:
        if movie["id"] == movie_id:
            movies.remove(movie)
            return {"message": "Movie deleted successfully"}
    raise HTTPException(status_code=404, detail="Movie not found")