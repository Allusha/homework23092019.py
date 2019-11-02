from functools import reduce


class WrongArtistError(Exception):
    pass


class Artist:
    def __init__(self, name, country):
        self.name = name
        self.country = country
        self.songs = []
        self.albums = []

    def __repr__(self):
        return self.name

    @property
    def songs_number(self):
        return len(self.songs)

    @property
    def album_number(self):
        return len(self.albums)


class Album:
    def __init__(self, name, year, genre, artist):
        self.name = name
        self.year = year
        self.genre = genre
        self.artist = artist
        self.songs = []
        self.artist.albums.append(self)
        self._duration = 0.0

    @property
    def songs_number(self):
        return len(self.songs)

    @property
    def duration(self):
        return reduce(lambda x, y: x.duration + y.duration, self.songs)

    def __repr__(self):
        return self.name


class Song:
    def __init__(self, name, artist, features, year, duration, album=None):
        self.name = name
        self.artist = artist
        self.features = features
        self.year = year
        self.duration = duration
        self.album = album
        self.artist.songs.append(self)

        if self.album.artist == self.artist:
            self.album.songs.append(self)
        else:
            raise WrongArtistError("Wrong artist")

    def __repr__(self):
        return self.name
