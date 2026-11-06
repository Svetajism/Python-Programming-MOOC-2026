class Series:
    def __init__(self, title: str, seasons: int, genres: list):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.rates = []

    def __str__(self):
        genres_str = ", ".join(self.genres)
        if len(self.rates) > 0:
            total = len(self.rates)
            avg = sum(self.rates) / len(self.rates)
            to_print = f"{total} ratings, average {avg:.1f} points"
        else:
            to_print = "no ratings"
        
        return (
            f"{self.title} ({self.seasons} seasons)\n"
            f"genres: {genres_str}\n"
            f"{to_print}"
        )

    def rate(self, rating: int):
        self.rates.append(rating)


def minimum_grade(rating: float, series_list: list) -> list:
    search_result = []
    for series in series_list:
        rate = sum(series.rates) / len(series.rates)
        if rate >= rating:
            search_result.append(series)
    return search_result

def includes_genre(genre: str, series_list: list) -> list:
    search_result = []
    for series in series_list:
        if genre in series.genres:
            search_result.append(series)
    return search_result
    


# Test
if __name__ == "__main__":
    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]


    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)