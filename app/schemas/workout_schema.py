from marshmallow import Schema, fields
from app.schemas.exercise_schema import ExerciseSchema


class WorkoutSchema(Schema):
    id = fields.Int(dump_only=True)
    date = fields.Date(required=True)
    duration_minutes = fields.Int(required=True)
    notes = fields.Str()

    exercises = fields.List(
        fields.Nested(ExerciseSchema),
        dump_only=True
    )