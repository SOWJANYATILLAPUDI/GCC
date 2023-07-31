import pygame
import time
import random

pygame.init()

# Set up the screen dimensions
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Snake direction
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

def draw_grid():
    for x in range(0, WIDTH, GRID_SIZE):
        pygame.draw.line(screen, WHITE, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, WHITE, (0, y), (WIDTH, y))

def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, WHITE, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

def draw_apple(apple):
    pygame.draw.rect(screen, RED, (apple[0] * GRID_SIZE, apple[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

def get_random_position():
    return random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1)

def main():
    snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
    snake_direction = RIGHT

    apple = get_random_position()

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_direction != DOWN:
                    snake_direction = UP
                elif event.key == pygame.K_DOWN and snake_direction != UP:
                    snake_direction = DOWN
                elif event.key == pygame.K_LEFT and snake_direction != RIGHT:
                    snake_direction = LEFT
                elif event.key == pygame.K_RIGHT and snake_direction != LEFT:
                    snake_direction = RIGHT

        # Move the snake
        head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])
        snake.insert(0, head)

        # Check if the snake eats the apple
        # Check if the snake eats the apple
        if tuple(snake[0]) == tuple(apple):
             apple = get_random_position()
        else:
            snake.pop()

        """
        ----------------------------------------------
        if snake[0] == apple:
            apple = get_random_position()
        else:
            snake.pop()
        """

        # Check for game over conditions
        if snake[0][0] < 0 or snake[0][0] >= GRID_WIDTH or snake[0][1] < 0 or snake[0][1] >= GRID_HEIGHT:
            pygame.quit()
            quit()

        if snake[0] in snake[1:]:
            pygame.quit()
            quit()

        # Clear the screen
        screen.fill(BLACK)

        # Draw elements
        draw_grid()
        draw_apple(apple)
        draw_snake(snake)

        pygame.display.update()

        # Set the game speed (adjust as needed)
        clock.tick(10)

if __name__ == "__main__":
    main()
