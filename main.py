# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "click",
#     "rich",
# ]
# ///

import click
from dataclasses import dataclass, field
from typing import List
import random 

@dataclass
class Building():
    floors: int
    

@dataclass
class Person():
    age: int # in turns aka minutes for now
    destination: int # destination floor
    location: int # current location floor


@dataclass
class Elevator():
    location: int
    destination: int = 0
    speed: float = 3.0
    capacity: int = 10
    floors_list: List[int] = field(default_factory=list)
    has_destination: bool = False
    caller: Person = None


def generatePerson(building: Building) -> Person:
    destination = random.randint(0, building.floors)
    location = random.randint(0, building.floors)
    return Person(
        age=0,  # Start at age 0 since they just entered the simulation
        destination=destination,
        location=location
    )


@click.command()
@click.option('--minutes', default=5, help='Number of minutes')
@click.option('--floors', default=100, help='Number of floors')
def main(minutes, floors):
    elevator = Elevator(location=0, floors_list = [range(floors)])
    building = Building(floors = floors)
    print(elevator)

    # generate starter people
    people = [generatePerson(building) for _ in range(2)]


    for lp in range(minutes):
        print("Starting turn {} ".format(lp))

        #generate people
        for p in [generatePerson(building) for _ in range(2)]:
            people.append(p)

        print(people)

        # Elevator
        if not elevator.has_destination:
            #find oldest person
            oldest = max(people, key=lambda x: x.age)
            print(oldest)
            elevator.destination = oldest.location
            elevator.has_destination = True
            elevator.caller = oldest

        if elevator.destination > elevator.location:
            elevator.location = elevator.location +1
        else if elevator.destination < elevator.location:
            elevator.location = elevator.location -1






        #end turn
        for person in people:
            person.age = person.age +1
        people = list(filter(lambda person: person.location is not person.destination, people))








if __name__ == "__main__":
    main()
