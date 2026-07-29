from flask import Blueprint, request, jsonify

from app.extensions import db
from app.models.exercise import Exercise
from app.schemas.exercise_schema import ExerciseSchema

exercise_bp = Blueprint("exercise_bp", __name__)

exercise_schema = ExerciseSchema()
exercises_schema = ExerciseSchema(many=True)


@exercise_bp.route("/", methods=["GET"])
def get_exercises():
    exercises = Exercise.query.all()
    return jsonify(exercises_schema.dump(exercises)), 200


@exercise_bp.route("/<int:id>", methods=["GET"])
def get_exercise(id):
    exercise = Exercise.query.get_or_404(id)
    return jsonify(exercise_schema.dump(exercise)), 200


@exercise_bp.route("/", methods=["POST"])
def create_exercise():
    data = request.get_json()

    exercise = Exercise(
        name=data["name"],
        category=data["category"],
        equipment_needed=data["equipment_needed"]
    )

    db.session.add(exercise)
    db.session.commit()

    return jsonify(exercise_schema.dump(exercise)), 201


@exercise_bp.route("/<int:id>", methods=["DELETE"])
def delete_exercise(id):
    exercise = Exercise.query.get_or_404(id)

    db.session.delete(exercise)
    db.session.commit()

    return jsonify({"message": "Exercise deleted successfully"}), 200