from __future__ import annotations


class Distance:

    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        else:
            raise TypeError("Unsupported type for addition with Distance")

    def __iadd__(self, other: Distance) -> int | float:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            raise TypeError("Unsupported type")
        return self

    def __mul__(self, times: int) -> Distance:
        return Distance(self.km * times)

    def __truediv__(self, divisor: int) -> Distance:
        return Distance(round(self.km / divisor, 2))

    def __lt__(self, other: Distance) -> int | float:
        other_km = other.km if isinstance(other, Distance) else other
        return self.km < other_km

    def __gt__(self, other: Distance) -> int | float:
        other_km = other.km if isinstance(other, Distance) else other
        return self.km > other_km

    def __eq__(self, other: Distance) -> int | float:
        other_km = other.km if isinstance(other, Distance) else other
        return self.km == other_km

    def __le__(self, other: Distance) -> int | float:
        other_km = other.km if isinstance(other, Distance) else other
        return self.km <= other_km

    def __ge__(self, other: Distance) -> int | float:
        other_km = other.km if isinstance(other, Distance) else other
        return self.km >= other_km
