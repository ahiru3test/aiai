import pygame
import pygame_gui
from SingletonMeta import SingletonMeta

### Model -------------------------------------------------------------
# ゲームの状態やロジックを管理するクラス
class GameModel(metaclass=SingletonMeta):
    # ゲームの初期化を行うメソッド
    def init(self):
        self.title = "Input name and push enter key!" # タイトル
        self.text = "" # テキスト
        self.timer = 60 # タイマー
        self.game_over = False # ゲームオーバーのフラグ

    # ゲームの状態を更新するメソッド
    def update(self, input):
        # 入力に応じてテキストを変更する
        if input == pygame.K_BACKSPACE:
            self.text = self.text[:-1]
        elif input == pygame.K_RETURN:
            self.text = ""
        else:
            self.text += input.unicode

        # タイマーを減らす
        self.timer -= 1

        # タイマーが0になったらゲームオーバーにする
        if self.timer == 0:
            self.game_over = True

### View --------------------------------------------------------------
# ゲームの画面や音声を表示するクラス
class GameView(metaclass=SingletonMeta):
    # 画面の初期化を行うメソッド
    def init(self, config):
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption(config.name)
        self.window_surface = pygame.display.set_mode((config.width, config.height))
        self.background=pygame.Surface((config.width,config.height))
        self.background.fill(pygame.Color('#000000'))
        self.manager = pygame_gui.UIManager((config.width, config.height))
        self.font = pygame.font.SysFont("Arial",32)

        # テキストボックスを作成
        self.text_box = pygame_gui.elements.ui_text_box.UITextBox(
            html_text="",
            relative_rect=pygame.Rect((0, 0), (200, 50)),
            manager=self.manager
        )
        self.text_box.set_position((config.width // 2 - 100, 50)) # 画面上部

    # 画面の描画を行うメソッド
    def draw(self, model, config):
        # 画面を消去する
        self.window_surface.blit(self.background, (0, 0))

        # タイトルを描画する
        title_surface = self.font.render(
            model.title, True, (255, 255, 255))
        title_rect = title_surface.get_rect()
        title_rect.center = (config.width // 2, config.height // 2)
        self.window_surface.blit(title_surface, title_rect)

        # テキストボックスにテキストを表示する
        self.text_box.html_text = model.text
        self.text_box.rebuild()

        # タイマーを描画する
        timer_surface = self.font.render(
            str(model.timer), True, (255, 255, 255))
        timer_rect = timer_surface.get_rect()
        timer_rect.center = (config.width // 2, config.height // 2 + 50)
        self.window_surface.blit(timer_surface, timer_rect)

        # ゲームオーバーの場合はメッセージを描画する
        if model.game_over:
            game_over_surface = self.font.render(
                "Game Over!", True, (255, 0, 0))
            game_over_rect = game_over_surface.get_rect()
            game_over_rect.center = (config.width // 2, config.height // 2 + 100)
            self.window_surface.blit(game_over_surface, game_over_rect)

        # GUIの更新と描画を行う
        self.manager.update(config.time_delta)
        self.manager.draw_ui(self.window_surface)

        # 画面の更新を行う
        pygame.display.update()

### Controller---------------------------------------------------------
# ゲームの入力や操作を受け付けるクラス
class GameController(metaclass=SingletonMeta):
    # 入力の検出を行うメソッド
    def get_input(self, config):
        # イベントを取得する
        for event in pygame.event.get():
            # 終了イベントの場合はゲームを終了する
            if event.type == pygame.QUIT:
                config.is_running = False

            # GUIのイベントを処理する
            config.view.manager.process_events(event)

            # キーボードのイベントの場合は入力を返す
            if event.type == pygame.KEYDOWN:
                return event

        # イベントがない場合はNoneを返す
        return None

### Main --------------------------------------------------------------
# ゲームの設定やループを管理するクラス
class GameConfig():
    def __init__(self,name="MVC",width=640,height=480,frame=60):
        self.name=name
        self.width=width
        self.height=height
        self.frame=frame
        self.is_running = True #ループする

        # ゲームのモデル、ビュー、コントローラーを作成する
        self.model = GameModel()
        self.view = GameView()
        self.controller = GameController()

        # 画面の初期化を行う
        self.view.init(self)

        # ゲームの初期化を行う
        self.model.init()

        # 時間管理用のクロックを作成する
        self.clock = pygame.time.Clock()

        # ゲームループを開始する
        self.game_loop()

    # ゲームループを行うメソッド
    def game_loop(self):
        while self.is_running:
            # 時間の更新を行う
            self.time_delta = self.clock.tick(self.frame)/1000.0

            # 入力の取得を行う
            input = self.controller.get_input(self)

            # 入力がある場合はゲームの状態を更新する
            if input is not None:
                self.model.update(input)

            # 画面の描画を行う
            self.view.draw(self.model, self)

if (__name__=="__main__"): GameConfig()
