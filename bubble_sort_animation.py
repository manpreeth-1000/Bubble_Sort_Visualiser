import pygame
import random
import sys

pygame.init()

data = [random.randint(1, 30) for _ in range(10)]     # if we want to visualize bubble sort on array of our choice, we can define data directly i.e without random
n = len(data)
screen_width = 800
screen_height = 400
bubble_radius = 20
bubble_spacing = 10
bubble_speed = 1
bubble_color = (0, 128, 255)
background_color = (255, 255, 255)
font_color = (0, 0, 0)
intro_text_color = (255, 0, 0)
intro_text = "Bubble Sort"
intro_text_size = 48
intro_duration = 5

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bubble Sort Animation")

def bubble_sort_animation(data):
    n = len(data)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, n):
            if data[i - 1] > data[i]:
                data[i - 1], data[i] = data[i], data[i - 1]
                swapped = True
            yield data

bubble_positions = [(i * (bubble_radius * 2 + bubble_spacing) + bubble_radius, screen_height // 2) for i in range(n)]
bubble_colors = [bubble_color for _ in range(n)]

clock = pygame.time.Clock()

intro_font = pygame.font.Font(None, intro_text_size)
intro_text = intro_font.render(intro_text, True, intro_text_color)
intro_text_rect = intro_text.get_rect(center=(screen_width // 2, screen_height // 2))
intro_duration = intro_duration * 1000
intro_frame_count = 0

running = True
sort_animation = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if intro_frame_count < intro_duration:
        screen.fill(background_color)
        screen.blit(intro_text, intro_text_rect)
        pygame.display.flip()
        intro_frame_count += 1

    elif sort_animation is None:
        sort_animation = bubble_sort_animation(data)

    try:
        if sort_animation:
            current_state = next(sort_animation)

            screen.fill(background_color)

            for i, value in enumerate(current_state):
                x, y = bubble_positions[i]
                pygame.draw.circle(screen, bubble_colors[i], (x, y), bubble_radius)
                font = pygame.font.Font(None, 36)
                text_surface = font.render(str(value), True, font_color)
                text_rect = text_surface.get_rect(center=(x, y))
                screen.blit(text_surface, text_rect)

            for i in range(n):
                x, y = bubble_positions[i]
                target_x = i * (bubble_radius * 2 + bubble_spacing) + bubble_radius
                if x < target_x:
                    bubble_positions[i] = (x + bubble_speed, y)
                elif x > target_x:
                    bubble_positions[i] = (x - bubble_speed, y)
                bubble_colors[i] = tuple(min(c + 2, 255) for c in bubble_colors[i])

            pygame.display.flip()
            clock.tick(1)

    except StopIteration:
        pass

pygame.quit()
sys.exit()