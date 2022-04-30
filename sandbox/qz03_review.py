from __future__ import annotations

class Course:
    """Models the idea of a UNC course."""
    name: str
    level: int
    prerequisites: list[str]

    def __init__(self, name: str, level: int, prerequisites: list[str]) -> None:
        self.name = name
        self.level = level
        self.prerequisites = prerequisites

    def is_valid_course(self, prereq: str) -> bool:
        if self.level < 400:
            return False
        else:
            for p in self.prerequisites:
                if prereq == p:
                    return True
            return False

def find_courses(courses: list[Course], prereq: str) -> list[str]:
    result: list[str] = []
    for course in courses:
        if course.level > 400:
            for p in course.prerequisites:
                if p == prereq:
                    result.append(course.name)
    return result


class ChristmasTreeFarm:
    plots: list[int]

    def __init__(self, plots: int, initial_planting: int) -> None:
        self.plots = []
        i: int = 0
        while i < initial_planting:
            self.plots.append(1)
            i += 1
        while i < plots:
            self.plots.append(0)
            i += 1
    
    def plant(self, plot_index: int) -> None:
        self.plots[plot_index] = 1
    
    def growth(self) -> None:
        for plot in self.plots:
            if plot > 0:
                plot += 1

    def harvest(self, replant: bool) -> int:
        count: int = 0
        for plot in self.plots:
            if plot >= 5:
                if replant:
                    plot = 1
                else:
                    plot = 0
                count += 1
        return count
    
    def __add__(self, other: ChristmasTreeFarm) -> ChristmasTreeFarm:
        size: int = len(self.plots) + len(other.plots)
        initial_plantings: int = 0
        for plot in self.plots:
            if plot > 0:
                initial_plantings += 1
        for plot in other.plots:
            if plot > 0:
                initial_plantings += 1
        return ChristmasTreeFarm(size, initial_plantings)

