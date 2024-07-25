from django.test import TestCase 

from media.serializers import MediaSerializer, GenreSerializer 
from media.models import Media, Genre 

class MediaSerializerTestCase(TestCase):
    def setUp(self):
        genre = [
            Genre.objects.create(name='genre1'),
            Genre.objects.create(name='genre2'),
            Genre.objects.create(name='genre3'),
        ]
        
        self.media = Media.objects.create(
            title = 'Media',
            type_of = 'movie',
            description = 'Description',
            year = 2020,
            duration = 120, 
            ) 
        
        self.media.genre.set(genre)
        
        return super().setUp()
        
    def tearDown(self) -> None:
        return super().tearDown()
    
    def test_create_media_serializer(self):
        data = { 
            'title': 'War of the Worlds',
            'type_of': 'movie',
            'description': 'The movie about the war of the worlds',
            'year': 2020,
            'duration': 120, 
            
        }
        
        serializer = MediaSerializer(data=data, genre=['war', 'worlds', 'popular'])
        self.assertTrue(serializer.is_valid())
        media = serializer.save()
    
        self.assertEqual(media.title, 'War of the Worlds')
        self.assertEqual(media.type_of, 'movie')
        self.assertEqual(media.description, 'The movie about the war of the worlds')
        self.assertEqual(media.year, 2020)
        self.assertEqual(media.duration, 120)
        self.assertEqual(media.genre.count(), 3)
        
    def test_update_media_serializer(self):
        data = { 
            'title': 'War of the Worlds',
            'type_of': 'movie',
            'description': 'The movie about the war of the worlds',
            'year': 2020,
            'duration': 120, 
            
        }
        
        serializer = MediaSerializer(instance=self.media, data=data, 
                                     genre=['war', 'worlds', 'popular'])
        self.assertTrue(serializer.is_valid())
        media = serializer.save()
    
        self.assertEqual(media.title, 'War of the Worlds')
        self.assertEqual(media.type_of, 'movie')
        self.assertEqual(media.description, 'The movie about the war of the worlds')
        self.assertEqual(media.year, 2020)
        self.assertEqual(media.duration, 120)
        self.assertEqual(media.genre.count(), 3)