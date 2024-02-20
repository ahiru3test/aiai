class MazeController:

    cursor_dict = {
        'h': (-1, 0),
        'j': (0, 1),
        'k': (0, -1),
        'l': (1, 0),
    }

    model = None
    view = None

    def process_input(self, input_str):
        if input_str in self.cursor_dict.keys():
            self.model.process(self.cursor_dict[input_str])
            return self.view.render(self.model)
        return self.view.render(
            self.model, message='h,j,k,lのいずれかを入力してください。')


class NormalMazeModel:

    world = list(list())
    current_x = 1
    current_y = 1
    message = ''

    def __init__(self):
        self.world = [
            [1, 0, 1, 1, 1],
            [1, 0, 1, 0, 0],
            [1, 0, 1, 0, 1],
            [1, 0, 0, 0, 1],
            [0, 0, 1, 1, 1],
        ]
        self.world[self.current_x][self.current_y] = -1

    def _get_next_place(self, diff):
        return self.current_x + diff[0], self.current_y + diff[1]

    def process(self, diff):
        new_x, new_y = self._get_next_place(diff)
        # 配列をそのまま使っているのでx,yに注意する
        if 0 <= new_y < len(self.world) and \
                0 <= new_x < len(self.world[new_y]) and \
                self.world[new_y][new_x] == 0:
            self.world[self.current_y][self.current_x] = 0
            self.world[new_y][new_x] = -1
            self.current_x, self.current_y = new_x, new_y
            self.message = 'GOGO!'
        else:
            self.message = '* おおっと *'


class NormalMazeView:

    world_map_dict = {
        -1: '@',
        0: '.',
        1: '#',
    }

    def _render_map(self, world):
        return '\n'.join([
            ''.join([self.world_map_dict[w] for w in world_row])
            for world_row in world])

    def render(self, model, message=None):
        if message is None:
            message = model.message
        return message + '\n' + self._render_map(model.world)


if __name__ == '__main__':
    controller = MazeController()
    controller.model = NormalMazeModel()
    controller.view = NormalMazeView()
    print(controller.process_input(''))
    while True:
        print(controller.process_input(input('')))

