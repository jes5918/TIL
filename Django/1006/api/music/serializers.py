from rest_framework import serializers
from .models import Music, Artist


class ArtistListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Artist
        fields = ('id', 'name',)
        
        
class MusicListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Music
        fields = ('id', 'title',)
        
        
class ArtistSerializer(serializers.ModelSerializer):
    
    music_set = MusicListSerializer(
        many=True,
        read_only=True,
    )
    
    music_count = serializers.IntegerField(
        source='music_set.count',
        read_only=True,
    )
    
    class Meta:
        model = ArtistListSerializer
        fields = ('id', 'name', 'music_set', 'music_count',)
        
        
class MusicSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MusicListSerializer
        fields = ('id', 'title', 'artist',)