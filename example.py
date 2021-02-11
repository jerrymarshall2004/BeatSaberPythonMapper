#BSPM Example Script
from BSPM import info, level, events, notes, obstacles

#Set the path of the Map Folder
path = ("C:/Program Files (x86)/Steam/steamapps/common/Beat Saber/Beat Saber_Data/CustomWIPLevels/maptest/")

#INFO

#Define variable "mapInfo" as the Info for the Map
mapInfo = info

#Define the attributes of the Map (Not required, default values are provided)
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

#LEVELS

#Define variable "normalStandard" as a level
normalStandard = level.level()

#Define the attributes of normalStandard (Not required, default values are provided)
normalStandard.characteristicName = "Standard"
normalStandard.difficulty = "Normal"
normalStandard.difficultyRank = 3
normalStandard.noteJumpMovementSpeed = 12
normalStandard.noteJumpStartBeatOffset = 0
normalStandard.editorOffset = 0
normalStandard.editorOldOffset = 0
normalStandard.warnings = "Don't Break Ur Arms Lol"
normalStandard.information = "Mapped With Beat Saber Python Mapper"
normalStandard.suggestions = "Technicolor, Chroma"
normalStandard.requirements = ""

#EVENTS

#Define "normalEvents" as a set of events
normalEvents = events.events()

#Add an Event to Normal Events (Time, Type, Value)
normalEvents.append(4, 0, 2)
normalEvents.append(4, 2, 2)
normalEvents.append(4, 3, 2)

#Define "normalEvents" as the events for "normalStandard"
normalStandard.events = normalEvents.events

#NOTES

#Define "normalNotes" as a set of notes
normalNotes = notes.notes()

#Add a Note to Normal Notes (Time, Type, X, Y, Direction)
normalNotes.append(4, 0, 1, 2, 1)
normalNotes.append(4, 1, 2, 2, 1)

#Define "normalNotes" as the notes for "normalStandard"
normalStandard.notes = normalNotes.notes

#OBSTACLES

#Define "normalObstacles" as a set of obstacles
normalObstacles = obstacles.obstacles()

#Add an Obstacle to Normal Obstacles (Time, Type, X, Width, Duration)
normalObstacles.append(0, 0, 0, 1, 4)
normalObstacles.append(0, 0, 3, 1, 4)

#Define "normalObstacles" as the obstacles for "normalStandard"
normalStandard.obstacles = normalObstacles.obstacles

#WRITE

#Write the "normalStandard" file at the pre-defined path
normalStandard.write(path)

#Write the Info file at the pre-defined path
mapInfo.write(path)