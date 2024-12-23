class Checked:
    ...


class Movie(Checked):
    title: str = "123"
    year: int
    box_office: float

    def name(self):
        ...


print(Movie.__dict__)
