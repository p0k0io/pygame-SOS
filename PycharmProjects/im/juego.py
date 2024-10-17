import pygame
import sys

pygame.init()

width = 800
height = 360
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sostenibilitat")

green = (0, 255, 0)
red = (255, 0, 0)

walk_sprite_sheet = pygame.image.load('Walk.png').convert_alpha()
idle_sprite_sheet = pygame.image.load('Idle.png').convert_alpha()

datacenter = pygame.image.load()
frame_width = 128
frame_height = 128

num_walk_frames = 10
num_idle_frames = 6

walk_frames = []
for i in range(num_walk_frames):
    frame = walk_sprite_sheet.subsurface(pygame.Rect(i * frame_width, 0, frame_width, frame_height))
    walk_frames.append(frame)

idle_frames = []
for i in range(num_idle_frames):
    frame = idle_sprite_sheet.subsurface(pygame.Rect(i * frame_width, 0, frame_width, frame_height))
    idle_frames.append(frame)

sprite_rect = walk_frames[0].get_rect()
sprite_rect.topleft = (100, 100)

max_estado = 100
current_estado = max_estado
estado_decrease_rate = 0.001

horizontal_speed = 1
vertical_speed = 2

frame_index = 0
walk_animation_speed = 0.1
idle_animation_speed = 0.05
frame_timer = 0

clock = pygame.time.Clock()
fps = 60

moving = False
last_moving = False

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    moving = False

    if keys[pygame.K_LEFT]:
        sprite_rect.x -= horizontal_speed
        moving = True
    if keys[pygame.K_RIGHT]:
        sprite_rect.x += horizontal_speed
        moving = True
    if keys[pygame.K_UP]:
        sprite_rect.y -= vertical_speed
        moving = True
    if keys[pygame.K_DOWN]:
        sprite_rect.y += vertical_speed
        moving = True

    current_estado -= estado_decrease_rate
    if current_estado < 0:
        current_estado = 0

    if moving != last_moving:
        frame_index = 0
        frame_timer = 0

    if moving:
        frame_timer += walk_animation_speed
        if frame_timer >= 1:
            frame_timer = 0
            frame_index = (frame_index + 1) % num_walk_frames
    else:
        frame_timer += idle_animation_speed
        if frame_timer >= 1:
            frame_timer = 0
            frame_index = (frame_index + 1) % num_idle_frames

    screen.fill(green)

    if moving and keys[pygame.K_LEFT]:
        screen.blit(pygame.transform.flip(walk_frames[frame_index], True, False), sprite_rect)
    elif moving:
        screen.blit(walk_frames[frame_index], sprite_rect)
    else:
        screen.blit(idle_frames[frame_index], sprite_rect)

    estado_bar_width = 200
    estado_bar_height = 20
    estado_ratio = current_estado / max_estado

    pygame.draw.rect(screen, (150, 0, 0), (50, 50, estado_bar_width, estado_bar_height))
    pygame.draw.rect(screen, red, (50, 50, estado_bar_width * estado_ratio, estado_bar_height))
    pygame.image.load('Sprite.png')
    pygame.display.flip()

    clock.tick(fps)
    last_moving = moving

pygame.quit()
sys.exit()
