import pygame
import pygame_gui
from pygame_gui.core import ObjectID
from NM import Config
import os

class App(Config):
    def __init__(self):
        
        super().__init__()
        pygame.init()

        # set display size according to screen size
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        info = pygame.display.Info()
        screen_width, screen_height = info.current_w, info.current_h    
        self.screen_size = (screen_width - 10 , screen_height - 100)
        self.window = pygame.display.set_mode(self.screen_size, pygame.RESIZABLE)
        pygame.display.set_caption(self.screen['title'])
        
        self.manager = pygame_gui.UIManager(self.screen_size, 'theme.json')
        self.elements()
        
    def elements(self):

        lable = 'Numerical Method'
        label_width = self.w_scale * self.font['size'] * len(lable)
        label_height = self.h_scale * self.font['size']
        lable_posx = self.s_width//2 - label_width//2
        lable_posy = 40

        self.label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((lable_posx, lable_posy), (label_width, label_height)),
            text=lable,
            manager=self.manager,
            object_id=ObjectID(class_id = "@label", object_id="#title")
        )

        w_gap = self.s_width//2 - 20
        top_gap = 90
        btm_gap = self.s_height - 140

        frame_rect_1 = pygame.Rect(20, top_gap, w_gap, btm_gap)
        frame_1 = pygame_gui.elements.UIPanel(
            relative_rect=frame_rect_1,
            manager=self.manager,
            object_id=ObjectID(class_id = "@frame", object_id="#input")
        )
        frame_rect_2 = pygame.Rect(w_gap + 20, top_gap, w_gap, btm_gap)
        frame_2 = pygame_gui.elements.UIPanel(
            relative_rect=frame_rect_2,
            manager=self.manager,
            object_id=ObjectID(class_id = "@frame", object_id="#output")
        )

        seek_bar = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=pygame.Rect(20, self.s_height - 45, w_gap*2, 23),  
            start_value=0,
            value_range=(0, 100),
            manager=self.manager
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
            
            self.window.fill(self.color['background'])
            
            self.manager.draw_ui(self.window)
            pygame.display.update()
        pygame.quit()

App().run()