import math


class PhotoAlbum:
    MAX_PHOTOS_ON_PAGE = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        # create photo album with number of photos instead of pages, calculates how much pages we need
        return cls(math.ceil(photos_count/cls.MAX_PHOTOS_ON_PAGE))

    def add_photo(self, label: str):
        for number_page, photo_page in enumerate(self.photos):
            if len(self.photos[number_page]) < self.MAX_PHOTOS_ON_PAGE:
                self.photos[number_page].append(label)
                return (f"{label} photo added successfully on page {number_page + 1} "
                        f"slot {len(photo_page)}")
        return f"No more free slots"

    def display(self):
        result = ["-----------"]
        result.extend([f"{' '.join(['[]' for _ in photo_page])}\n-----------" for photo_page in self.photos])
        return '\n'.join(result)


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
