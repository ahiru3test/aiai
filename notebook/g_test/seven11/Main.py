import pygame

from pygame_gui import UIManager, UI_TEXT_ENTRY_CHANGED
from pygame_gui.elements import UIWindow, UITextEntryBox, UITextBox

class AAA():
    def __init__(self):
        self.name = 'Pygame Notepad'
        self.width =800
        self.height =600

        pygame.init()
        pygame.display.set_caption(self.name)
        self.window_surface = pygame.display.set_mode(
            (self.width, self.height))
        self.manager = UIManager(
            (self.width, self.height)
            , 'data/themes/notepad_theme.json')

        self.background = pygame.Surface(
            (self.width, self.height))
        self.background.fill(
            self.manager.ui_theme.get_colour('dark_bg'))

        self.notepad_window = UIWindow(
            pygame.Rect(50, 20, 300, 400)
            , window_display_title=self.name)
        
        # output_window = UIWindow(
        #     pygame.Rect(400, 20, 300, 400)
        #     , window_display_title="Pygame GUI Formatted Text")

        self.text_entry_box = UITextEntryBox(
            relative_rect=pygame.Rect(
                (0, 0)
                , self.notepad_window.get_container().get_size())
            , initial_text=""
            , container=self.notepad_window)
        # text_output_box = UITextBox(
        #     relative_rect=pygame.Rect((0, 0), output_window.get_container().get_size()),
        #     html_text="",
        #     container=output_window)
        self.clock = pygame.time.Clock()
        self.is_running = True
    
    def run(self):
        while self.is_running:
            time_delta = self.clock.tick(60)/1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False

                if (event.type == UI_TEXT_ENTRY_CHANGED 
                    and event.ui_element == self.text_entry_box):
                    # text_output_box.set_text(event.text)
                    print(event.text)

                self.manager.process_events(event)

            self.manager.update(time_delta)

            self.window_surface.blit(self.background, (0, 0))
            self.manager.draw_ui(self.window_surface)

            pygame.display.update()

if(__name__=="__main__"): (a:=AAA()).run()
