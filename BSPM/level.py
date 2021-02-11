from . import info
from . import notes

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

class level:
    def __init__(self):
        
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

    def write(self, path):
        writeFile(self.difficulty, self.characteristicName, path, self.events, self.notes, self.obstacles)
        info.defineBeatmapSets(self.characteristicName, self.difficulty, self.difficultyRank, self.beatmapFilename, self.noteJumpMovementSpeed, self.noteJumpStartBeatOffset, self.editorOffset, self.editorOldOffset, self.warnings, self.information, self.suggestions, self.requirements)
