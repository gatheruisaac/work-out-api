from flask import Blueprint, request, jsonify
from datetime import datetime

from app.extensions import db
from app.models.workout import Workout
from app.schemas.workout_schema import WorkoutSchema

workout_bp = Blueprint("workout_bp", __name__)

workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True)


@workout_bp.route("/", methods=["GET"])
def get_workouts():
    workouts = Workout.query.all()
    return jsonify(workouts_schema.dump(workouts)), 200


@workout_bp.route("/<int:id>", methods=["GET"])
def get_workout(id):
    workout = Workout.query.get_or_404(id)
    return jsonify(workout_schema.dump(workout)), 200


@workout_bp.route("/", methods=["POST"])
def create_workout():
    data = request.get_json()

    workout = Workout(
        date=datetime.strptime(data["date"], "%Y-%m-%d").date(),
        duration_minutes=data["duration_minutes"],
        notes=data.get("notes")
    )

    db.session.add(workout)
    db.session.commit()

    return jsonify(workout_schema.dump(workout)), 201


@workout_bp.route("/<int:id>", methods=["DELETE"])
def delete_workout(id):
    workout = Workout.query.get_or_404(id)

    db.session.delete(workout)
    db.session.commit()

    return jsonify({"message": "Workout deleted successfully"}), 200