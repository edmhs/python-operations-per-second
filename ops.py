import time

class OPS:

    def __init__(self):
        self.seconds = {}
        pass

    def add(self):
        sec = int(round(time.time() ))

        if sec in self.seconds:
            self.seconds[sec] = self.seconds[sec]+1
        else:
            self.seconds[sec] = 1

    def print(self):
        print(self.seconds)