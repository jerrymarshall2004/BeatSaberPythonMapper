class notes:
    def __init__(self):
        notes = list()
        self.notes = notes

    def append(self, Time, Type, X, Y, Direction):
            global notes
            self.notes.append('{"_time":' + str(Time) + ',"_lineIndex":' + str(X) + ',"_lineLayer":' + str(Y) + ',"_type":' + str(Type) + ',"_cutDirection":' + str(Direction) + '},')