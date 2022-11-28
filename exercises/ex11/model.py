"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random, randint
from exercises.ex11 import constants
from math import sin, cos, pi, sqrt


__author__ = "730470219"


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)
    
    def distance(self, other: Point) -> float:
        return sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    # Part 1) Define a method named `tick` with no parameters.
    # Its purpose is to reassign the object's location attribute
    # the result of adding the self object's location with its
    # direction. Hint: Look at the add method.
    def tick(self) -> None:
        self.location = self.location.add(self.direction)
        if self.is_infected():
            self.sickness += 1
        if self.sickness > constants.RECOVERY_PERIOD:
            self.immunize()
        
    def color(self) -> str:
        """Return the color representation of a cell."""
        if self.is_vulnerable():
            return "light slate gray"
        if self.is_infected():
            return "crimson"
        return "royal blue"
    
    def contract_disease(self) -> None:
        self.sickness = constants.INFECTED
    
    def immunize(self) -> None:
        self.sickness = constants.IMMUNE
    
    def is_vulnerable(self) -> bool:
        if self.sickness == constants.VULNERABLE:
            return True
        return False

    def is_infected(self) -> bool:
        if self.sickness >= constants.INFECTED:
            return True
        return False
    
    def is_immune(self) -> bool:
        if self.sickness == constants.IMMUNE:
            return True
        return False

    def contact_with(self, other: Cell) -> None:
        if randint(1, 100) <= constants.INFECTION_PROBABILITY:
            if self.is_infected() and other.is_vulnerable():
                other.contract_disease()
            if self.is_vulnerable() and other.is_infected():
                self.contract_disease()
    
    def contact_mechanism(self, cell: Cell) -> None:
        """self.direction.x *= -1.0
        self.direction.y *= -1.0
        cell.direction.x *= -1.0
        cell.direction.y *= -1.0"""
            

class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, infected: int, immune: int = 0):
        """Initialize the cells with random locations and directions."""
        self.population = []
        if infected <= 0:
            raise ValueError("Must start with at least 1 infected cell")
        for i in range(cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            if infected > 0:
                cell.contract_disease()
                infected -= 1
            elif immune > 0:
                cell.immunize()
                immune -= 1
            self.population.append(cell)

    
    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0
        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0

    def check_contacts(self) -> None:
        i: int = 0
        while i < len(self.population):
            j: int = i + 1
            while j < len(self.population):
                if self.population[i].location.distance(self.population[j].location) < constants.CELL_RADIUS:
                    self.population[i].contact_with(self.population[j])
                    self.population[i].contact_mechanism(self.population[j])
                j += 1
            i += 1

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        for i in self.population:
            if i.is_infected():
                return False
        return True

    def calc_demo(self) -> None:
        inf: int = 0
        imm: int = 0
        for i in self.population:
            if i.is_infected():
                inf += 1
            elif i.is_immune():
                imm += 1
        vul: int = len(self.population) - inf - imm
        print(f"Total Vulnerable: {vul} | Total Infected: {inf} | Total Immune: {imm}")

            
