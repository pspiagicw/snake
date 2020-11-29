import sys
from snake import snake
from snake import apple
import random
UP = (1,0)
DOWN = (-1,0)
LEFT = (0,1)
RIGHT = (0,-1)

class Game:
    def __init__(self,height , width):
        self.height  = height
        self.width = width
        self.snake = snake.Snake([(i,0) for i in range(2,5)],UP)
        self.apple = apple.Apple(3,4)
    def board_matrix(self):
        return [ [None]*30 ]*30
    def render(self):
        board = self.board_matrix()
        snake_body = self.snake.get_body()
        snake_head = self.snake.get_head()
        apple = self.apple.get_coordinates()
        print(' +','-'*30,'+')
        for i in range(len(board)):
            print(' | ',end='')
            for j in range(len(board[0])):
                if (i,j) in snake_body:
                    print('O',end='')
                elif (i,j) == snake_head:
                    print('X',end='')
                elif (i,j) == apple:
                    print('*',end='')
                else:
                    print(' ',end='')
            print(' | ')
        print(' +','-'*30,'+')
    def parse_input(self,input):
        if input.lower() == 'w':
            self.snake.set_direction(UP)
        if input.lower() == 's':
            self.snake.set_direction(DOWN)
        if input.lower() == 'a':
            self.snake.set_direction(LEFT)
        if input.lower() == 'd':
            self.snake.set_direction(RIGHT)
        if input.lower() == 'k':
            self.snake.set_direction(UP)
        if input.lower() == 'j':
            self.snake.set_direction(DOWN)
        if input.lower() == 'h':
            self.snake.set_direction(LEFT)
        if input.lower() == 'l':
            self.snake.set_direction(RIGHT)
        if input.lower() == 'q':
            sys.exit(0)
        self.snake.make_move(self.apple_eaten())
        self.apple_check()
        self.snake_dead()
    def apple_check(self):
        if self.apple.is_eaten:
            self.apple  = apple.Apple(random.randint(0,20),random.randint(0,20))
    def apple_eaten(self):
        head = self.snake.get_head()
        if head == self.apple.get_coordinates():
            self.apple.is_eaten = True
            return True
        return False
    def snake_dead(self):
        head = self.snake.get_head()
        head_x , head_y = head
        if head_x == -1 or head_x == 30 or head_y == -1 or head_y == 30:
            print('Dead')
            sys.exit(0)
