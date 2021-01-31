from . import info
from . import notes

global characteristicName
global difficulty
global difficultyRank
global beatmapFilename
global noteJumpMovementSpeed
global noteJumpStartBeatOffset
global editorOffset
global editorOldOffset
global warnings
global information
global suggestions
global requirements
global events
global notes
global obstacles

characteristicName = "Standard"
difficulty = "Normal"
difficultyRank = 3
beatmapFilename = "NormalStandard"
noteJumpMovementSpeed = 12
noteJumpStartBeatOffset = 0
editorOffset = 0
editorOldOffset = 0
warnings = ''
information = ''
suggestions = ''
requirements = ''
events = ''
notes = ''
obstacles = ''

def listToText(events, notes, obstacles):
    global eventText
    global noteText
    global obstacleText
    eventText = ''
    noteText = ''
    obstacleText = ''
    for note in notes:
            noteText+=(note)
    for event in events:
            eventText+=(event)
    for obstacle in obstacles:
            obstacleText+=(obstacle)

def writeFile(difficulty, characteristicName, path, events, notes, obstacles):
    listToText(events, notes, obstacles)
    difficultyText = '{"_version":"3.2.0","_customData":{"_time":0,"_BPMChanges":[],"_bookmarks":[]},"_events":[' + eventText + '],"_notes":[' + noteText + '],"_obstacles":[' + obstacleText + '],"_waypoints":[]}'
    difficultyFile = open(path + difficulty + characteristicName + '.dat', "w")
    difficultyFile.write (difficultyText)

def write(path):
    writeFile(difficulty, characteristicName, path, events, notes, obstacles)
    info.defineBeatmapSets(characteristicName, difficulty, difficultyRank, beatmapFilename, noteJumpMovementSpeed, noteJumpStartBeatOffset, editorOffset, editorOldOffset, warnings, information, suggestions, requirements)

class level:
    def __init__(self):
        global characteristicName
        global difficulty
        global difficultyRank
        global beatmapFilename
        global noteJumpMovementSpeed
        global noteJumpStartBeatOffset
        global editorOffset
        global editorOldOffset
        global warnings
        global information
        global suggestions
        global requirements
        global events
        global notes
        global obstacles
        self.characteristicName = characteristicName
        self.difficulty = difficulty
        self.difficultyRank = difficultyRank
        self.beatmapFilename = beatmapFilename
        self.noteJumpMovementSpeed = noteJumpMovementSpeed
        self.noteJumpStartBeatOffset = noteJumpStartBeatOffset
        self.editorOffset = editorOffset
        self.editorOldOffset = editorOldOffset
        self.warnings = warnings
        self.information = information
        self.suggestions = suggestions
        self.requirements = requirements
        self.events = events
        self.notes = notes
        self.obstacles = obstacles
