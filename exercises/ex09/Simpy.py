"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730470219"


class Simpy:
    """Creation of a new class."""
    values: list[float]

    def __init__(self, values: list[float]) -> None:
        """Constructor method."""
        self.values = values

    def __str__(self) -> str:
        """Method for printing the str literal."""
        return f"Simpy({self.values})"

    def fill(self, num: float, repeats: int) -> None:
        """Method for creating copys of a value."""
        self.values = []
        for i in range(0, repeats):
            self.values.append(num)

    def arange(self, start: float, stop: float, step: float = 1) -> None:
        """Method for creating a range of incrementing values."""
        self.values = []
        assert step != 0
        while abs(start) < abs(stop):
            self.values.append(start)
            start += step
    
    def sum(self) -> float:
        """Method for calculating the sum."""
        return sum(self.values)

    def __add__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Overloading the addition operator."""
        result: list[float] = []
        if isinstance(rhs, float):
            for item in self.values:
                result.append(item + rhs)
        if isinstance(rhs, Simpy):
            for i in range(0, len(self.values)):
                result.append(self.values[i] + rhs.values[i])
        return Simpy(result)

    def __pow__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Overloading the power operator."""
        result: list[float] = []
        if isinstance(rhs, float):
            for item in self.values:
                result.append(item ** rhs)
        if isinstance(rhs, Simpy):
            for i in range(0, len(self.values)):
                result.append(self.values[i] ** rhs.values[i])
        return Simpy(result)

    def __eq__(self, rhs: Union[Simpy, float]) -> list[bool]:
        """Overloading the equal operator."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for item in self.values:
                result.append(item == rhs)
        if isinstance(rhs, Simpy):
            for i in range(0, len(self.values)):
                result.append(self.values[i] == rhs.values[i])
        return result

    def __gt__(self, rhs: Union[Simpy, float]) -> list[bool]:
        """Overloading the greater than operator."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for item in self.values:
                result.append(item > rhs)
        if isinstance(rhs, Simpy):
            for i in range(0, len(self.values)):
                result.append(self.values[i] > rhs.values[i])
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Overloading the subscription notation operator."""
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            print(rhs)
            result: list[float] = []
            for i in range(0, len(self.values)):
                if rhs[i]:
                    result.append(self.values[i])
            return Simpy(result)