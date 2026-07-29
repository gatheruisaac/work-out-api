# work-out-api# 🏋️ Workout API

A RESTful Workout API built with **Flask**, **Flask-SQLAlchemy**, **Flask-Migrate**, and **Marshmallow**. The application enables personal trainers and fitness enthusiasts to manage workouts, exercises, and the relationship between them.

---

## 📖 Project Overview

This API allows users to:

- Create and manage workouts
- Create and manage exercises
- Associate multiple exercises with a workout
- Track workout details such as sets, reps, and duration using a join table
- Retrieve workouts with their associated exercises
- Retrieve exercises with their associated workouts

---

## 🛠️ Technologies Used

- Python 3
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Marshmallow
- SQLite
- Pipenv
- Postman

---

## 📁 Project Structure

```
work-out-api/
│
├── app/
│   ├── __init__.py
│   ├── extensions.py
│   ├── models/
│   ├── routes/
│   └── schemas/
│
├── migrations/
├── config.py
├── run.py
├── seed.py
├── requirements.txt
├── Pipfile
├── Pipfile.lock
└── README.md
```

---

## 🗄️ Database Models

### Exercise

| Field | Type |
|--------|------|
| id | Integer |
| name | String |
| category | String |
| equipment_needed | Boolean |

### Workout

| Field | Type |
|--------|------|
| id | Integer |
| date | Date |
| duration_minutes | Integer |
| notes | Text |

### WorkoutExercise (Join Table)

| Field | Type |
|--------|------|
| id | Integer |
| workout_id | Foreign Key |
| exercise_id | Foreign Key |
| reps | Integer |
| sets | Integer |
| duration_seconds | Integer |

---

## 🔗 Relationships

- A Workout has many WorkoutExercises.
- An Exercise has many WorkoutExercises.
- A WorkoutExercise belongs to one Workout.
- A WorkoutExercise belongs to one Exercise.
- A Workout has many Exercises through WorkoutExercises.
- An Exercise has many Workouts through WorkoutExercises.

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/gatheruisaac/work-out-api.git
```

Navigate into the project:

```bash
cd work-out-api
```

Install the project dependencies:

```bash
pipenv install
```

Activate the virtual environment:

```bash
pipenv shell
```

---

# ▶️ Running the Application

Start the Flask development server:

```bash
pipenv run python3 run.py
```

The application will run at:

```
http://127.0.0.1:5000
```

---

# 🗃️ Database Setup

Initialize the database migrations:

```bash
pipenv run flask --app run.py db init
```

Generate a migration:

```bash
pipenv run flask --app run.py db migrate -m "Initial migration"
```

Apply the migration:

```bash
pipenv run flask --app run.py db upgrade
```

---

# 🌱 Seed the Database

Populate the database with sample workout data:

```bash
pipenv run python3 seed.py
```

---

# 📡 API Endpoints

## Workouts

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/workouts/` | Retrieve all workouts |
| GET | `/workouts/<id>` | Retrieve a specific workout |
| POST | `/workouts/` | Create a new workout |
| DELETE | `/workouts/<id>` | Delete a workout |

---

## Exercises

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/exercises/` | Retrieve all exercises |
| GET | `/exercises/<id>` | Retrieve a specific exercise |
| POST | `/exercises/` | Create a new exercise |
| DELETE | `/exercises/<id>` | Delete an exercise |

---

## Workout Exercises

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/workouts/<workout_id>/exercises/<exercise_id>/workout_exercises/` | Add an exercise to a workout with reps, sets, and duration |

---

# 🧪 Testing

The API was tested using **Postman**.

The following endpoints were successfully tested:

- GET all workouts
- GET a single workout
- POST a workout
- DELETE a workout
- GET all exercises
- GET a single exercise
- POST an exercise
- DELETE an exercise
- POST a WorkoutExercise

---

# 📌 Example Requests

## Create a Workout

```json
{
    "date": "2026-08-01",
    "duration_minutes": 60,
    "notes": "Full body workout"
}
```

## Create an Exercise

```json
{
    "name": "Bench Press",
    "category": "Chest",
    "equipment_needed": true
}
```

## Add an Exercise to a Workout

```json
{
    "reps": 10,
    "sets": 4,
    "duration_seconds": 0
}
```