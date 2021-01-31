# Beat Saber Python Mapper

A Simple Python Package that allows developers to make Beat Saber maps in Python!

## Installation

```cmd
pip install BSPM
```

## The Basics

### Import the required Packages

```python
from BSPM import info, level, events, notes, obstacles
```

### Set the desired path for your map folder

```python
path = ("C:/Program Files (x86)/Steam/steamapps/common/Beat Saber/Beat Saber_Data/CustomWIPLevels/Example Map/")
```

### Making a new map
```python
#Define variable "mapInfo" as the Info for the Map
mapInfo = info
```

### Making a new difficulty
```python
#Define variable "normalStandard" as a level
normalStandard = level
```

### Adding Events

```python
#Define "normalEvents" as a set of events
normalEvents = events.events()

#Add an Event to Normal Events (Time, Type, Value)
normalEvents.append(4, 0, 2)
normalEvents.append(4, 2, 2)
normalEvents.append(4, 3, 2)

#Define "normalEvents" as the events for "normalStandard"
normalStandard.events = normalEvents.events
```

### Adding Notes

```python
#Define "normalNotes" as a set of notes
normalNotes = notes.notes()

#Add a Note to Normal Notes (Time, Type, X, Y, Direction)
normalNotes.append(4, 0, 1, 2, 1)
normalNotes.append(4, 1, 2, 2, 1)

#Define "normalNotes" as the notes for "normalStandard"
normalStandard.notes = normalNotes.notes
```

### Adding Obstacles

```python
#Define "normalObstacles" as a set of obstacles
normalObstacles = obstacles.obstacles()

#Add an Obstacle to Normal Obstacles (Time, Type, X, Width, Duration)
normalObstacles.append(0, 0, 0, 1, 4)
normalObstacles.append(0, 0, 3, 1, 4)

#Define "normalObstacles" as the obstacles for "normalStandard"
normalStandard.obstacles = normalObstacles.obstacles
```

### Writing the Files

```python
#Write the "normalStandard" file at the pre-defined path
normalStandard.write(path)

#Write the Info file at the pre-defined path
mapInfo.write(path)
```
