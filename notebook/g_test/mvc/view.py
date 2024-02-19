import pygame

class View:
    def __init__(self, model):
        self.model = model

        # Pygameを初期化する
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        self.clock = pygame.time.Clock()

    def draw(self):
        # 画面を塗りつぶす
        self.screen.fill((0, 0, 0))

        # モデルからデータを取得する
        x = self.model.x
        y = self.model.y

        # データを描画する
        pygame.draw.rect(self.screen, (255, 255, 255), (x, y, 10, 10))

        # 画面を更新する
        pygame.display.update()

    def run(self):
        while True:
            # イベントを処理する
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.model.move_up()
                    elif event.key == pygame.K_DOWN:
                        self.model.move_down()
                    elif event.key == pygame.K_LEFT:
                        self.model.move_left()
                    elif event.key == pygame.K_RIGHT:
                        self.model.move_right()

            # ビューを描画する
            self.draw()

            # フレームレートを制限する
            self.clock.tick(60)
