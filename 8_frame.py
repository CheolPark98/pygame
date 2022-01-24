

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


# 이벤트 루프: 대기?
runnig = True
while runnig:
    dt = clock.tick(30) #원하는 프레임 수
    print("fps : " + str(clock.get_fps()))
    
    # 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get(): # 사용자의 동작을 체크: 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: #QUIT 대문자로 적어야함, 창이 닫히는 이벤트가 발생하였는가?
            runnig = False #게임이 진행중이 아님

        # 3. 게임 캐릭터 위치 정의
        
        # 4. 충돌 처리

        # 5. 화면에 그리기

        pygame.display.update()


    

  


pygame.quit()