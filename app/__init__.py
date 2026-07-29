from flask import Flask

from config import Config
from app.extensions import db, migrate


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Import models
    from app.models.workout import Workout
    from app.models.exercise import Exercise
    from app.models.workout_exercise import WorkoutExercise

    # Import blueprints
    from app.routes.workout_routes import workout_bp
    from app.routes.exercise_routes import exercise_bp
    from app.routes.workout_exercise_routes import workout_exercise_bp

    # Register blueprints
    app.register_blueprint(workout_bp, url_prefix="/workouts")
    app.register_blueprint(exercise_bp, url_prefix="/exercises")
    app.register_blueprint(
        workout_exercise_bp,
        url_prefix="/workouts/<int:workout_id>/exercises/<int:exercise_id>/workout_exercises"
    )

    return app