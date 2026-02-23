# 🎬 Movie Collection API

**Hey! 👋 Thanks for checking out my  development project.**

While my main focus as a student is on **Artificial Intelligence and Machine Learning**, I realize that knowing how to build an AI model is only half the battle—deploying it so users can interact with it is the other half.

I built this **Movie Collection API** using **FastAPI** to master the fundamentals of backend architecture. I implemented the logic to handle full **CRUD** operations, integrated unique **UUID** tracking for every record, and used **Pydantic** for strict data validation. This serves as a foundational step toward my goal of deploying scalable, production-ready AI agents.

---
## 🛠️ Tech Stack
* **Language:** Python
* **Framework:** FastAPI
* **Server:** Uvicorn
* **Validation:** Pydantic

## ✨ Features
* **Full CRUD Operations:** Seamlessly Create, Read, Update, and Delete movie records.
* **Unique Identification:** Automatically generates a unique UUID for every movie added to the collection.
* **Data Validation:** Uses **Pydantic** models to ensure every entry has a valid name, director, and release year.
* **In-Memory Storage:** Optimized for fast performance during testing and development.
* **Robust Error Handling:** Integrated HTTP exceptions (404) for handling requests for non-existent IDs.



## 🚀 How to Run Localy

To test this API on your own machine, follow these steps in your terminal:

**1. Clone the repository:**
`git clone https://github.com/Keerthanapalvannan-25/fastapi-movie-api.git`
`cd fastapi-movie-api`

**2. Install the required dependencies:**
`pip install fastapi uvicorn`

**3. Start the local server:**
`uvicorn main:app --reload`

**4. Test the API:**
Open your web browser and navigate to the interactive documentation at:
👉 `http://127.0.0.1:8000/docs`

## 📡 API Endpoints Summary

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/movies` | Add a new movie to the collection |
| `GET`  | `/movies` | Retrieve all movies in the list |
| `GET`  | `/movies/{id}` | Find a specific movie by its unique ID |
| `PUT`  | `/movies/{id}` | Update movie details (Director, Year, etc.) |
| `DELETE`| `/movies/{id}` | Remove a movie from the collection |
