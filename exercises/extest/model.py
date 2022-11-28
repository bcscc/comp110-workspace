"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random, randint
from exercises.extest import constants
from math import sin, cos, pi, sqrt, acos


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
        
    def color(self) -> str:
        """Return the color representation of a cell."""
        return "light slate gray"
    
    def contact_mechanism(self, cell: Cell) -> None:
        distX: float = self.location.x - cell.location.x
        distY: float = self.location.y - cell.location.y
        dotprod: float = (distX*self.direction.x+distY*self.direction.y)/(distX*distX+distY*distY)
        newAngle: float = acos(dotprod*sqrt((distX*distX+distY*distY)/(self.direction.x*self.direction.x+self.direction.y*self.direction.y)))
        self.direction.x += sin(newAngle)*(2*distX*dotprod)
        self.direction.y += cos(newAngle)*(2*distY*dotprod)
        """self.direction.x *= -1.0
        self.direction.y *= -1.0
        cell.direction.x *= -1.0
        cell.direction.y *= -1.0"""
            

class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self):
        """Initialize the cells with random locations and directions."""
        self.population = []
        one: Cell = Cell(Point(-200, 0), Point(10, 0))
        self.population.append(one)
        two: Cell = Cell(Point(0, 0), Point(0, 0))
        self.population.append(two)

    
    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

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
                if self.population[i].location.distance(self.population[j].location) <= constants.CELL_RADIUS:
                    self.population[i].contact_mechanism(self.population[j])
                j += 1
            i += 1

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        return False

            
