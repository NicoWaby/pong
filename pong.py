import pygame
import random
import time
# Set up pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("pong")
clock = pygame.time.Clock()
points1 = 0
points2 = 0

icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

font = pygame.font.Font(None, 64)
text1 = font.render(f"{points1}", True, (255, 255, 255))
text1_pos = text1.get_rect(centerx=screen.get_width() / 3, y= 10)
font = pygame.font.Font(None, 64)
text2 = font.render(f"{points2}", True, (255, 255, 255))
text2_pos = text2.get_rect(centerx=(screen.get_width() / 3) * 2, y= 10)

dt = 0

player1_x = screen.get_width() / 15
player1_y = screen.get_height() / 2 - 50
player2_x = screen.get_width() / 15 * 14
player2_y = screen.get_height() / 2 - 50
circle_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
circle_dirx = -6
circle_diry = -3

running = True
#Loop that repeats every frame
while running:
    # Check for events
    for event in pygame.event.get():
        # If the user clicks the x, it sends the QUIT event and closes
        if event.type == pygame.QUIT:
            running = False
    # Fills screen to wipe anything from the last frame
    screen.fill((0,0,0))
    # Render the rest of the game here
    pygame.draw.rect(screen, (255, 255, 255), (player1_x, player1_y, 20, 100))
    pygame.draw.rect(screen, (255, 255, 255), (player2_x, player2_y, 20, 100))
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if player1_y >= 0:
            player1_y -= 500 * dt
    if keys[pygame.K_s]:
        if player1_y <= 620:
            player1_y += 500 * dt
    if keys[pygame.K_UP]:
        if player2_y >= 0:
            player2_y -= 500 * dt
    if keys[pygame.K_DOWN]:
        if player2_y <= 620:
            player2_y += 500 * dt
    
    circle_pos += (circle_dirx, circle_diry)
    pygame.draw.circle(screen, (255, 255, 255), circle_pos, 10)
    ball_x = circle_pos.x
    ball_y = circle_pos.y
    ball = pygame.Rect(ball_x, ball_y, 10, 10)
    player1 = pygame.Rect((player1_x + 10), player1_y, 20, 100)
    player2 = pygame.Rect((player2_x - 10), player2_y, 20, 100)
    top = pygame.Rect(0, -40, 1280, 50)
    bottom =  pygame.Rect(0, 720, 1280, 50)
    left = pygame.Rect(-70, 0, 80, 720)
    right = pygame.Rect(1270, 0, 80, 720)
    if player1.collidepoint(ball_x, ball_y):
        circle_dirx *= -1
        circle_diry *= -1 + random.randint(-5, 5)
        if circle_diry <= 0:
            if circle_diry >= -3:
                circle_diry += -2
        if circle_diry >= 0:
            if circle_diry <= 3:
                circle_diry += 2
    if player2.collidepoint(ball_x, ball_y):
        circle_dirx *= -1
        circle_diry *= -1 + random.randint(-5, 5)
        if circle_diry <= 0:
            if circle_diry >= -3:
                circle_diry += -2
        if circle_diry >= 0:
            if circle_diry <= 3:
                circle_diry += 2
    if left.collidepoint(ball_x, ball_y):
        points2 += 1
        print(points2, "points for player 2")
        time.sleep(1)
        circle_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
        circle_dirx = 6
        circle_diry = -3
    if right.collidepoint(ball_x, ball_y):
        points1 += 1
        print(points1, "points for player 1")
        time.sleep(1)
        circle_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
        circle_dirx = -6
        circle_diry = -3
    if top.collidepoint(ball_x, ball_y):
        circle_diry *= -1
    if bottom.collidepoint(ball_x, ball_y):
        circle_diry *= -1
    if circle_dirx >= 30:
        circle_dirx = 30
    if circle_dirx <= -30:
        circle_dirx = -30
    if circle_diry >= 15:
        circle_diry = 15
    if circle_diry <= -15:
        circle_diry = -15
    
    text1 = font.render(f"{points1}", True, (255, 255, 255))
    text2 = font.render(f"{points2}", True, (255, 255, 255))
    screen.blit(text1, text1_pos)
    screen.blit(text2, text2_pos)
      
    # flip() displays the changes on the screen
    pygame.display.flip()
    
    clock.tick(60) # Limits the framerate
    dt = clock.tick(60) / 1000

pygame.quit()
