import pygame
import pygame_gui
pygame.init()
pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode((800, 600))
background = pygame.Surface((800, 600))
background.fill(pygame.Color('#000000'))
manager = pygame_gui.UIManager((800, 600))

# button_layout_rect = pygame.Rect(30, 20, 100, 20)

ui_window = pygame_gui.windows.UIMessageWindow(
    rect=pygame.Rect(100, 100, 600, 400),
    manager=manager,
    html_message="My UI Window"
)

#add button
hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)),
                                            text='Say Hello',
                                            manager=manager,
                                            container=ui_window
                                            )

clock = pygame.time.Clock()
is_running = True
while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

#add button action
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == hello_button:
                print('Hello World!')

        manager.process_events(event)
    manager.update(time_delta)
    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)
    pygame.display.update()
