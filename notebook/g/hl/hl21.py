import pygame
import random

pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# Game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            n1, n2 = random.randint(1,10), random.randint(1,10)

            if event.key == pygame.K_6:
                print(f"My number is {n1}. Your choice is High. Your number is {n2}.")
                print("You win!" if n1 < n2 else "You lose...")

            if event.key == pygame.K_4:
                print(f"My number is {n1}. Your choice is Low. Your number is {n2}.")
                print("You win!" if n1 > n2 else "You lose...")

    # Handle other game logic here

pygame.quit()
