from song import Song


class Album:
    def __init__(self, name: str, *songs):
        self.name = name
        self.songs = list(songs) or []
        self.published = False

    def add_song(self, song: Song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return "Cannot add songs. Album is published."
        if song in self.songs:
            return "Song is already in the album."
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if self.published:
            return "Cannot remove songs. Album is published."
        for song_instance in self.songs:
            if song_name == song_instance.username:
                self.songs.remove(song_instance)
                return f"Removed song {song_name} from album {self.name}."
        return "Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        info = [f"Album {self.name}"]
        [info.append(f"== {song_obj.get_info()}") for song_obj in self.songs]
        return "\n".join(info)
