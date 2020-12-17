from hw22.models import MusicBand, Album, Track


def all_albums_band(band_name):
    band = MusicBand.objects.filter(band_name=band_name).first()
    albums_band = band.albums.all()
    return albums_band


def all_tracks_album(album_name):
    album = Album.objects.filter(album_name=album_name).first()
    tracks_album = album.tracks.all()
    return tracks_album


def all_tracks_band(band_name):
    band = MusicBand.objects.filter(band_name=band_name).first()
    albums = band.albums.all()
    tracks = [album.tracks.all() for album in albums]
    return tracks


def all_albums_bands_1990():
    bands = MusicBand.objects.filter(year=1990)
    albums = [band.albums.all() for band in bands]
    return albums
