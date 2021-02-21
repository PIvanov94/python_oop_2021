class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name):
        albums_list = [a for a in self.albums if a.name == album_name]
        if albums_list:
            album = albums_list[0]
            if album.published:
                return "Album has been published. It cannot be removed."
            self.albums.remove(album)
            return f"Album {album.name} has been removed."
        return f"Album {album_name} is not found."

    def details(self):
        data = f"Band {self.name}\n"
        for album in self.albums:
            data += f"{album.details()}\n"
        return data