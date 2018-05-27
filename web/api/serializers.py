from rest_framework import serializers
import base64


class InferenceRequest(object):
    def __init__(self, x_min: float, y_min: float, x_max: float, y_max: float, image_data: str, rectangularize: bool):
        self.x_min = x_min
        self.y_min = y_min
        self.x_max = x_max
        self.y_max = y_max
        self.image_data = image_data
        self.rectangularize = rectangularize


def validate_base64(s: str) -> None:
    print("Validating base64", s, type(s))
    try:
        base64.standard_b64decode(s)
    except Exception as e:
        msg = "Ensure this value is a base64 encoded."
        print(e)
        raise serializers.ValidationError(msg)


class InferenceRequestSerializer(serializers.Serializer):
    x_min = serializers.FloatField(required=False)
    y_min = serializers.FloatField(required=False)
    x_max = serializers.FloatField(required=False)
    y_max = serializers.FloatField(required=False)
    rectangularize = serializers.FloatField(required=False, default=True)
    image_data = serializers.CharField(required=True,
                                       allow_blank=False,
                                       allow_null=False,
                                       help_text="Image data as base64 encoded string",
                                       validators=[validate_base64]
                                       )
