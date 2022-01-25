from threading import Timer
from turtle import Screen, width
import pygame

pygame.init() # 초기화 반드시 필요

#화면 크기 설정
screen_witdth = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_witdth, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Basic Game") # 게임 이름

# 배경 이미지 불러오기
background = pygame.image.load("D:\\gits\\pygame_basic\\background.png")  #파일 경로 구하기 copy path

# FPS
clock = pygame.time.Clock()
# 캐릭터 (스프라이트) 불러오기
character = pygame.image.load ("D:\\gits\\pygame_basic\\character.png")
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0] # 캐릭터의 가로 크기
character_height = character_size[1] # 캐릭터의 세로 크기
character_x_pos = screen_witdth / 2 - character_width / 2 #  화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height #  화면 세로 크기 가장 아래에 해당하는 곳에 위치

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.6

# 적 enemy 캐릭터
enemy = pygame.image.load ("D:\\gits\\pygame_basic\\enemy.png")
enemy_size = enemy.get_rect().size # 이미지의 크기를 구해옴
enemy_width = enemy_size[0] # 캐릭터의 가로 크기
enemy_height = enemy_size[1] # 캐릭터의 세로 크기
enemy_x_pos = screen_witdth / 2 - enemy_width / 2 #  화면 가로의 절반 크기에 해당하는 곳에 위치
enemy_y_pos = screen_height/2 - enemy_height/2 #  화면 세로 크기 가장 아래에 해당하는 곳에 위치

# 폰트 정의
game_font= pygame.font.Font(None, 40)# 폰트 객체 생성 (폰트, 크기)

#총 시간 
total_time = 10

# 시간 계산
start_ticks = pygame.time.get_ticks()  # 시간 tick을 받아옴

# 이벤트 루프: 대기?
runnig = True
while runnig:
    dt = clock.tick(60) #원하는 프레임 수
    print("fps : " + str(clock.get_fps()))
    
    for event in pygame.event.get(): # 사용자의 동작을 체크: 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: #QUIT 대문자로 적어야함, 창이 닫히는 이벤트가 발생하였는가?
            runnig = False #게임이 진행중이 아님

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
        
        #경계값 처리
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    
    
    #캐릭터 위치 변환
    character_x_pos += to_x * dt # 프레임과 상관없이 이동 속도 일정하게 하기
    character_y_pos += to_y * dt

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_witdth - character_width:
        character_x_pos = screen_witdth - character_width

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

     #충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect() #rect 정보 = 좌표, width, height
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect() #rect 정보 = 좌표, width, height
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    
    #충돌체크
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        runnig = False # 게임종료
  
    screen.blit(background, (0, 0)) # 배경 그리기, (0, 0) 왼쪽 가장 위

    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기

    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) #적그리기

    # 타이머 집어 넣기
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 
    #경과 시간을 1000으로 나누어서 초 단위로 표시 ms/1000 = s

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255)) #초 단위로 자르기위해 int

    screen.blit(timer, (10,10))
    
    #만약 시간이 0 이하라면 게임종료
    if total_time - elapsed_time <=0:
        print("타임아웃")
        runnig = False

    pygame.display.update() #게임화면을 다시 그리기 pygame은 매 프레임마다 디스플레이를 그려줘야함


# 잠시 대기
pygame.time.delay(2000) 


pygame.quit()