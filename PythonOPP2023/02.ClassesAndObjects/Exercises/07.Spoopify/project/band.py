from album import Album
from song import Song


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album_to_add: Album):
        if album_to_add not in self.albums:
            self.albums.append(album_to_add)
            return f"Band {self.name} has added their newest album {album_to_add.name}."
        return f"Band {self.name} already has {album_to_add.name} in their library."

    def remove_album(self, album_name: str):
        for album_instance in self.albums:
            if album_instance.username == album_name:
                if album_instance.published:
                    return "Album has been published. It cannot be removed."
                self.albums.remove(album_instance)
                return f"Album {album_name} has been removed."
        return f"Album {album_name} is not found."

    def details(self):
        info_band = [f"Band {self.name}"]
        [info_band.append(album_obj.details()) for album_obj in self.albums]
        return "\n".join(info_band)


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
