class events:
    def __init__(self):
        events = list()
        self.events = events

    def append(self, Time, Type, Value):
            global events
            self.events.append('{"_time":' + str(Time) + ',"_type":' + str(Type) + ',"_value":' + str(Value) + '},')