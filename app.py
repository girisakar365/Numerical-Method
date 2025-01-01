import pygame
import pygame_gui
from NM import Config

class App(Config):
    def __init__(self):
        
        super().__init__()
        pygame.init()
        
        self.window = pygame.display.set_mode(self.config_window['size'])
        pygame.display.set_caption(self.config_window['title'])
        
        self.manager = pygame_gui.UIManager(self.config_window['size'])
        
        self.label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((250, 250), (200, 200)),
            text='Hello World!',
            manager=self.manager,
            
        )

    def run(self):
        clock = pygame.time.Clock()
        is_running = True
        while is_running:
            time_delta = clock.tick(60) / 1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
                self.manager.process_events(event)
            
            self.manager.update(time_delta)
            
            self.window.fill(self.config_color['background'])
            
            self.manager.draw_ui(self.window)
            pygame.display.update()
        pygame.quit()

App().run()