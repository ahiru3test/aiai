# スタート画面の処理をする関数
def start():
    global game_state, cpu_number1, cpu_number2, player_number, player_win
    # キー入力を処理する
    for event in pygame.event.get():
        # ウィンドウの×ボタンを押したら終了する
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # スペースキーを押したらプレイ画面に移行する
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_state = PLAY
            # CPUがランダムに2つの数字を選ぶ
            # この処理をここから移動する
            # cpu_number1 = random.choice(numbers)
            # cpu_number2 = random.choice(numbers)
            # プレイヤーの数字を初期化する
            player_number = 0
            # プレイヤーの勝敗を初期化する
            player_win = False

    # スタート画面のメッセージを描画する
    draw_text("High and Low Game", 100, WHITE, window, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 4)
    draw_text("Press Space to start", 50, WHITE, window, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)

# プレイ画面の処理をする関数
def play():
    global game_state, cpu_number1, cpu_number2, player_number, player_win
    # キー入力を処理する
    for event in pygame.event.get():
        # ウィンドウの×ボタンを押したら終了する
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # 4キーを押したらプレイヤーの数字をLowにする
        if event.type == pygame.KEYDOWN and event.key == pygame.K_4:
            player_number = 4
            # プレイヤーの数字とCPUの数字を比較する
            compare_numbers()
            # エンド画面に移行する
            game_state = END
        # 6キーを押したらプレイヤーの数字をHighにする
        if event.type == pygame.KEYDOWN and event.key == pygame.K_6:
            player_number = 6
            # プレイヤーの数字とCPUの数字を比較する
            compare_numbers()
            # エンド画面に移行する
            game_state = END

    # プレイ画面のメッセージを描画する
    draw_text("CPU's numbers", 50, WHITE, window, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 4)
    draw_text(str(cpu_number1) + " ?", 100, WHITE, window, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
    draw_text("Press 4(Low) or 6(High)", 50, WHITE, window, WINDOW_WIDTH / 2, WINDOW_HEIGHT * 3 / 4)

    # CPUがランダムに2つの数字を選ぶ
    # この処理をここに移動する
    cpu_number1 = random.choice(numbers)
    cpu_number2 = random.choice(numbers)
