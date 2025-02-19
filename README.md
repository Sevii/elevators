# elevators
Simulating elevators


Code Challenge

1. The Elevator

    * Provide code that simulates an elevator. You may use any language (recommend using java or Python).
    * Please upload your code Git Hub for a discussion during your interview with our team.
    * Additionally, document all assumptions and any features that weren't implemented.
    * Please be prepared to discuss the assumptions and features that were not implemented during your interview.



Simulate skyscraper with elevator system in it. 
    Why - This is more interesting
    Goal — simulate how height of building and number of elevators effects travel time through the building
    Stack — Python + Rich, UV, click


What will it do? 
    The simulator is a command line program that runs a elevator transit time simulation and reports results.


Problem Statement 
I’ve often heard that as buildings get taller a higher fraction of their volume has to be used up by elevators to maintain reasonable travel speeds, lets test this in a simulation. 


Entities 
    People
        age, destination, location
    Floors 
        size
    Elevators
        floors, capacity, speed, space requirements 

Assumptions:
    * A floor is 3m tall
    * Buildings are evenly composed of floors, extra height is dropped.
    * Elevators have constant speed, pretend we averaged it
    * Elevators fit 10 people


Questions:
    * Do we simulate only people arriving to work or also leaving occasionally? Hotel California?
    * How do we calculate the volume needed by elevators per floor (Do we need this?)

Notes: 
    * We will start with 1 elevator, once that is working will continue if warrented.


1. Pick / Generate building 
2. User picks number of people and distribution
3. Simulation runs 

Simulation 
    function which generates new people who want to go to floors.
        Do we generate all people ahead of time and put them in queue? 
        More memory efficient to generate as we go

    People with destinations are added to the building
    Elevators move picking people up and dropping them off















Test buildings 

Burj Khalifa
height : 829.8m
elevators: 57
speed 10m/s
stories : 163

The E.V. Haughwout Department Store in New York City
height: 24m
elevators : 1 
speed: 0.2032 m/s
stories: 5

Empire State building (Original buildout)
stories: 102
height 380m
elevators: 58
speed: 3.55m/s




