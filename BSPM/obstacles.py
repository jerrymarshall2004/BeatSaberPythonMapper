class obstacles:
    def __init__(self):
        obstacles = list()
        self.obstacles = obstacles

    def append(self, Time, Type, X, Width, Duration):
            global obstacles
            self.obstacles.append('{"_time":' + str(Time) + ',"_lineIndex":' + str(X) + ',"_type":' + str(Type) + ',"_duration":' + str(Duration) + ',"_width":' + str(Width) + '},')