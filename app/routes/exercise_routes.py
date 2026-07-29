from flask import Blueprint, jsonify, request

exercise_bp = Blueprint("exercise_bp", __name__)


@exercise_bp.route("/", methods=["GET"])
def get_exercises():
    return jsonify({"message": "Exercise routes working"})


@exercise_bp.route("/", methods=["POST"])
def create_exercise():
    return jsonify({"message": "Create exercise"})