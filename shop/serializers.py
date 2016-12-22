from rest_framework import serializers
from .models import BookInfo, University, Student


class BookSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    isbn_no = serializers.CharField(max_length=50)
    price = serializers.DecimalField(max_digits=5, decimal_places=2)
    author = serializers.CharField(max_length=20)

    def create(self, validated_data):
        return BookInfo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.isbn_no = validated_data.get('isbn_no', instance.isbn_no)
        instance.price = validated_data.get('price', instance.price)
        instance.author = validated_data.get('author', instance.author)
        instance.save()
        return instance

class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ('name',)


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('name', 'id_no', 'university')