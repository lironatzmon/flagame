def create():
    global field
    for i in range(consts.SQUARE_GRID_ROWS):
        row = []
        for j in range(consts.SQUARE_GRID_COLS):
            row.append({"content": "E", "left_cord_x": j * consts.LENGTH, "left_cord_y": i * consts.LENGTH})
        field.append(row)


def put_grass_in_field(grass_img):
    for i in range(20):
        row_random = random.randint(0, consts.SQUARE_GRID_ROWS-1)
        col_random = random.randint(0, consts.SQUARE_GRID_COLS-1)
        cord_y = int(row_random * 20)
        cord_x = int(col_random * 20)
        field[row_random][col_random]["content"] = "G"
        grass = pygame.image.load(grass_img)
        grass_size = pygame.transform.scale(grass, (
            consts.GRASS_WIDTH, consts.GRASS_HEIGHT))
        screen.blit(grass_size, (cord_x, cord_y))
        pygame.display.update()

