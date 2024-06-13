import pygame
import random

# 初始化Pygame
pygame.init()

# 设置窗口大小和标题
screen = pygame.display.set_mode((400, 500))
pygame.display.set_caption('2048')

# 定义颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
COLORS = {
    0: (205, 193, 180),
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46)
}

# 字体设置
font = pygame.font.Font(None, 60)
small_font = pygame.font.Font(None, 30)

def initialize_game():
    board = [[0] * 4 for _ in range(4)]
    add_new_tile(board)
    add_new_tile(board)
    return board

def add_new_tile(board):
    empty_tiles = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if empty_tiles:
        i, j = random.choice(empty_tiles)
        board[i][j] = random.choice([2, 4])

def draw_board(board):
    screen.fill(WHITE)
    for i in range(4):
        for j in range(4):
            value = board[i][j]
            color = COLORS.get(value, BLACK)
            pygame.draw.rect(screen, color, (j * 100, i * 100 + 100, 100, 100))
            if value != 0:
                text = font.render(str(value), True, BLACK)
                text_rect = text.get_rect(center=(j * 100 + 50, i * 100 + 150))
                screen.blit(text, text_rect)

    # 绘制控制按钮
    pygame.draw.rect(screen, GRAY, (50, 450, 100, 40))
    pygame.draw.rect(screen, GRAY, (250, 450, 100, 40))
    pygame.draw.rect(screen, GRAY, (150, 400, 100, 40))
    pygame.draw.rect(screen, GRAY, (150, 450, 100, 40))
    
    left_text = small_font.render("Left", True, BLACK)
    screen.blit(left_text, (85, 460))
    right_text = small_font.render("Right", True, BLACK)
    screen.blit(right_text, (285, 460))
    up_text = small_font.render("Up", True, BLACK)
    screen.blit(up_text, (185, 410))
    down_text = small_font.render("Down", True, BLACK)
    screen.blit(down_text, (185, 460))

def slide_left(row):
    new_row = [i for i in row if i != 0]
    new_row += [0] * (4 - len(new_row))
    return new_row

def combine_row(row):
    for i in range(3):
        if row[i] == row[i + 1] and row[i] != 0:
            row[i] *= 2
            row[i + 1] = 0
    return row

def move_left(board):
    new_board = []
    for row in board:
        new_row = slide_left(row)
        new_row = combine_row(new_row)
        new_row = slide_left(new_row)
        new_board.append(new_row)
    return new_board

def reverse(row):
    return row[::-1]

def transpose(board):
    return [list(row) for row in zip(*board)]

def move_right(board):
    new_board = [reverse(row) for row in board]
    new_board = move_left(new_board)
    new_board = [reverse(row) for row in new_board]
    return new_board

def move_up(board):
    new_board = transpose(board)
    new_board = move_left(new_board)
    new_board = transpose(new_board)
    return new_board

def move_down(board):
    new_board = transpose(board)
    new_board = move_right(new_board)
    new_board = transpose(new_board)
    return new_board

def is_game_over(board):
    for row in board:
        if 0 in row:
            return False
    for i in range(4):
        for j in range(3):
            if board[i][j] == board[i][j + 1] or board[j][i] == board[j + 1][i]:
                return False
    return True

def make_move(board, move):
    if move == 'left':
        new_board = move_left(board)
    elif move == 'right':
        new_board = move_right(board)
    elif move == 'up':
        new_board = move_up(board)
    elif move == 'down':
        new_board = move_down(board)
    else:
        return board

    if new_board != board:
        add_new_tile(new_board)
    return new_board

def main():
    board = initialize_game()
    clock = pygame.time.Clock()
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 50 <= x <= 150 and 450 <= y <= 490:
                    board = make_move(board, 'left')
                elif 250 <= x <= 350 and 450 <= y <= 490:
                    board = make_move(board, 'right')
                elif 150 <= x <= 250 and 400 <= y <= 440:
                    board = make_move(board, 'up')
                elif 150 <= x <= 250 and 450 <= y <= 490:
                    board = make_move(board, 'down')
        
        if is_game_over(board):
            game_over = True

        draw_board(board)
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
