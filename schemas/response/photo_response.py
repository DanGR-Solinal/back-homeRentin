from marshmallow import fields, Schema

class PhotoResponse(Schema):
    photo_url = fields.String(required=True)