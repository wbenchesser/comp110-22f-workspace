"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt


__author__ = "730564467"


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
    
    def distance(self, p2: Point) -> float:
        """Finds the difference between two points."""
        x2: float = p2.x
        y2: float = p2.y
        xdsqrd: float = (x2 - self.x)**2
        ydsqrd: float = (y2 - self.y)**2
        return sqrt(xdsqrd + ydsqrd)


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    def contract_disease(self) -> None:
        """Assign the INFECTED constant to the sickness attribute of the Cell."""
        self.sickness = constants.INFECTED
    
    def is_vulnerable(self) -> bool:
        """Checks if a cell is vulnerable."""
        if self.sickness is constants.VULNERABLE:
            return True
        else:
            return False

    def is_infected(self) -> bool:
        """Checks if a cell is infected."""
        if self.sickness >= constants.INFECTED:
            return True
        else:
            return False

    def tick(self) -> None:
        """Reassign the object's location attribute."""
        self.location = self.location.add(self.direction)
        if self.is_infected() is True:
            self.sickness += 1
        if self.sickness >= constants.RECOVERY_PERIOD:
            self.immunize()
        
    def color(self) -> str:
        """Return the color representation of a cell."""
        if self.is_infected() is True:
            return "medium violet red"
        if self.is_vulnerable() is True:
            return "gray"
        if self.is_immune() is True:
            return "cyan"
    
    def contact_with(self, other_cell: Cell) -> None:
        """When two cells overlap, if one is vulnerable and one is infected, make the vulnerable cell infected."""
        if self.is_infected() is True and other_cell.is_vulnerable() is True:
            other_cell.contract_disease()
        if self.is_vulnerable() is True and other_cell.is_infected() is True:
            self.contract_disease()

    def immunize(self) -> None:
        """Makes an infected cell immune."""
        self.sickness = constants.IMMUNE

    def is_immune(self) -> bool:
        """Returns True when the cell's sickness attribute is == IMMUNE."""
        if self.sickness == constants.IMMUNE:
            return True
        else:
            return False


class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, in_count: int, im_count: int = 0):
        """Initialize the cells with random locations and directions."""
        if in_count <= 0 or in_count >= cells:
            raise ValueError("Error, some number of the Cell objects must begin infected.")
        if im_count < 0 or im_count >= cells:
            raise ValueError("Error with number of preset immune cells.")
        self.population = []
        for _ in range(im_count):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            cell.sickness = constants.IMMUNE
            self.population.append(cell)
        for _ in range(in_count):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            cell.sickness = constants.INFECTED
            self.population.append(cell)
        for _ in range(cells - in_count):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
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
            cell.direction.x *= -1.0
        if cell.location.x < -(constants.MAX_X):
            cell.direction.x *= -1.0
        if cell.location.y > constants.MAX_Y:
            cell.direction.y *= -1.0
        if cell.location.y < -(constants.MAX_Y):
            cell.direction.y *= -1.0

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        check: bool = True
        for cell in self.population:
            if cell.sickness >= 1:
                check = False
        return check

    def check_contacts(self) -> None:
        """Checks to see if any cells are making contact."""
        for cell1 in range(len(self.population)):
            for cell2 in range(cell1 + 1, len(self.population)):
                if self.population[cell1].location.distance(self.population[cell2].location) < constants.CELL_RADIUS:
                    self.population[cell1].contact_with(self.population[cell2])
