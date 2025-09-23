# Globals for the directions
# Change the values as you see fit
EAST = 'E'
NORTH = 'N'
WEST = 'W'
SOUTH = 'S'

d = {
     NORTH: EAST,
     SOUTH: WEST,
     WEST: NORTH,
     EAST: SOUTH
    }


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):

        self.first_direction = direction
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.direcs = [direction]


    def _change_direction(self, direction, step):

        if step == 'R':
            return d[direction]
        elif step == 'L':
            for key in d:
                if d[key] == direction:
                    return key


    def move(self, steps):
        self.steps = steps
        for i in self.steps:
            if i == 'R' or i == 'L':
                new_dir = self._change_direction(self.direcs[-1], i)
                self.direcs.append(new_dir) 
            else:
                if self.direcs[-1] == EAST:
                    self.x_pos += 1
                elif self.direcs[-1] == WEST:
                    self.x_pos -= 1
                elif self.direcs[-1] == NORTH:
                    self.y_pos += 1
                elif self.direcs[-1] == SOUTH:
                    self.y_pos -= 1

    @property
    def direction(self):
        return self.direcs[-1]
    
    @property
    def coordinates(self):
        return self.x_pos, self.y_pos