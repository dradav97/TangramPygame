import pygame

import sys
from Button import Button
from Shape import Shape
import collision as c


class TangramGame:
    def __init__ (self):
        # display settings
        pygame.init()
        self.screen = pygame.display.set_mode((800,500))
        pygame.display.set_caption("Tangram Game")
        self.clock = pygame.time.Clock()
        self.color = (230,230,230)
        self.color_brown = (103,77,77)
        self.color_black =(0,0,0)

        # state game
        self.game_activated = False

        self.control= False

        # add components
        self.play_button = Button(self,"Play")
        self.shape = Shape(self, self.color_black, (0,0), [(10, 10), (10, 80), (20, 10), (20, 80)])
    
    def run_game(self):
        # 
        while True:
            # time of frames
            self.clock.tick(60)
            
            # even loop
            for event in pygame.event.get():
                print(event)
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
                        self.shape.movex(True)
                    if event.key== pygame.K_DOWN:
                        self.shape.movey(True)
                    if event.key== pygame.K_LEFT:
                        self.shape.movex(False)
                    if event.key== pygame.K_UP:
                        self.shape.movey(False)
                    if event.key== pygame.K_SPACE:
                        self.shape.rotate()


                elif event.type == pygame.KEYDOWN:
                    self.control= False

           


            #draw button
            self.play_button.draw_button()
            

            if self.game_activated:
                # game operation
                self.screen.fill(self.color)
                self.interface()
                #draw shape
                self.shape.draw()
        

            
            
            

            # Update the full display Surface to the screen
            pygame.display.flip()


    
    def interface(self):
        # screen 800,500
        # 800 - 200
        pygame.draw.rect(self.screen,self.color_brown, [600, 0, 200, 500], 0)
        
        pass

    def check_button(self,mousePos):
        if self.play_button.rect.collidepoint(mousePos):
            print(f"{mousePos}")
            self.game_activated = True

    def check_shapes(self, mousePos):
        pass


if __name__ == '__main__':
    game = TangramGame()
    game.run_game()
