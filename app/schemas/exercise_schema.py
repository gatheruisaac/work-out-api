from marshmallow import Schema, fields


class WorkoutSummarySchema(Schema):
    id = fields.Int()
    date = fields.Date()
    duration_minutes = fields.Int()
    notes = fields.Str()


class ExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    category = fields.Str(required=True)
    equipment_needed = fields.Bool(required=True)

    workouts = fields.List(
        fields.Nested(WorkoutSummarySchema),
        dump_only=True
    )