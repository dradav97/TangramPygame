import pygame
import collision as c
class Shape():
    def __init__(self, a_game, color, pos, points):
        self.screen = a_game.screen
        self.x = 0
        self.y = 0
        self.color = color
        self.points = points
        

        self.v = c.Vector
        array =[]
        for point in points:
            array.append(self.v(point[0],point[1]))
        print(array)
        
        self.p0 = c.Concave_Poly(self.v(pos[0],pos[1]),array)

    
    def movex(self,direction):
        if direction: 
            self.p0.pos.x += 20
        else:
            self.p0.pos.x -= 20
    

    def movey(self,direction):
        if direction: 
            self.p0.pos.y += 20
        else:
            self.p0.pos.y -= 20

    def rotate(self):
        self.p0.angle += 1.5708
        
        

    def draw(self):
        
        print(self.p0.aabb)
        pygame.draw.polygon(self.screen, self.color,(self.p0.aabb[0],self.p0.aabb[1],self.p0.aabb[3],self.p0.aabb[2]),3)
        pass

