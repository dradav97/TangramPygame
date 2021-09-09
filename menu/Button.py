import pygame.font

class Button:
    def __init__(self, a_game, text):
        self.screen = a_game.screen
        self.screen_rect = self.screen.get_rect()
        self.width, self.height = 200,50
        self.color = (255,0,0)
        self.textColor = (255,255,255)

        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        
        self.prepare_text(text)

    def prepare_text(self, text):
        self.text_image = self.font.render(text, True, self.textColor, self.color)
        self.text_image_rect = self.text_image.get_rect()
        self.text_image_rect.center = self.rect.center
    
    def draw_button(self):
        self.screen.fill(self.color, self.rect)
        self.screen.blit(self.text_image, self.text_image_rect)