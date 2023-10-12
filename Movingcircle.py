import pygame
import random

COLORS = {
    "red": (255, 0, 0),
    "blue": (0, 0, 255),
    "yellow": (255, 255, 0),
    # Add more colors as needed
}


class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class MovingCircle(Shape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.dx = random.uniform(5, 5)
        self.dy = random.uniform(5, 5)
        self.color = random.choice(list(COLORS.values()))

    def move(self, screen_width, screen_height):
        self.x += self.dx
        self.y += self.dy

        if self.x - self.radius < 0 or self.x + self.radius > screen_width:
            self.dx *= -1
        if self.y - self.radius < 0 or self.y + self.radius > screen_height:
            self.dy *= -1

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)


pygame.init()
screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("circle is moving in a random direction")
running = True
clock = pygame.time.Clock()
players = 7
circles = [MovingCircle(random.randint(0, screen_width), random.randint(0, screen_height), 30) for i in range(players)]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("sky blue")
    for circle in circles:
        circle.move(1280, 720)
        circle.draw(screen)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()