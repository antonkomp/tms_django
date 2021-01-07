from django.db import models


class MusicBand(models.Model):
    band_name = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    style = models.CharField(max_length=50, default=None)

    def __str__(self):
        return f'MusicBand ({self.band_name})'


class Album(models.Model):
    album_name = models.CharField(max_length=100)
    band = models.ForeignKey('MusicBand', null=True, on_delete=models.SET_NULL, related_name='albums')
    year_release = models.PositiveIntegerField()

    def __str__(self):
        return f'Album ({self.album_name})'


class Track(models.Model):
    track_name = models.CharField(max_length=100)
    duration = models.FloatField(default=None)
    album = models.ForeignKey('Album', null=True, on_delete=models.SET_NULL, related_name='tracks')

    def __str__(self):
        return f'Track ({self.track_name})'
