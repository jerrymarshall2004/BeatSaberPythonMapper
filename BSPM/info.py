import os.path
from os import path

standardBeatmaps = ''
noArrowsBeatmaps = ''
oneSaberBeatmaps = ''

global version
global songName
global songSubName
global songAuthorName
global levelAuthorName
global beatsPerMinute
global shuffle
global shufflePeriod
global previewStartTime
global previewDuration
global songFilename
global coverImageFilename
global environmentName
global songTimeOffset
global contributors

#Pre Defined Values
version = "3.2.0"
songName = 'Unknown'
songSubName = ''
songAuthorName = 'Unknown'
levelAuthorName = 'Unknown'
beatsPerMinute = 120
shuffle = 0
shufflePeriod = 0.5
previewStartTime = 12
previewDuration = 10
songFilename = 'song.ogg'
coverImageFilename = 'cover.jpg'
environmentName = 'DefaultEnvironment'
songTimeOffset = 0
contributors = ''

def defineBeatmapSets(characteristicName, difficulty, difficultyRank, beatmapFilename, noteJumpMovementSpeed, noteJumpStartBeatOffset, editorOffset, editorOldOffset, warnings, information, suggestions, requirements):
    if not warnings == "":
        warnings = ('"' + warnings + '"')
    if not information == "":
        information = ('"' + information + '"')
    if not suggestions == "":
        suggestions = ('"' + suggestions + '"')
    if not requirements == "":
        requirements = ('"' + requirements + '"')
    if characteristicName == "Standard":
        global standardBeatmaps
        standardBeatmaps+='{"_difficulty":"' + difficulty + '","_difficultyRank":' + str(difficultyRank) + ',"_beatmapFilename":"' + difficulty + characteristicName + '.dat","_noteJumpMovementSpeed":' + str(noteJumpMovementSpeed) + ',"_noteJumpStartBeatOffset":' + str(noteJumpStartBeatOffset) + ',"_customData":{"_editorOffset":' + str(editorOffset) + ',"_editorOldOffset":' + str(editorOldOffset) + ',"_warnings":[' + warnings + '],"_information":[' + information + '],"_suggestions":[' + suggestions + '],"_requirements":[' + requirements + ']}},'
    if characteristicName == "NoArrows":
        global noArrowsBeatmaps
        noArrowsBeatmaps+='{"_difficulty":"' + difficulty + '","_difficultyRank":' + str(difficultyRank) + ',"_beatmapFilename":"' + difficulty + characteristicName + '.dat","_noteJumpMovementSpeed":' + str(noteJumpMovementSpeed) + ',"_noteJumpStartBeatOffset":' + str(noteJumpStartBeatOffset) + ',"_customData":{"_editorOffset":' + str(editorOffset) + ',"_editorOldOffset":' + str(editorOldOffset) + ',"_warnings":[' + warnings + '],"_information":[' + information + '],"_suggestions":[' + suggestions + '],"_requirements":[' + requirements + ']}},'
    if characteristicName == "OneSaber":
        global oneSaberBeatmaps
        oneSaberBeatmaps+='{"_difficulty":"' + difficulty + '","_difficultyRank":' + str(difficultyRank) + ',"_beatmapFilename":"' + difficulty + characteristicName + '.dat","_noteJumpMovementSpeed":' + str(noteJumpMovementSpeed) + ',"_noteJumpStartBeatOffset":' + str(noteJumpStartBeatOffset) + ',"_customData":{"_editorOffset":' + str(editorOffset) + ',"_editorOldOffset":' + str(editorOldOffset) + ',"_warnings":[' + warnings + '],"_information":[' + information + '],"_suggestions":[' + suggestions + '],"_requirements":[' + requirements + ']}},'

def write(path):
    if standardBeatmaps !='':
        standardBeatmapsText = '{"_beatmapCharacteristicName":"Standard","_difficultyBeatmaps":[' + standardBeatmaps + ']},'
    else:
        standardBeatmapsText = ''
    if noArrowsBeatmaps !='':
        noArrowsBeatmapsText = '{"_beatmapCharacteristicName":"NoArrows","_difficultyBeatmaps":[' + noArrowsBeatmaps + ']},'
    else:
        noArrowsBeatmapsText = ''
    if oneSaberBeatmaps !='':
        oneSaberBeatmapsText = '{"_beatmapCharacteristicName":"OneSaber","_difficultyBeatmaps":[' + oneSaberBeatmaps + ']},'
    else:
        oneSaberBeatmapsText = ''
    difficultyBeatmapSets = (standardBeatmapsText + noArrowsBeatmapsText + oneSaberBeatmapsText)
    infoText = '{"_version":"' + version + '","_songName":"' + songName + '","_songSubName":"' + songSubName + '","_songAuthorName":"' + songAuthorName + '","_levelAuthorName":"' + levelAuthorName + '","_beatsPerMinute":' + str(beatsPerMinute) + ',"_shuffle":' + str(shuffle) + ',"_shufflePeriod":' + str(shufflePeriod) + ',"_previewStartTime":' + str(previewStartTime) + ',"_previewDuration":' + str(previewDuration) + ',"_songFilename":"' + songFilename + '","_coverImageFilename":"' + coverImageFilename + '","_environmentName":"' + environmentName + '","_songTimeOffset":' + str(songTimeOffset) + ',"_customData":{"_contributors":[' + contributors + '],"_editors":{"BSPM":{"version":"1.0.0"},"_lastEditedBy":"BSPM"}},"_difficultyBeatmapSets":[' + difficultyBeatmapSets + ']}'
    infoFile = open(path + 'Info.dat', "w")
    infoFile.write (infoText.replace("]}},]},]}", "]}}]}]}"))
    