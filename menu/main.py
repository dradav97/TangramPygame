
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
        self.win_button = Button(self,"Felicitaciones has completado el tangram")
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

        self.tr = Quadrilateral(deepcopy(n), deepcopy(j), deepcopy(f), deepcopy(i), deepcopy(n), self.screen,self.ORANGE)
        self.te = Quadrilateral(deepcopy(a), deepcopy(l), deepcopy(o), deepcopy(j), deepcopy(a), self.screen,self.YELLOW)
        self.tt = Quadrilateral(deepcopy(b), deepcopy(i), deepcopy(p), deepcopy(m), deepcopy(b), self.screen,self.GREEN )
        self.td = Quadrilateral(deepcopy(o), deepcopy(h), deepcopy(t), deepcopy(s), deepcopy(o), self.screen,self.GREEN)
        self.tf = Quadrilateral(deepcopy(s), deepcopy(t), deepcopy(k), deepcopy(p), deepcopy(s), self.screen,self.RED)
        self.tg = Quadrilateral(deepcopy(m), deepcopy(p), deepcopy(k), deepcopy(d), deepcopy(d), self.screen,self.YELLOW)
    
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

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.tq.control = True
                    if event.key == pygame.K_w:
                        self.tw.control = True
                    if event.key == pygame.K_e:
                        self.te.control = True
                    if event.key == pygame.K_r:
                        self.tr.control = True
                    if event.key == pygame.K_t:
                        self.tt.control = True
                    if event.key == pygame.K_y:
                        self.ty.control = True
                    if event.key == pygame.K_u:
                        self.tu.control = True
                    if event.key == pygame.K_i:
                        self.ti.control = True
                    if event.key == pygame.K_o:
                        self.to.control = True
                    if event.key == pygame.K_p:
                        self.tp.control = True
                    if event.key == pygame.K_a:
                        self.ta.control = True
                    if event.key == pygame.K_s:
                        self.ts.control = True
                    if event.key == pygame.K_d:
                        self.td.control = True
                    if event.key == pygame.K_f:
                        self.tf.control = True
                    if event.key == pygame.K_g:
                        self.tg.control = True
                    if event.key == pygame.K_1:
                        print("\n\nFelicitaciones completaste el tangram!!!!!!!\n\n")
                        sys.exit()

                    
                    
                
                    
                if event.type == pygame.KEYDOWN:
                    if event.key== pygame.K_RIGHT and self.tq.control:
                        self.tq.move_r
                    if event.key== pygame.K_DOWN and self.tq.control:
                        self.tq.move_d
                    if event.key== pygame.K_LEFT and self.tq.control:
                        self.tq.move_l
                    if event.key== pygame.K_UP and self.tq.control:
                        self.tq.move_u
                    if event.key== pygame.K_SPACE and self.tq.control:
                        self.tq.rotate()

                    if event.key== pygame.K_RIGHT and self.tw.control:
                        self.tw.move_r
                    if event.key== pygame.K_DOWN and self.tw.control:
                        self.tw.move_d
                    if event.key== pygame.K_LEFT and self.tw.control:
                        self.tw.move_l
                    if event.key== pygame.K_UP and self.tw.control:
                        self.tw.move_u
                    if event.key== pygame.K_SPACE and self.tw.control:
                        self.tw.rotate()

                    if event.key== pygame.K_RIGHT and self.te.control:
                        self.te.move_r
                    if event.key== pygame.K_DOWN and self.te.control:
                        self.te.move_d
                    if event.key== pygame.K_LEFT and self.te.control:
                        self.te.move_l
                    if event.key== pygame.K_UP and self.te.control:
                        self.te.move_u
                    if event.key== pygame.K_SPACE and self.te.control:
                        self.te.rotate()

                    if event.key== pygame.K_RIGHT and self.tr.control:
                        self.tr.move_r
                    if event.key== pygame.K_DOWN and self.tr.control:
                        self.tr.move_d
                    if event.key== pygame.K_LEFT and self.tr.control:
                        self.tr.move_l
                    if event.key== pygame.K_UP and self.tr.control:
                        self.tr.move_u
                    if event.key== pygame.K_SPACE and self.tr.control:
                        self.tr.rotate()
                    
                    if event.key== pygame.K_RIGHT and self.tt.control:
                        self.tt.move_r
                    if event.key== pygame.K_DOWN and self.tt.control:
                        self.tt.move_d
                    if event.key== pygame.K_LEFT and self.tt.control:
                        self.tt.move_l
                    if event.key== pygame.K_UP and self.tt.control:
                        self.tt.move_u
                    if event.key== pygame.K_SPACE and self.tt.control:
                        self.tt.rotate()
                    
                    if event.key== pygame.K_RIGHT and self.ty.control:
                        self.ty.move_r
                    if event.key== pygame.K_DOWN and self.ty.control:
                        self.ty.move_d
                    if event.key== pygame.K_LEFT and self.ty.control:
                        self.ty.move_l
                    if event.key== pygame.K_UP and self.ty.control:
                        self.ty.move_u
                    if event.key== pygame.K_SPACE and self.ty.control:
                        self.ty.rotate()
                    
                    if event.key== pygame.K_RIGHT and self.tu.control:
                        self.tu.move_r
                    if event.key== pygame.K_DOWN and self.tu.control:
                        self.tu.move_d
                    if event.key== pygame.K_LEFT and self.tu.control:
                        self.tu.move_l
                    if event.key== pygame.K_UP and self.tu.control:
                        self.tu.move_u
                    if event.key== pygame.K_SPACE and self.tu.control:
                        self.tu.rotate()
                    
                    if event.key== pygame.K_RIGHT and self.ti.control:
                        self.ti.move_r
                    if event.key== pygame.K_DOWN and self.ti.control:
                        self.ti.move_d
                    if event.key== pygame.K_LEFT and self.ti.control:
                        self.ti.move_l
                    if event.key== pygame.K_UP and self.ti.control:
                        self.ti.move_u
                    if event.key== pygame.K_SPACE and self.ti.control:
                        self.ti.rotate()
                    
                    if event.key== pygame.K_RIGHT and self.to.control:
                        self.to.move_r
                    if event.key== pygame.K_DOWN and self.to.control:
                        self.to.move_d
                    if event.key== pygame.K_LEFT and self.to.control:
                        self.to.move_l
                    if event.key== pygame.K_UP and self.to.control:
                        self.to.move_u
                    if event.key== pygame.K_SPACE and self.to.control:
                        self.to.rotate()
                    
                    if event.key== pygame.K_RIGHT and self.tp.control:
                        self.tp.move_r
                    if event.key== pygame.K_DOWN and self.tp.control:
                        self.tp.move_d
                    if event.key== pygame.K_LEFT and self.tp.control:
                        self.tp.move_l
                    if event.key== pygame.K_UP and self.tp.control:
                        self.tp.move_u
                    if event.key== pygame.K_SPACE and self.tp.control:
                        self.tp.rotate()

                    if event.key== pygame.K_RIGHT and self.ta.control:
                        self.ta.move_r
                    if event.key== pygame.K_DOWN and self.ta.control:
                        self.ta.move_d
                    if event.key== pygame.K_LEFT and self.ta.control:
                        self.ta.move_l
                    if event.key== pygame.K_UP and self.ta.control:
                        self.ta.move_u
                    if event.key== pygame.K_SPACE and self.ta.control:
                        self.ta.rotate()
                    
                    if event.key== pygame.K_RIGHT and self.ts.control:
                        self.ts.move_r
                    if event.key== pygame.K_DOWN and self.ts.control:
                        self.ts.move_d
                    if event.key== pygame.K_LEFT and self.ts.control:
                        self.ts.move_l
                    if event.key== pygame.K_UP and self.ts.control:
                        self.ts.move_u
                    if event.key== pygame.K_SPACE and self.ts.control:
                        self.ts.rotate()
                    
                    if event.key== pygame.K_RIGHT and self.td.control:
                        self.td.move_r
                    if event.key== pygame.K_DOWN and self.td.control:
                        self.td.move_d
                    if event.key== pygame.K_LEFT and self.td.control:
                        self.td.move_l
                    if event.key== pygame.K_UP and self.td.control:
                        self.td.move_u
                    if event.key== pygame.K_SPACE and self.td.control:
                        self.td.rotate()
                    
                    if event.key== pygame.K_RIGHT and self.tf.control:
                        self.tf.move_r
                    if event.key== pygame.K_DOWN and self.tf.control:
                        self.tf.move_d
                    if event.key== pygame.K_LEFT and self.tf.control:
                        self.tf.move_l
                    if event.key== pygame.K_UP and self.tf.control:
                        self.tf.move_u
                    if event.key== pygame.K_SPACE and self.tf.control:
                        self.tf.rotate()
                    
                    if event.key== pygame.K_RIGHT and self.tg.control:
                        self.tg.move_r
                    if event.key== pygame.K_DOWN and self.tg.control:
                        self.tg.move_d
                    if event.key== pygame.K_LEFT and self.tg.control:
                        self.tg.move_l
                    if event.key== pygame.K_UP and self.tg.control:
                        self.tg.move_u
                    if event.key== pygame.K_SPACE and self.tg.control:
                        self.tg.rotate()


                elif event.type == pygame.KEYUP:
                    
                    if event.key == pygame.K_q:
                        self.tq.control= False
                    if event.key == pygame.K_w:
                        self.tw.control= False
                    if event.key == pygame.K_e:
                        self.te.control= False
                    if event.key == pygame.K_r:
                        self.tr.control= False
                    if event.key == pygame.K_t:
                        self.tt.control= False
                    if event.key == pygame.K_y:
                        self.ty.control= False
                    if event.key == pygame.K_u:
                        self.tu.control= False
                    if event.key == pygame.K_i:
                        self.ti.control= False
                    if event.key == pygame.K_o:
                        self.to.control= False
                    if event.key == pygame.K_p:
                        self.tp.control= False
                    if event.key == pygame.K_a:
                        self.ta.control= False
                    if event.key == pygame.K_s:
                        self.ts.control= False
                    if event.key == pygame.K_d:
                        self.td.control= False
                    if event.key == pygame.K_f:
                        self.tf.control= False
                    if event.key == pygame.K_g:
                        self.tg.control= False

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

        self.tr.draw()
        self.te.draw()
        self.tt.draw()
        self.td.draw()
        self.tf.draw()
        self.tg.draw()


    def interface(self):
        # screen 800,500
        # 800 - 200
        pygame.draw.rect(self.screen,self.color_brown, [800, 0, 200, 900], 0)
        
        pass

    def validate(self):
        control = False
        if self.tq.point_distance(self.tw.vertex_c)<5:
            control= True
        else:
            control= False
        if self.tw.point_distance(self.tf.vertex_c)<5:
            control= True
        else:
            control= False
        if self.te.point_distance(self.tt.vertex_c)<5:
            control= True
        else:
            control= False
        if self.tt.point_distance(self.tg.vertex_c)<5:
            control= True
        else:
            control= False
        if self.ty.point_distance(self.tu.vertex_c)<5:
            control= True
        else:
            control= False
        if self.tu.point_distance(self.tp.vertex_c)<5:
            control= True
        else:
            control= False
        if self.tp.point_distance(self.to.vertex_c)<5:
            control= True
        else:
            control= False
        if self.to.point_distance(self.ts.vertex_c)<5:
            control= True
        else:
            control= False
        if self.ts.point_distance(self.ta.vertex_c)<5:
            control= True
        else:
            control= False
        if self.tq.point_distance(self.tg.vertex_c)<5:
            control= True
        else:
            control= False
        if self.ts.point_distance(self.to.vertex_c)<5:
            control= True
        else:
            control= False
        return control
        

    def check_button(self,mousePos):
        if self.play_button.rect.collidepoint(mousePos):
            
            self.game_activated = True

    def check_tqs(self, mousePos):
        pass


if __name__ == '__main__':
    game = TangramGame()
    game.run_game()
