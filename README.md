# python-operations-per-second
Simple operations per second counter class

#### code
~~~
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
~~~

#### Usage
~~~
o = OPS()

while [do something]:
    o.add()
    //some activity

o.print()
//prints {1544912424: 769, 1544912425: 2648, 1544912426: 2578, 1544912427: 2599, 1544912428: 1406}

~~~