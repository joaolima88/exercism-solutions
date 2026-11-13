class Clock:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute
        self.new_minutes = None
        self.new_hour = None
    
    def time(self):
        self.hour = self.hour + (self.minute // 60)
        self.minute = self.minute % 60

        if self.hour > 24:
            while self.hour > 24:
                self.hour -= 24
        elif self.hour < 0:
            while self.hour < 0:
                self.hour += 24
        
        if self.hour == 24:
            self.hour = 0

        return self.hour, self.minute

    def __repr__(self):
        return f'Clock({self.hour}, {self.minute})'
    
    def __str__(self):
        self.time()
        return f'{'0' * (2-len(str(self.hour)))}{self.hour}:{'0' * (2-len(str(self.minute)))}{self.minute}'

    def __add__(self, minutes):
        self.new_minutes = minutes

        self.new_hour = self.new_minutes // 60
        self.new_minutes = self.new_minutes % 60

        self.time()

        self.hour += self.new_hour
        self.minute += self.new_minutes

        return self

    def __sub__(self, minutes):
        self.new_minutes = minutes

        self.new_hour = self.new_minutes // 60
        self.new_minutes = self.new_minutes % 60

        self.hour -= self.new_hour
        self.minute -= self.new_minutes

        self.time()
        return self

    def __eq__(self, other):
        return str(self.time()) == str(other.time())


