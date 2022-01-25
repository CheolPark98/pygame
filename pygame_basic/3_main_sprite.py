from turtle import Screen
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

# 캐릭터 (스프라이트) 불러오기
character = pygame.image.load ("D:\\gits\\pygame_basic\\character.png")
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0] # 캐릭터의 가로 크기
character_height = character_size[1] # 캐릭터의 세로 크기
character_x_pos = screen_witdth / 2 - character_width / 2 #  화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height #  화면 세로 크기 가장 아래에 해당하는 곳에 위치

# 이벤트 루프: 대기?
runnig = True
while runnig:
    for event in pygame.event.get(): # 사용자의 동작을 체크: 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: #QUIT 대문자로 적어야함, 창이 닫히는 이벤트가 발생하였는가?
            runnig = False #게임이 진행중이 아님

    screen.blit(background, (0, 0)) # 배경 그리기, (0, 0) 왼쪽 가장 위

    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기

    pygame.display.update() #게임화면을 다시 그리기 pygame은 매 프레임마다 디스플레이를 그려줘야함

pygame.quit()