import pygame

class Shape():
    def __init__(self, a_game, color, pos, points):
        self.screen = a_game.screen
        self.x = 0
        self.y = 0
        self.color = color
        self.points = points
        

        

    
    def movex(self,direction):
        if direction: 
            pass
        else:
            pass
    

    def movey(self,direction):
        if direction: 
            pass
        else:
            pass

    def rotate(self):
        pass
        
        

    def draw(self):
        
        print(self.points)
        pygame.draw.polygon(self.screen, self.color,(self.points[0],self.points[1],self.points[2],self.points[3]))
        pass

