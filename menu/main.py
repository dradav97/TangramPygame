
import pygame
import sys
from Button import Button

from figures.Triangle import Triangle
from figures.Quadrilateral import Quadrilateral
from figures.Vertex import Vertex
import numpy as np
from copy import deepcopy
from files import read,write
from Api import Api

class TangramGame:
    def __init__ (self):
        # display settings
        pygame.init()
        self.api = Api()
        self.screen = pygame.display.set_mode((1000,1000))
        pygame.display.set_caption("Tangram Game")
        self.clock = pygame.time.Clock()
        self.color = (230,230,230)
        self.color_brown = (103,77,77)
        self.color_black =(0,0,0)
        self.font = pygame.font.SysFont('Consolas', 30)

        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)
        self.BLUE = (0, 0, 255)
        self.VIOLET = (125, 125, 125)
        self.YELLOW = (200, 0, 200)
        self.ORANGE = (200, 200, 0)

        self.nada ='no entro'
        self.contador_tiempo = 128
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        self.text_timer = ""

        # state game
        self.game_activated = False

        self.control= False

        # add components
        self.play_button = Button(self,"Play")
        self.win_button = Button(self,"Felicitaciones has completado el tangram")
        #self.tq = Quadrilateral(Vertex([10, 30]), Vertex([10, 80]), Vertex([90, 80]), Vertex([90, 30]), Vertex([10, 30]), self.screen)
        self.algo = True
        self.terminado = True
        self.factor = 5
        self.lado = 90
        self.arriba = 50
        self.a = Vertex(np.array([self.lado+0,self.arriba+0]) * self.factor)
        self.n = Vertex(np.array([self.lado+50, self.arriba+0]) * self.factor)
        self.b = Vertex(np.array([self.lado+100,self.arriba+ 0]) * self.factor)
        self.j = Vertex(np.array([self.lado+25, self.arriba+25]) * self.factor)
        self.i = Vertex(np.array([self.lado+75,self.arriba+ 25]) * self.factor)
        self.l = Vertex(np.array([self.lado+0,self.arriba+ 50]) * self.factor)
        self.r = Vertex(np.array([self.lado+25, self.arriba+50]) * self.factor)
        self.f = Vertex(np.array([self.lado+50,self.arriba+ 50]) * self.factor)
        self.q = Vertex(np.array([self.lado+75,self.arriba+ 50]) * self.factor)
        self.m = Vertex(np.array([self.lado+100,self.arriba+ 50]) * self.factor)
        self.o = Vertex(np.array([self.lado+25,self.arriba+ 75]) * self.factor)
        self.s = Vertex(np.array([self.lado+50,self.arriba+ 75]) * self.factor)
        self.p = Vertex(np.array([self.lado+75,self.arriba+ 75]) * self.factor)
        self.c = Vertex(np.array([self.lado+0, self.arriba+100]) * self.factor)
        self.h = Vertex(np.array([self.lado+25,self.arriba+ 100]) * self.factor)
        self.t = Vertex(np.array([self.lado+50,self.arriba+ 100]) * self.factor)
        self.k = Vertex(np.array([self.lado+75, self.arriba+100]) * self.factor)
        self.d = Vertex(np.array([self.lado+100,self.arriba+ 100]) * self.factor)


        self.tq = Triangle(deepcopy(self.a), deepcopy(self.j), deepcopy(self.n), deepcopy(self.a), self.screen, self.GREEN,"tq")
        self.tw = Triangle(deepcopy(self.n), deepcopy(self.i), deepcopy(self.b), deepcopy(self.n), self.screen, self.RED,"tw")
        self.ty = Triangle(deepcopy(self.j), deepcopy(self.r), deepcopy(self.f), deepcopy(self.j), self.screen, self.BLUE,"ty")
        self.tu = Triangle(deepcopy(self.i), deepcopy(self.f), deepcopy(self.q), deepcopy(self.i), self.screen, self.BLUE,"tu")
        self.ti = Triangle(deepcopy(self.r), deepcopy(self.o), deepcopy(self.f), deepcopy(self.r), self.screen, self.VIOLET,"ti")
        self.to = Triangle(deepcopy(self.f), deepcopy(self.p), deepcopy(self.q), deepcopy(self.f), self.screen, self.VIOLET,"to")
        self.tp = Triangle(deepcopy(self.f), deepcopy(self.o), deepcopy(self.p), deepcopy(self.f), self.screen, self.BLUE,"tp")
        self.ta = Triangle(deepcopy(self.l), deepcopy(self.c), deepcopy(self.o), deepcopy(self.l), self.screen, self.RED,"ta")
        self.ts = Triangle(deepcopy(self.o), deepcopy(self.c), deepcopy(self.h), deepcopy(self.o), self.screen, self.BLUE,"ts")

        self.tr = Quadrilateral(deepcopy(self.n), deepcopy(self.j), deepcopy(self.f), deepcopy(self.i), deepcopy(self.n), self.screen,self.ORANGE,"tr")
        self.te = Quadrilateral(deepcopy(self.a), deepcopy(self.l), deepcopy(self.o), deepcopy(self.j), deepcopy(self.a), self.screen,self.YELLOW,"te")
        self.tt = Quadrilateral(deepcopy(self.b), deepcopy(self.i), deepcopy(self.p), deepcopy(self.m), deepcopy(self.b), self.screen,self.GREEN,"tt")
        self.td = Quadrilateral(deepcopy(self.o), deepcopy(self.h), deepcopy(self.t), deepcopy(self.s), deepcopy(self.o), self.screen,self.GREEN,"td")
        self.tf = Quadrilateral(deepcopy(self.s), deepcopy(self.t), deepcopy(self.k), deepcopy(self.p), deepcopy(self.s), self.screen,self.RED,"tf")
        self.tg = Quadrilateral(deepcopy(self.m), deepcopy(self.p), deepcopy(self.k), deepcopy(self.d), deepcopy(self.m), self.screen,self.YELLOW,"tg")

        self.f1 = [
            [self.tq, self.a],
            [self.tw, self.n],
            [self.ty, self.j],
            [self.tu, self.i],
            [self.ti, self.r],
            [self.to, self.f],
            [self.tp, self.f],
            [self.ta, self.l],
            [self.ts, self.o],
            [self.tr, self.n],
            [self.te, self.a],
            [self.tt, self.b],
            [self.td, self.o],
            [self.tf, self.s],
            [self.tg, self.m],
            ]
    
    def run_game(self):
        # 
        start_ticks=pygame.time.get_ticks()
        while True:
            # time of frames
            self.clock.tick(60)
            
            
            
            # even loop
            for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    sys.exit()
                

                # time event
                if event.type == pygame.USEREVENT and self.game_activated: 
                    if(self.contador_tiempo>=0):
                        self.contador_tiempo -= 1
                        #str( self.contador_tiempo ).rjust(3)
                        minutes = str(self.contador_tiempo//60) if self.contador_tiempo//60>10 else "0"+str(self.contador_tiempo//60)
                        seconds = str(self.contador_tiempo%60) if self.contador_tiempo%60>10 else "0"+str(self.contador_tiempo%60)
                        operation = minutes + ':' + seconds
                        self.text_timer = operation.rjust(3) if self.contador_tiempo > 0 else 'boom!'

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
                        for i in self.f1:
                            i[0].pos_random()
                        #self.tr.toOrigin()
                        self.terminado = True
                        print("\n\nFelicitaciones completaste el tangram!!!!!!!\n\n")
                        

                    
                    
                
                    
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
                self.screen.blit(self.font.render(self.text_timer, True, (0, 0, 0)), (32, 48))

                if(self.validateCardFinish()):
                    if self.terminado:
                        self.api.set_status()
                        print("oscar gano")
                        break
                body = self.api.get_status()
                if(body["status"]):
                    print(f'{body["name"]} ya gano')
                    break


                """
                # esto es para que el programa juegue solo, o mas o menos era la idea
                for i in self.f1:
                    self.validateCard(i[0],i[1])
                """


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
        #pygame.draw.rect(self.screen,self.color_brown, [800, 0, 200, 900], 0)
        pygame.draw.rect(self.screen,self.color_brown, [90*self.factor, 50*self.factor, 100*self.factor+2, 100* self.factor+2],1)
        # self.screen = pygame.display.set_mode((1600,900))

        
    def validateCard(self, card, pos_final):
        if(self.terminado):
            variable = read(card.name)
            print('----------------------'+card.name)
            if(self.validatePreviosPoint(variable,card.center.vertex)):
                card.toOrigin()
            write(card.name,card.toString())

            
            if card.center.x > pos_final.x:
                card.move_l

            if card.center.y > pos_final.y:
                card.move_u
            
            if card.center.x < pos_final.x:
                card.move_r

            if card.center.y < pos_final.y:
                card.move_d

        if (self.validateCardFinish()):
            if self.terminado:
                print('termino')
                print(self.nada)
                self.terminado = False

    def validatePreviosPoint(self,arreglo, centro_comparar):
        out = True
        #print('------------------------------------------------------------------------')
        #print(arreglo)
        #print(len(arreglo))
        #print(centro_comparar)
        
        for i in range(len(arreglo)):
            #print("$$")
            #print(i)
            print("##")
            print(arreglo[i][0][0])
            print(arreglo[i][0][1])
            #print(arreglo[i][0])
            
            
            print('-------')

            print(centro_comparar[0])
            #print(arreglo[i][0])
            print(centro_comparar[1])
            print("##\n")
            if (int(arreglo[i][0][0]==int(centro_comparar[0]))):
                self.nada= 'entra a la primera'
                if (int(arreglo[i][0][1]==int(centro_comparar[1]))):
                    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ Se encontro una coincidencia @@@@@@@@@@@@@@@@@@@@@@@@@@@@')
                else:
                    out = False
            else:
                out = False
        #print('----------')
        
        return out
        
        
    def validateCardFinish (self):
        out = True
        for i in self.f1:
            if(i[0].center.x == i[0].origincenter.x):
                if(i[0].center.y == i[0].origincenter.y):
                    pass
                else:
                    return False
            else:
                return False
        return out
                    
    
        

                


            
            

        
        

        

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
