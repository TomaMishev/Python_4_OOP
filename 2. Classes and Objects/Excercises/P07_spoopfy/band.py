from Excercises.P07_spoopfy.album import Album
from Excercises.P07_spoopfy.song import Song


class Band:

    def __init__(self, name: str):
        self.name = name
        self.albums = list()

    def add_album(self, album: Album):
        for current_album in self.albums:
            if current_album.name == album.name:
                return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        for current_album in self.albums:
            if current_album.name == album_name and current_album.published:
                return f"Album has been published. It cannot be removed."
            elif current_album.name == album_name:
                self.albums.remove(current_album)
                return f"Album {album_name} has been removed."
        return f"Album {album_name} is not found."

    def details(self):
        result = f"Band {self.name}\n"
        for current_album in self.albums:
            result += f"{current_album.details()}\n"
        return result


song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())
band = Band("Manuel")
print(band.add_album(album))
print(band.remove_album("Initial D"))
print(band.details())
