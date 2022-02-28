import pygame, sys, random

#gen stepup
pygame.init()
clock = pygame.time.Clock()

#setting up main window
screen_width = 1200
screen_height = 800

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Simple Pong by Nicodemus Robles")

ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)


bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)
game_font = pygame.font.Font("freesansbold.ttf", 24)

#game vars
ball_speed_x = 7
ball_speed_y = 7

player_speed = 0
opponent_speed = 7

player_score = 0
opponet_score = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


        #player keys
        if event.type == pygame.KEYDOWN:
            if event.key ==  pygame. K_DOWN:
                player_speed += 7
            if event.key ==  pygame. K_UP:
                player_speed -= 7

        if event.type == pygame.KEYUP:
            if event.key ==  pygame. K_DOWN:
                player_speed -= 7
            if event.key ==  pygame. K_UP:
                player_speed += 7

    #player Animation
    player.y += player_speed
    
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

    #opponente Animation
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

    #Ball animation
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top < 0 or ball.bottom > screen_height:
        ball_speed_y *= -1
        
    #game over
    if ball.left < 0:
        ball.center = (screen_width/2,screen_height/2)
        ball_speed_x = 7 * random.choice((1,-1))
        ball_speed_y = 7 * random.choice((1,-1))
        player_score += 1

    if ball.right > screen_width:
        ball.center = (screen_width/2,screen_height/2)
        ball_speed_x = 7 * random.choice((1,-1))
        ball_speed_y = 7 * random.choice((1,-1))
        opponet_score += 1


    #Ball Collision
    if ball.colliderect(player) and ball_speed_x > 0:
        ball_speed_x *= -1
    if ball.colliderect(opponent) and ball_speed_x < 0:
        ball_speed_x *= -1


    #visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, ball)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.aaline(screen, light_grey, (screen_width/2,0), (screen_width/2, screen_height) )

    #update text
    player_text = game_font.render(f"{player_score}",False, light_grey)
    screen.blit(player_text, (610,350))

    opponent_text = game_font.render(f"{opponet_score}",False, light_grey)
    screen.blit(opponent_text, (580,350))
    
    #update window
    pygame.display.flip()
    clock.tick(60)
