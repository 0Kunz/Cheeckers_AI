class BoardCoordinates:

    def __init__(self):
        self.start_x = 22
        self.start_y = 702
        self.tile_size = 97
        self.board_size = 8

        self.map_coordinates = self.create_map_coordinates()

    def create_map_coordinates(self):
        coordinates = [[], [], [], [], [], [], [], []]

        x = self.start_x
        y = self.start_y

        for row in range(self.board_size):
            for col in range(self.board_size):
                coordinates[row].append([x, y])
                x += self.tile_size

            y -= self.tile_size
            x = self.start_x

        return coordinates

    def get_pixel_position(self, row, col):
        return self.map_coordinates[row][col]

    def get_tile_by_pixel(self, x, y):
        left_limit = self.start_x
        right_limit = self.start_x + (self.tile_size * self.board_size)

        bottom_limit = self.start_y - (self.tile_size * (self.board_size - 1))
        top_limit = self.start_y + self.tile_size

        if x < left_limit or x >= right_limit:
            return None

        if y < bottom_limit or y >= top_limit:
            return None

        col = int((x - self.start_x) // self.tile_size)
        row = int((top_limit - y) // self.tile_size)

        return row, col