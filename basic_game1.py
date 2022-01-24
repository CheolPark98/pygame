import random
import pygame

####################################################
#기본초기화 (반드시 해야 하는 것들)
pygame.init() # 초기화 반드시 필요

#화면 크기 설정
screen_witdth = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_witdth, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Basic Game") # 게임 이름

# FPS
clock = pygame.time.Clock()
#####################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 폰트등)
background = pygame.image.load("D:\gits\pygame_basic\다운로드.jpg")

chracter = pygame.image.load("D:\gits\pygame_basic\images.jpg")
chracter_size = chracter.get_rect().size
chracter_width = chracter_size[0]
chracter_height = chracter_size[1]
chracter_x_pos = screen_witdth/2 - chracter_width/2
chracter_y_pos = screen_height - chracter_height

to_x = 0
chracter_speed = 10

enemy1 = pygame.image.load ("D:\gits\pygame_basic\images.png")
enemy1_size = enemy1.get_rect().size # 이미지의 크기를 구해옴
enemy1_width = enemy1_size[0] # 캐릭터의 가로 크기
enemy1_height = enemy1_size[1] # 캐릭터의 세로 크기
enemy1_x_pos = random.randint(0, screen_witdth-screen_witdth) #  화면 가로의 절반 크기에 해당하는 곳에 위치
enemy1_y_pos = 0
enemy1_speed = 10

enemy2 = pygame.image.load ("D:\gits\pygame_basic\images.png")
enemy2_size = enemy2.get_rect().size # 이미지의 크기를 구해옴
enemy2_width = enemy2_size[0] # 캐릭터의 가로 크기
enemy2_height = enemy2_size[1] # 캐릭터의 세로 크기
enemy2_x_pos = random.randint(0, screen_witdth-screen_witdth) #  화면 가로의 절반 크기에 해당하는 곳에 위치
enemy2_y_pos = 0
enemy2_speed = 15

# 이벤트 루프: 대기?
runnig = True
while runnig:
    dt = clock.tick(30) #원하는 프레임 수
 
    
    # 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get(): # 사용자의 동작을 체크: 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: #QUIT 대문자로 적어야함, 창이 닫히는 이벤트가 발생하였는가?
            runnig = False #게임이 진행중이 아님

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= chracter_speed
            elif event.key == pygame.K_RIGHT:
                to_x += chracter_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    # # 3. 게임 캐릭터 위치 정의
    chracter_x_pos += to_x

    if chracter_x_pos < 0:
        chracter_x_pos=0
    elif chracter_x_pos > screen_witdth - chracter_width:
        chracter_x_pos = screen_witdth -chracter_width

    enemy1_y_pos += enemy1_speed
    enemy2_y_pos += enemy2_speed


    if enemy1_y_pos > screen_height:
        enemy1_y_pos=0
        enemy1_x_pos=random.randint(0, screen_witdth-enemy1_width)

    if enemy2_y_pos > screen_height:
        enemy2_y_pos=0
        enemy2_x_pos=random.randint(0, screen_witdth-enemy2_width)
    # 4. 충돌 처리
    chracter_rect = chracter.get_rect()
    chracter_rect.left = chracter_x_pos
    chracter_rect.top = chracter_y_pos

    enemy1_rect = enemy1.get_rect()
    enemy1_rect.left = enemy1_x_pos
    enemy1_rect.top = enemy1_y_pos
    enemy2_rect = enemy1.get_rect()
    enemy2_rect.left = enemy2_x_pos
    enemy2_rect.top = enemy2_y_pos

    if chracter_rect.colliderect(enemy1_rect):
        print("충돌했어요!")
        runnig = False
    if chracter_rect.colliderect(enemy2_rect):
        print("충돌했어요!")
        runnig = False

        # 5. 화면에 그리기
    screen.blit(background, (0,0))

    screen.blit(chracter, (chracter_x_pos, chracter_y_pos))

    screen.blit(enemy1, (enemy1_x_pos,enemy1_y_pos))
    screen.blit(enemy2, (enemy2_x_pos,enemy2_y_pos))

    pygame.display.update()


pygame.quit()