import pygame
import time

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Simulated LED Blinker")

# Define colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# LED position and radius
led_pos = (150, 150)
radius = 40

# Function to draw LED
def draw_led(state):
    screen.fill(BLACK)
    color = GREEN if state else RED
    pygame.draw.circle(screen, color, led_pos, radius)
    pygame.display.flip()

# Main simulation loop (10 blinks)
for i in range(10):
    draw_led(True)
    time.sleep(0.5)
    draw_led(False)
    time.sleep(0.5)

# Hold screen for a bit before exit
time.sleep(5)
pygame.quit()
