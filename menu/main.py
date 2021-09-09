
import pygame
import sys
from Button import Button

from figures.Triangle import Triangle
from figures.Quadrilateral import Quadrilateral
from figures.Vertex import Vertex
import numpy as np
from copy import deepcopy


class TangramGame:
    def __init__ (self):
        # display settings
        pygame.init()
        self.screen = pygame.display.set_mode((1000,900))
        pygame.display.set_caption("Tangram Game")
        self.clock = pygame.time.Clock()
        self.color = (230,230,230)
        self.color_brown = (103,77,77)
        self.color_black =(0,0,0)

        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)
        self.BLUE = (0, 0, 255)
        self.VIOLET = (125, 125, 125)
        self.YELLOW = (200, 0, 200)
        self.ORANGE = (200, 200, 0)

        # state game
        self.game_activated = False

        self.control= False

        # add components
        self.play_button = Button(self,"Play")
        #self.tq = Quadrilateral(Vertex([10, 30]), Vertex([10, 80]), Vertex([90, 80]), Vertex([90, 30]), Vertex([10, 30]), self.screen)
        factor = 5
        a = Vertex(np.array([0, 0]) * factor)
        n = Vertex(np.array([50, 0]) * factor)
        b = Vertex(np.array([100, 0]) * factor)
        j = Vertex(np.array([25, 25]) * factor)
        i = Vertex(np.array([75, 25]) * factor)
        l = Vertex(np.array([0, 50]) * factor)
        r = Vertex(np.array([25, 50]) * factor)
        f = Vertex(np.array([50, 50]) * factor)
        q = Vertex(np.array([75, 50]) * factor)
        m = Vertex(np.array([100, 50]) * factor)
        o = Vertex(np.array([25, 75]) * factor)
        s = Vertex(np.array([50, 75]) * factor)
        p = Vertex(np.array([75, 75]) * factor)
        c = Vertex(np.array([0, 100]) * factor)
        h = Vertex(np.array([25, 100]) * factor)
        t = Vertex(np.array([50, 100]) * factor)
        k = Vertex(np.array([75, 100]) * factor)
        d = Vertex(np.array([100, 100]) * factor)

        self.tq = Triangle(deepcopy(a), deepcopy(j), deepcopy(n), deepcopy(a), self.screen, self.GREEN)
        self.tw = Triangle(deepcopy(n), deepcopy(i), deepcopy(b), deepcopy(n), self.screen, self.RED)
        self.ty = Triangle(deepcopy(j), deepcopy(r), deepcopy(f), deepcopy(j), self.screen, self.BLUE)
        self.tu = Triangle(deepcopy(i), deepcopy(f), deepcopy(q), deepcopy(i), self.screen, self.BLUE)
        self.ti = Triangle(deepcopy(r), deepcopy(o), deepcopy(f), deepcopy(r), self.screen, self.VIOLET)
        self.to = Triangle(deepcopy(f), deepcopy(p), deepcopy(q), deepcopy(f), self.screen, self.VIOLET)
        self.tp = Triangle(deepcopy(f), deepcopy(o), deepcopy(p), deepcopy(f), self.screen, self.BLUE)
        self.ta = Triangle(deepcopy(l), deepcopy(c), deepcopy(o), deepcopy(l), self.screen, self.RED)
        self.ts = Triangle(deepcopy(o), deepcopy(c), deepcopy(h), deepcopy(o), self.screen, self.BLUE)

        self.cr = Quadrilateral(deepcopy(n), deepcopy(j), deepcopy(f), deepcopy(i), deepcopy(n), self.screen,self.ORANGE)
        self.ce = Quadrilateral(deepcopy(a), deepcopy(l), deepcopy(o), deepcopy(j), deepcopy(a), self.screen,self.YELLOW)
        self.ct = Quadrilateral(deepcopy(b), deepcopy(i), deepcopy(p), deepcopy(m), deepcopy(b), self.screen,self.GREEN )
        self.cd = Quadrilateral(deepcopy(o), deepcopy(h), deepcopy(t), deepcopy(s), deepcopy(o), self.screen,self.GREEN)
        self.cf = Quadrilateral(deepcopy(s), deepcopy(t), deepcopy(k), deepcopy(p), deepcopy(s), self.screen,self.RED)
        self.cg = Quadrilateral(deepcopy(m), deepcopy(p), deepcopy(k), deepcopy(d), deepcopy(d), self.screen,self.YELLOW)
    
    def run_game(self):
        # 
        while True:
            # time of frames
            self.clock.tick(60)
            
            # even loop
            for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    sys.exit()
                
                # mouse event
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # we get the mouse position
                    mousePos = pygame.mouse.get_pos()
                    self.check_button(mousePos)

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.control = True
                if event.type == pygame.KEYDOWN:
                    if event.key== pygame.K_RIGHT:
                        self.tq.move_r
                    if event.key== pygame.K_DOWN:
                        self.tq.move_d
                    if event.key== pygame.K_LEFT:
                        self.tq.move_l
                    if event.key== pygame.K_UP:
                        self.tq.move_u
                    if event.key== pygame.K_SPACE:
                        self.tq.rotate()


                elif event.type == pygame.KEYDOWN:
                    self.control= False




            #draw button
            self.play_button.draw_button()
            

            if self.game_activated:
                # game operation
                self.screen.fill(self.color)
                self.interface()
                #draw tq
                self.draw_tqs()
                
        

            
            
            

            # Update the full display Surface to the screen
            pygame.display.flip()


    def draw_tqs(self):
        self.tq.draw()
        self.tw.draw()
        self.ty.draw()
        self.tu.draw()
        self.ti.draw()
        self.to.draw()
        self.tp.draw()
        self.ta.draw()
        self.ts.draw()

        self.cr.draw()
        self.ce.draw()
        self.ct.draw()
        self.cd.draw()
        self.cf.draw()
        self.cg.draw()


    def interface(self):
        # screen 800,500
        # 800 - 200
        pygame.draw.rect(self.screen,self.color_brown, [800, 0, 200, 900], 0)
        
        pass

    def check_button(self,mousePos):
        if self.play_button.rect.collidepoint(mousePos):
            print(f"{mousePos}")
            self.game_activated = True

    def check_tqs(self, mousePos):
        pass


if __name__ == '__main__':
    game = TangramGame()
    game.run_game()
