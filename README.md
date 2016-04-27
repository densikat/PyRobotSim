# PyRobotSim

Simulation of toy robot moving on a square tabletop

A robot is placed on a 5x5 tabletop. Instructions are issued to the robot via user input or via a text input file

This is a Python implementation of my initial Java based [Robot Simulator](https://github.com/densikat/Robot-Simulator)

I chose Python to get some experience with a dynamic language. For now this version only has an interactive mode.

## Environments

Initially developed on

* Windows 10
* Python 3.5.1 (Only tested on this version)

## System dependencies and configuration

* Python 3.5.1 or greater

## Successfully tested on following platforms

* Windows 10
* Ubuntu 16.04

## Usage Instructions

Load command prompt/shell and change to working directory of robotsim class files

To run application on Linux:

	$ python3 Simulator.py

To run application on Windows (Python 3 location must be on PATH variable):

	$ python Simulator.py
	
## Valid commands

Note: Commands for interactive and input file are identical

#####PLACE X,Y,DIRECTION

**Purpose:** Places robot on tabletop. Only valid if robot is not on board already, will be discard otherwise.

X = X coordinate on tabletop to place robot. Valid inputs: 0-4
Y = Y coordinate on tabletop to place robot. Valid inputs: 0-4
DIRECTION = Direction for robot to face. Valid inputs are NORTH, SOUTH, EAST, WEST

#####MOVE

**Purpose:** Move robot one unit forward in the direction it is currently facing.

Only valid if movement does not take robot off the tabletop edge.

#####LEFT

**Purpose:** Rotate the robot 90 degrees to the left

_example_ Robot is facing north, LEFT is issued, robot is now facing WEST

#####RIGHT

**Purpose:** Rotate the robot 90 degrees to the right

_example_ Robot is facing north, RIGHT is issued, robot is now facing EAST

#####REPORT

**Purpose:** Reports the location of the robot and direction the robot is facing

_example_

REPORT
3,3,NORTH

#####EXIT

**Purpose:** Exit the game


## Running tests

1. Browse to source root
2. Run the following to execute tests (Linux)

	```
	$ python3 -m unittest Tests/*.py
	```

## Structure

Code is comprised of four main source files

**Simulator.py**

_Runs the simulator_

Class does the following:

    Takes and checks command line arguments passed to the program
	Initializes robot and table
    Runs in interactive loop, takes commands from command line
    Takes each command sequentially and processes them
    
**Robot.py**

_Class representation of a robot_

Does the following:
    
    Takes a command and validates it against a given table
    Executes a command against a given table

**Table.py**

_Class representation of Table Top_

Does the following:

    Initializes a table top with specific X and Y upper bounds

**Direction.py**

_Direction class, uses hashtable internally to represent directions_

_This class was implemented to provide a way to arithmetically (via hashtable index) achieve rotation instructions_

Does the following:

    Returns string representation of direction based on hashtable index.
    
**Commands\Command.py**

_Class representation of a command, all command objects game are derived off this abstract class_

Does the following:

    Takes a command string, parses string, if valid populates command instance fields

**Commands\CommandFactory.py**

_Factory class that produces command objects_

Does the following:

    Produces objects based on Command class. This is based on user input command from console.

## Todo

* Increase test coverage

## License

This project is licensed under the [MIT License](http://www.opensource.org/licenses/MIT)
