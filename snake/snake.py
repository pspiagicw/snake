import sys
class Snake:
    def __init__(self,init_body,init_direction):
        self.body = init_body
        self.direction = init_direction
    def take_step(self,position):
        self.body = self.body.insert(0,position)
        self.body = self.body[:-1]
    def set_direction(self,direction):
        self.direction = direction
    def get_head(self):
        return self.body[0]
    def get_body(self):
        return self.body[1:]
    def make_move(self,apple_eaten):
        body = self.body
        direction = self.direction
        head = self.get_head()
        new_body = list()
        new_body = [(head[0] - direction[0] , head[1] - direction[1])]
        new_head = new_body
        new_body.extend(body)
        if not apple_eaten:
            new_body = new_body[:-1]
        self.body = new_body
