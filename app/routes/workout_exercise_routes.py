from flask import Blueprint, request, jsonify

from app.extensions import db
from app.models.workout import Workout
from app.models.exercise import Exercise
from app.models.workout_exercise import WorkoutExercise
from app.schemas.workout_exercise_schema import WorkoutExerciseSchema

workout_exercise_bp = Blueprint("workout_exercise_bp", __name__)

workout_exercise_schema = WorkoutExerciseSchema()


@workout_exercise_bp.route("/", methods=["POST"])
def add_exercise_to_workout(workout_id, exercise_id):
    workout = Workout.query.get_or_404(workout_id)
    exercise = Exercise.query.get_or_404(exercise_id)

    data = request.get_json()

    workout_exercise = WorkoutExercise(
        workout=workout,
        exercise=exercise,
        reps=data.get("reps"),
        sets=data.get("sets"),
        duration_seconds=data.get("duration_seconds")
    )

    db.session.add(workout_exercise)
    db.session.commit()

    return jsonify(workout_exercise_schema.dump(workout_exercise)), 201