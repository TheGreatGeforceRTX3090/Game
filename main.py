import pygame
import os


def load_image(name):
    fullname = os.path.join('textures', name)
    image = pygame.image.load(fullname)
    return image


class EmptyBlock(pygame.sprite.Sprite):
    texture = load_image('empty_block.png')

    def __init__(self, *group):
        super().__init__(*group)
        self.image = EmptyBlock.texture
        self.rect = self.image.get_rect()


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[EmptyBlock(sprites) for _ in range(width)] for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        for i in range(self.height):
            for j in range(self.width):
                self.board[i][j].rect.x = self.left + j * self.cell_size
                self.board[i][j].rect.y = self.top + i * self.cell_size

    def get_cell(self, mouse_pos):
        if ((len(self.board) * self.cell_size + self.left < mouse_pos[1] or mouse_pos[1] < self.left)
                or (mouse_pos[0] > len(self.board[0]) * self.cell_size + self.top or mouse_pos[0] < self.top)):
            return None
        x, y = 0, 0
        while (x + 1) * self.cell_size + self.left <= mouse_pos[0]:
            x += 1
        while (y + 1) * self.cell_size + self.top <= mouse_pos[1]:
            y += 1
        board_cords = (x, y)
        return board_cords


sprites = pygame.sprite.Group()
board = Board(10, 20)
board.set_view(20, 20, 35)
running = True
clock = pygame.time.Clock()
tick = 5
pygame.mixer.init()
pygame.mixer.music.load('tetris_soundtrack.mp3')
pygame.mixer.music.play(0)
pygame.mixer.music.set_volume(0.15)
while running:
    pygame.init()
    pygame.display.set_caption('Tetris')
    screen = pygame.display.set_mode((600, 740))
    screen.fill((16, 16, 16))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    board.render()
    sprites.draw(screen)
    pygame.display.flip()
