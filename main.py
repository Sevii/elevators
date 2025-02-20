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
import math
import statistics

@dataclass
class Building():
    floors: int
    

@dataclass
class Person():
    age: int # in turns aka minutes for now
    destination: int # destination floor
    location: int # current location floor, negative means inside the elevator
    elevator: int
    inElevator: bool = False
    arrived: bool = False


@dataclass
class Elevator():
    id: int 
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
    while(destination == location):
        destination = random.randint(0, building.floors)
        location = random.randint(0, building.floors)

    return Person(
        age=0,  # Start at age 0 since they just entered the simulation
        destination=destination,
        location=location,
        elevator = None
    )


@click.command()
@click.option('--minutes', default=50, help='Number of minutes')
@click.option('--floors', default=20, help='Number of floors')
def main(minutes, floors):
    elevator = Elevator(id=0, location=0, floors_list = [range(floors)])
    building = Building(floors = floors)
    print(elevator)

    # generate starter people
    people = [generatePerson(building) for _ in range(5)]
    totalPeople = len(people)

    for lp in range(minutes):
        print("Starting turn {} ".format(lp))

        #generate people
        # for p in [generatePerson(building) for _ in range(2)]:
        #     people.append(p)
        #     totalPeople = totalPeople + 1

        

        # Elevator

        inhabitants = list(filter(lambda person: person.elevator == elevator.id and not person.arrived, people))

        if len(inhabitants) == 0 or elevator.has_destination == False:
            #find oldest person
            activePeople = list(filter(lambda person: not person.arrived, people))
            if len(activePeople) > 0:
                oldest = max(activePeople, key=lambda x: x.age)
                print(oldest)
                if oldest.inElevator:
                    elevator.destination = oldest.destination
                else:
                    elevator.destination = oldest.location
                elevator.has_destination = True
                elevator.caller = oldest
            else:
                print("No people left! {} ".format(len(activePeople)))

        # Elevator moves towards its destination
        # if any people are on a floor it passes it can pick them up if their destination is on the way
        # If the elevator stops it should end its turn

        elevator_continue = True
        floors_moved = 0
        while(elevator_continue):
            print("Elevator looping destination {} ".format(elevator.destination))
            print("Elevator on floor {} ".format(elevator.location))
            if elevator.destination == elevator.location:
                elevator_continue = False
                elevator.has_destination = False

            if elevator.destination > elevator.location:
                print("Elevator is going up!")
                elevator.location = elevator.location +1
                floors_moved = floors_moved +1
            elif elevator.destination < elevator.location:
                print("Elevator is going down!")
                elevator.location = elevator.location -1
                floors_moved = floors_moved +1
            else:
                floors_moved = floors_moved +1

            if floors_moved > 5:
                break

            inhabitants = list(filter(lambda person: person.elevator == elevator.id and not person.arrived, people))
            print("inhabitants count {} ".format(len(inhabitants)))
            # If the elevator has room for more people it can stop to pick them up
            # In the real world, elevators don't seem to track capacity annoying people inside
            if len(inhabitants) < elevator.capacity:
                floor_people = list(filter(lambda person: person.location == elevator.location and not person.arrived and not person.inElevator, people))
                print("floor people count {} ".format(len(floor_people)))
                if len(floor_people) > 0:
                    # people are on this floor
                    # if they are going in the same direction we can pick them up
                    for p in floor_people:
                        if p.destination > p.location:
                            #going up
                            if elevator.destination > elevator.location or not elevator.has_destination:
                                #elevator also going up, add person to elevator
                                p.elevator = elevator.id
                                p.inElevator = True
                                print("Picked someone up!")
                        if p.destination < p.location:
                            #going down
                            if elevator.destination < elevator.location or not elevator.has_destination:
                                #elevator also going down, add person to elevator
                                p.elevator = elevator.id
                                p.inElevator = True
                                print("Picked someone up!")


            # the elevator can drop people off, if it does it will stop for one minutes (aka a turn)
            if len(inhabitants) > 0:
                shouldStop = False
                for person in inhabitants:
                    if person.destination == elevator.location:
                        print("Dropped someone off!")
                        shouldStop = True
                        person.inElevator = False
                        print("Dropped someone off!")
                        person.arrived = True
                elevator_continue = False
                break;



        #end turn
        #increase the age of each person
        for person in people:
            if person.arrived == False:
                person.age = person.age +1
        # print(people)

    print("Simulation finished -------------------------------------------------")    
    print("Floors in sim: {}".format(floors))
    print("Total people {} ".format(totalPeople))

    peopleStillInTransit = list(filter(lambda person: not person.arrived, people))   
    peopleDelivered = list(filter(lambda person: person.arrived, people))    
    peopleDeliveredCount = len(people) - len(peopleStillInTransit)
    ages = list(map(lambda x: x.age, peopleStillInTransit))
    deliveredAges = list(map(lambda x: x.age, peopleDelivered))
    print("People delivered {} ".format(peopleDeliveredCount))
    if len(ages) > 0:
        print("Average age of undelivered people {} ".format(statistics.mean(ages)))
    if len(deliveredAges) > 0:
        print("Average age of delivered people {} ".format(statistics.mean(deliveredAges)))

    print("Undelivered people {} ".format(ages))
    print("Mean age of people still in transit {} ".format(ages))
    print("People still in transit {} ".format(len(ages)))
    print("Total people {} ".format(totalPeople))
    





if __name__ == "__main__":
    main()
