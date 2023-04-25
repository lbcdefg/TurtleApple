import turtle
import random as ran
from time import *

# 최고점수파일
file = open(".\\imgs\\max_score.txt", "r", encoding="utf-8")
max_score = file.read().strip()

# 메인화면이 될 스크린과, 객체들을 띄울 turtle(메인화면 터틀로고용이기도 함), 글작성용 writer 터틀객체 생성
screen = turtle.Screen()
screen.setup(width=600, height=800)
screen.title("사과담기게임")
screen.tracer(0)
screen.bgpic(".\\imgs\\appletree2.gif")
screen.update()
turtle.penup()
turtle.hideturtle()
writer = turtle.Turtle(); writer.penup()
writer.penup()
turtle_image = ".\\imgs\\turtlelogo.gif"
turtle.addshape(turtle_image)
writer.shape(turtle_image)
writer.hideturtle()

# 떨어지는 사과 생성
appleli = list()
for i in range(6):
    apple = turtle.Turtle()
    apple_image = ".\\imgs\\apple2.gif"
    turtle.addshape(apple_image)
    apple.shape(apple_image)
    apple.shapesize(30,30)
    apple.penup()
    apple.setheading(270)
    apple.fall_speed = ran.randint(5,20)
    apple.goto(ran.randint(-300,300), ran.randint(500,800))
    appleli.append(apple)

# 떨어지는 폭탄 생성
bombli = []
for i in range(2):
    bomb = turtle.Turtle()
    bomb_image = ".\\imgs\\bomb2.gif"
    turtle.addshape(bomb_image)
    bomb.shape(bomb_image)
    bomb.penup()
    bomb.setheading(270)
    bomb.shapesize(30,30)
    bomb.fall_speed = ran.randint(5,20)
    bomb.goto(ran.randint(-290,290), ran.randint(600,1000))
    bombli.append(bomb)

# 바구니 생성
b = turtle.Turtle()
basket_image = ".\\imgs\\basket2.gif"
turtle.addshape(basket_image)
b.shape(basket_image)
b.shapesize(30,30)
b.penup()
b.goto(0,-350)
b.direction = "right"
b.move_speed = 5

# 거북이 생성
tli = []
t = turtle.Turtle()
turtle_image = ".\\imgs\\turtle.gif"
turtle.addshape(turtle_image)
t.shape(turtle_image)
t.setheading(270)
t.fall_speed = ran.uniform(5,20)
t.penup()
t.goto(-800,-800)
tli.append(t)

# 화면 상단의 SCORE와 LIFE 점수를 지우고 새로 쓰는 함수
def scoreUpdate():
    global score; global life
    turtle.goto(-120,345)
    turtle.clear()
    turtle.write(f"SCORE: {score} Life: {life}", False, align="center", font=("나눔스퀘어 네오 Bold", 25, "bold"))

# 시작화면
def setting():
    global life, score
    writer.hideturtle()
    writer.clear()
    score = 0; life = 3
    writer.goto(0,180)
    writer.write("사과밭의거북이", False, "center", ("나눔스퀘어 네오 Bold",50,"bold"))
    writer.goto(0,-100)
    writer.write("[H]를 눌러 설명 보기!", False, "center", ("나눔스퀘어 네오 Bold",20,"bold"))
    writer.goto(0,-200)
    writer.write("[SPACE]로 시작!", False, "center", ("나눔스퀘어 네오 Bold",40,"bold"))
    #writer.penup()
    writer.goto(0,20)
    writer.showturtle()
    turtle.update()
    scoreUpdate()

# 시작화면에서 [H]를 눌렀을 때 이동하는 게임설명화면
def info():
    writer.hideturtle()
    writer.clear()
    
    #설명용 아이콘(사실은 터틀) 등장
    appleli[0].goto(0,55)
    bombli[0].goto(-100,60)
    t.goto(100,40)
    
    writer.goto(0,150)
    writer.write("게임설명!", False, "center", ("나눔스퀘어 네오 Bold",50,"bold"))
    writer.goto(0,-50)
    writer.write("방향키를 움직여 바구니에 사과를 담으세요!", False, "center", ("나눔스퀘어 네오 Bold",20,"bold"))
    writer.goto(0,-90)
    writer.write("실수로 폭탄을 담으면 LIFE가 깎여요!", False, "center", ("나눔스퀘어 네오 Bold",20,"bold"))
    writer.goto(0,-130)
    writer.write("거북이가 당신을 구해줄거예요!", False, "center", ("나눔스퀘어 네오 Bold",20,"bold"))
    writer.goto(0,-200)
    writer.write("[SPACE]로 시작!", False, "center", ("나눔스퀘어 네오 Bold",40,"bold"))
    writer.penup()
    turtle.update()

# 방향키 좌/우 에 따른 방향설정
def goLeft():
    b.setheading(180)
def goRight():
    b.setheading(0)
turtle.onkeypress(goLeft, "Left")
turtle.onkeypress(goRight, "Right")

# 거북이 등장확률 조정 (등장확률 1%)
def showTurtle():
    r = ran.randint(1,100)
    if r == 1:
        t.goto(ran.randint(-290,290),450)

#게임시작
def playGame():
    global score; global life    
    score = 0; life = 3         #게임 시작시 스코어(0)와 라이프(3) 초기화
    scoreUpdate()
    writer.hideturtle()
    writer.clear()
    
    # 게임설명때 설명하러 나온 폭탄, 사과, 거북이 다시 돌려보내기
    appleli[0].goto(ran.randint(-290,290), 400)
    bombli[0].goto(ran.randint(-290,290), 450)
    t.goto(-800,-800)
    
    #실제 게임 실행
    playing = True
    while playing:
        b.forward(b.move_speed)
        t.forward(t.fall_speed)
        if b.xcor()>=250:
            b.setx(250)
        if b.xcor()<=-250:
            b.setx(-250)
        
        # 바구니에 사과를 담으면 스코어+1, 바구니 이동속도+0.08   
        for apple in appleli:
            apple.forward(apple.fall_speed)
            if apple.distance(b)<50 and b.ycor()-30 <apple.ycor()< b.ycor()+30:
                score += 1
                b.move_speed += 0.08
                apple.goto(ran.randint(-290,290), 400)
                scoreUpdate()
            # 바구니 아래로 떨어지면 다시 위에서부터 떨어지기
            if apple.ycor()<-420:
                apple.goto(ran.randint(-290,290), 400)
        
        # 바구니에 폭탄을 담으면 라이프-1
        for bomb in bombli:
            bomb.forward(bomb.fall_speed) 
            if bomb.distance(b)<70 and b.ycor()-30 <bomb.ycor()< b.ycor()+30:
                life -= 1
                bomb.goto(ran.randint(-290,290), ran.randint(450,550))
                scoreUpdate()
                if life <= 0:
                    gameover()
                    return False
            # 바구니 아래로 떨어지면 다시 위에서부터 떨어지기   
            if bomb.ycor()<-400:
                bomb.goto(ran.randint(-290,290), ran.randint(450,550))
                scoreUpdate()
                
        # 소실된 라이프가 있을 경우 10%의 확률로 거북이 소환 / 거북이를 바구니에 담으면 라이프 +1
        if not life ==3:
            if t.ycor()<-400:  #만약 거북이가 화면안에 있다면 라이프가 없어도 뜨지 않음 => 한 화면에 중복으로 안뜸 
                showTurtle()
        if t.distance(b)<70 and b.ycor()-30<t.ycor()<b.ycor()+30:
            life +=1
            t.goto(-800,-800)
            scoreUpdate()
        turtle.update()
        sleep(0.01)

# 게임오버
def gameover():
    global score
    global max_score
    writer.goto(0,0)
    writer.write("Game Over", False, "center", ("나눔스퀘어 네오 Bold",50,"bold"))
    for apple in appleli:
        apple.goto(ran.randint(-300,300), ran.randint(430,1100))
    for bomb in bombli:
        bomb.goto(ran.randint(-300,300), ran.randint(600,1000))
    writer.goto(0,-100)
    
    if score >= int(max_score):
        max_score = score
        writer.write(f"최고 점수 달성! {max_score}점 입니다!", False, "center", ("나눔스퀘어 네오 Bold",30,"bold"))
        file = open(".\\imgs\\max_score.txt", "w", encoding="utf-8")
        file.write(str(max_score))
    else: 
        writer.write(f"당신의 점수는 {score}점 입니다", False, "center", ("나눔스퀘어 네오 Bold",30,"bold"))   
        writer.goto(0,-150)
        writer.write(f"최고 점수는 {max_score}점 입니다", False, "center", ("나눔스퀘어 네오 Bold",30,"bold"))
    writer.goto(0, -200)
    writer.write(f"[SPACE]를 눌러 다시시작!", False, "center", ("나눔스퀘어 네오 Bold",30,"bold"))
    
turtle.onkeypress(playGame, "space")
turtle.onkeypress(info, "h")

setting()
turtle.listen()
turtle.mainloop()