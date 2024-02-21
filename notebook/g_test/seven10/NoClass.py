import pygame, pygame_gui
from PG import PG

# MTitleクラスの代わりに辞書型の変数を作る
m_title = {
    "title": "Input name and push enter key!",
    "text": ""
}

# VTitleクラスの代わりに関数を作る
def v_title_init(a):
    text_surface = a["font"].render(
        a["m_title"]["title"], True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.center = (a["width"] // 2, a["height"] // 2)
    a["window_surface"].blit(text_surface, text_rect)

    # テキストボックスを作成 # 追加
    a["text_box"] = pygame_gui.elements.ui_text_box.UITextBox(
        html_text="",
        relative_rect=pygame.Rect((0, 0), (200, 50)),
        manager=a["manager"]
    )
    a["text_box"].set_position((a["width"] // 2 - 100, 50)) # 画面上部
    a["text_box"].on_text_changed = v_title_on_text_changed
    a["text_box"].on_text_entry_finished = v_title_on_text_entry_finished # 追加

def v_title_on_text_changed(event):
    # テキストボックス内のテキストを取得
    text = event.text

    # テキストをm_titleのtext属性に代入
    m_title["text"] = text

def v_title_on_text_entry_finished(event):
    # テキストボックスの入力が完了したときにc_title_init関数を呼び出す
    c_title_init(event)

# CTitleクラスの代わりに関数を作る
def c_title_init(event):
    print("MTitle.text:", m_title["text"])
    # if event.type == pygame.USEREVENT:
    #     if event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
    #         # 入力された値をm_titleのtext属性に代入
    #         print(event.text)
    #         m_title["text"] = event.text

# Inputクラスの代わりに関数を作る
def input_do(a):
    a["time_delta"] = a["clock"].tick(a["frame"])/1000.0 #Clock設定
    ###イベント周りの処理はこの辺で
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            a["is_running"] = False

        ### add event action
        # if event.type == pygame_gui.UI_BUTTON_PRESSED:
        #     if event.ui_element == hello_button:
        #         print('Hello World!')

        a["manager"].process_events(event)

        c_title_init(event)

# Logicクラスの代わりに関数を作る
def logic_do(a):
    pass

# Resolveクラスの代わりに関数を作る
def resolve_do(a):
    if (a["scene"] != a["before_scene"]):
        ###ループの最初や画面遷移の直後に行う初期化
        v_title_init(a)
        #シーン変更処理完了
        a["before_scene"] = a["scene"]
        # print(f"{self.scene} (<-{self.before_scene})")

# Viewクラスの代わりに関数を作る
def view_do(a):
    a["manager"].update(a["time_delta"]) #guiの更新
    a["window_surface"].blit(a["background"], (0, 0)) #画面の描画

    ### 描画
    ### 描画時に小細工をする場合はこの辺に
    v_title_init(a)
    ###

    a["manager"].draw_ui(a["window_surface"]) #guiの描画
    pygame.display.update() #pg表示の更新

# Mainクラスの代わりに辞書型の変数と関数を作る
# a = {
#     "name": "MVC",
#     "width": 640,
#     "height": 480,
#     "frame": 60,
#     "scene": "Title", #今のシーン
#     "before_scene": "", #前のシーン
#     "b_list": [input_do, logic_do, resolve_do, view_do],
#     "m_title": m_title, # MTitleクラスのインスタンスの代わり
#     "is_running": True #ループする
# }



# pygameの初期化
a["pg"] = PG().init(a)

# ループ開始
while a["is_running"]:
    for b in a["b_list"]:
        b(a)
