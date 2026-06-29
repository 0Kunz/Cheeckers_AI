class BoardCoordinates:
    START_X = 22
    START_Y = 702
    TILE_SIZE = 97
    BOARD_SIZE = 8

    def __init__(self):
        self.start_x = self.START_X
        self.start_y = self.START_Y
        self.tile_size = self.TILE_SIZE
        self.board_size = self.BOARD_SIZE

        self.map_coordinates = self.create_map_coordinates()

    def create_map_coordinates(self):
        coordinates = []

        for row in range(self.board_size):
            coordinate_row = []

            for column in range(self.board_size):
                x = self.start_x + (column * self.tile_size)
                y = self.start_y - (row * self.tile_size)

                coordinate_row.append((x, y))

            coordinates.append(coordinate_row)

        return coordinates

    def get_pixel_position(self, row, column):
        return self.map_coordinates[row][column]

    def get_tile_by_pixel(self, x, y):
        if not self.is_inside_board_area(x, y):
            return None

        column = int((x - self.left_limit()) // self.tile_size)
        row = int((self.top_limit() - y) // self.tile_size)

        return row, column

    def is_inside_board_area(self, x, y):
        return (
            self.left_limit() <= x < self.right_limit()
            and self.bottom_limit() <= y < self.top_limit()
        )

    def left_limit(self):
        return self.start_x

    def right_limit(self):
        return self.start_x + (self.tile_size * self.board_size)

    def top_limit(self):
        return self.start_y + self.tile_size

    def bottom_limit(self):
        return self.start_y - (self.tile_size * (self.board_size - 1))