class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for page in range(self.pages)]
        self.max_photos_in_page = 4

    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(int(photos_count / 4))

    def add_photo(self, label):
        for page in range(len(self.photos)):
            if len(self.photos[page]) < 4:
                self.photos[page].append(label)
                return f"{label} photo added successfully on page {page + 1} slot {len(self.photos[page])}"
        return "No more free spots"

    def display(self):
        result = ""
        for row in self.photos:
            result += f"-----------\n"
            if len(row) > 0:
                result += f"{' '.join('[]' for el in row)}\n"
            else:
                result += "\n"
        result += f"-----------\n"
        return result
