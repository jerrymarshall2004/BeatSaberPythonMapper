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

### Making a new Map
```python
#Define variable "mapInfo" as the Info for the Map
mapInfo = info
```

### Making a new Level/Difficulty
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

## Adding Metadata
Default Metadata is provided in the package but alot of elements should be changed to fit your map, this can be done easily with the following code.

### Map Wide Metadata

```python
#Define the metadata of the Map
mapInfo.version = "3.2.0"
mapInfo.songName = "Faded"
mapInfo.songSubName = "Where Are You Now"
mapInfo.songAuthorName = "Alan Walker"
mapInfo.levelAuthorName = "Jerry marshall"
mapInfo.beatsPerMinute = 90
mapInfo.shuffle = 0
mapInfo.shufflePeriod = 0.5
mapInfo.previewStartTime = 12
mapInfo.previewDuration = 10
mapInfo.songFilename = "song.ogg"
mapInfo.coverImageFilename = "cover.jpg"
mapInfo.environmentName = "DefaultEnvironment"
mapInfo.songTimeOffset = 0
mapInfo.contributors = ""
```

### Per Level/Difficulty Metadata
```python
#Define the metadata of normalStandard
normalStandard.characteristicName = "Standard"
normalStandard.difficulty = "Normal"
normalStandard.difficultyRank = 3
normalStandard.noteJumpMovementSpeed = 12
normalStandard.noteJumpStartBeatOffset = 0
normalStandard.editorOffset = 0
normalStandard.editorOldOffset = 0
normalStandard.warnings = "Don't Break Ur Arms lol"
normalStandard.information = "Mapped With Beat Saber Python Mapper"
normalStandard.suggestions = "Technicolor, Chroma"
normalStandard.requirements = ""
```
