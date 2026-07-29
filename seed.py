from datetime import date

from app import create_app
from app.extensions import db
from app.models.workout import Workout
from app.models.exercise import Exercise
from app.models.workout_exercise import WorkoutExercise

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    # Exercises
    squat = Exercise(
        name="Squat",
        category="Legs",
        equipment_needed=False
    )

    pushup = Exercise(
        name="Push Up",
        category="Chest",
        equipment_needed=False
    )

    plank = Exercise(
        name="Plank",
        category="Core",
        equipment_needed=False
    )

    db.session.add_all([squat, pushup, plank])
    db.session.commit()

    # Workouts
    workout1 = Workout(
        date=date(2026, 7, 29),
        duration_minutes=45,
        notes="Morning strength workout"
    )

    workout2 = Workout(
        date=date(2026, 7, 30),
        duration_minutes=30,
        notes="Core training session"
    )

    db.session.add_all([workout1, workout2])
    db.session.commit()

    # Join table
    db.session.add_all([
        WorkoutExercise(
            workout=workout1,
            exercise=squat,
            reps=12,
            sets=4,
            duration_seconds=0
        ),
        WorkoutExercise(
            workout=workout1,
            exercise=pushup,
            reps=15,
            sets=3,
            duration_seconds=0
        ),
        WorkoutExercise(
            workout=workout2,
            exercise=plank,
            reps=0,
            sets=3,
            duration_seconds=60
        )
    ])

    db.session.commit()

    print("Database seeded successfully!")