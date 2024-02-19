import pygame

class Model:
    def __init__(self):
        self.x = 0
        self.y = 0

class View:
    def __init__(self, model):
        self.model = model
        self.surface = pygame.Surface((400, 300))

    def draw(self):
        self.surface.fill((0, 0, 0))
        pygame.draw.circle(self.surface, (255, 255, 255), (self.model.x, self.model.y), 10)

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.model.x -= 1
                elif event.key == pygame.K_RIGHT:
                    self.model.x += 1
                elif event.key == pygame.K_UP:
                    self.model.y -= 1
                elif event.key == pygame.K_DOWN:
                    self.model.y += 1

def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    clock = pygame.time.Clock()

    model = Model()
    view = View(model)
    controller = Controller(model, view)

    running = True
    while running:
        controller.handle_events()
        view.draw()
        screen.blit(view.surface, (0, 0))
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()
