from rest_framework import serializers 
from rest_framework.validators import UniqueValidator

from datetime import datetime

from .models import Media, Genre

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'
        ready_only_fields = ['id']

class MediaSerializer(serializers.ModelSerializer):
    def __init__(self, instance=None, data=..., genre: list = [], **kwargs):
        super().__init__(instance, data, **kwargs)

        self.genres = genre

    genre = GenreSerializer(many=True, read_only=True)
    class Meta:
        model = Media
        fields = '__all__'
        ready_only_fields = ['id']

    
    def validate_title(self, value): 
        if Media.objects.filter(title=value).exists():
            raise serializers.ValidationError('Title already exists')
        return value 

    def validate_year(self, value):
        if value < 1900:
            raise serializers.ValidationError('Year must be greater than 1900')
        elif value > datetime.now().year:
            raise serializers.ValidationError('Year must be less than the current year')
        
        return value

    def create(self, validated_data):
        if len(self.genres) == 0:
            raise serializers.ValidationError('Genre is required') 
        
        try: 
            media = Media.objects.create(**validated_data)
            
            media.genre.set([
                    Genre.objects.get_or_create(name=name_of_genre)[0] for name_of_genre in self.genres
            ])
        except Exception as e:
            raise e

        return media
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.type_of = validated_data.get('type_of', instance.type_of)
        instance.description = validated_data.get('description', instance.description)
        instance.year = validated_data.get('year', instance.year)
        instance.duration = validated_data.get('duration', instance.duration)
        
        if len(self.genres) > 0:
            instance.genre.clear()
            try: 
                instance.genre.clear()
                instance.genre.set([
                        Genre.objects.get_or_create(name=name_of_genre)[0] for name_of_genre in self.genres
                ])
            except Exception as e:
                raise e
        instance.save()

        return instance