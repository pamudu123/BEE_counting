'''
The Bee class:

The bee's horizontal and vertical speeds are set randomly between specific ranges.
The bee's horizontal direction is randomly set to "LEFT" or "RIGHT," and its vertical direction is randomly set to "IN" or "OUT."
The bee's initial position is determined based on its vertical direction. If moving "OUT," it starts at a random position at the bottom of the background; if moving "IN," it starts at a random position at the top of the background.

Methods:
update_bee_position: Updates the bee's position based on its current directions and speeds.
'''

import random
import args

class Bee:
    def __init__(self, bg_h, bg_w, bee_h, bee_w):
        self.bg_h = bg_h     # Background image height
        self.bg_w = bg_w     # Background image width
        self.bee_h = bee_h   # Bee image height
        self.bee_w = bee_w   # Bee image width
        
        ## BEE behaviuor
        self.bee_hor_speed = random.randint(args.BEE_HORIZONTAL_SPEED_RANGE[0], args.BEE_HORIZONTAL_SPEED_RANGE[1])
        self.bee_ver_speed = random.randint(args.BEE_VERTICAL_SPEED_RANGE[0], args.BEE_VERTICAL_SPEED_RANGE[1])

        self._set_bee_directions()
        self._set_bee_initial_position()

    def _set_bee_directions(self):
        horizontal_directories = ["LEFT","RIGHT"]
        vertical_directories   = ["IN","OUT"]
        self.bee_hor_dir = random.choice(horizontal_directories)
        self.bee_ver_dir = random.choice(vertical_directories)

    def _set_bee_initial_position(self):
        if self.bee_ver_dir == "OUT":
            self.pos_x = random.randint(0, self.bg_w) 
            self.pos_y = random.randint(self.bg_h-self.bee_h, self.bg_h)

        if self.bee_ver_dir == "IN":
            self.pos_x = random.randint(0, self.bg_w) 
            self.pos_y = random.randint(0,self.bee_h)
        return self.pos_x , self.pos_y

    def update_bee_position(self):
        if self.bee_ver_dir == "IN" and self.bee_hor_dir == "RIGHT":
            self.pos_x = self.pos_x + self.bee_hor_speed
            self.pos_y = self.pos_y + self.bee_ver_speed
        elif self.bee_ver_dir  == "IN" and self.bee_hor_dir == "LEFT":
            self.pos_x = self.pos_x - self.bee_hor_speed
            self.pos_y = self.pos_y + self.bee_ver_speed
        elif self.bee_ver_dir  == "OUT" and self.bee_hor_dir == "RIGHT":
            self.pos_x = self.pos_x + self.bee_hor_speed
            self.pos_y = self.pos_y - self.bee_ver_speed
        elif self.bee_ver_dir  == "OUT" and self.bee_hor_dir == "LEFT":
            self.pos_x = self.pos_x - self.bee_hor_speed
            self.pos_y = self.pos_y - self.bee_ver_speed

        return self.pos_x, self.pos_y
    
    def __str__(self):
        return f"Bee: Size ({self.bee_h}x{self.bee_w}), Position ({self.pos_x}, {self.pos_y}), Direction ({self.bee_hor_dir}, {self.bee_ver_dir})"

    
# ## sample call ##
# bee_1 = Bee(480, 680, 40, 25)
# print(bee_1.update_bee_position())
# print(bee_1.update_bee_position())
