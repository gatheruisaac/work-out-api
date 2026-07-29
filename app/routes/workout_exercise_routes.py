from flask import Blueprint, jsonify

workout_exercise_bp = Blueprint(
    "workout_exercise_bp",
    __name__
)


@workout_exercise_bp.route("/", methods=["POST"])
def add_exercise_to_workout():
    return jsonify({"message": "WorkoutExercise route working"})