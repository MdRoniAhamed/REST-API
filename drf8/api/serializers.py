from rest_framework import serializers
from .models import Student

# Validators
def start_with_r(value):
    if value.lower()[0] != 'r':
        raise serializers.ValidationError("Nme Should be start with R")
    
class StudentSerializer(serializers.ModelSerializer):
    # def start_with_r(value):
    #     if value.lower()[0] != 'r':
    #         raise serializers.ValidationError("Nme Should be start with R")
    name = serializers.CharField(validators=[start_with_r])
    class Meta:
        model = Student
        fields = ['name','roll','city']
# Field level Validation
    def validate_roll(self, value):
        if value>= 200:
            raise serializers.ValidationError('Seat Full!!')
        return value
    
# Object level validation    
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'roni' and ct.lower() != 'mymensingh':
            raise serializers.ValidationError('City must be Mymensingh')
        return data