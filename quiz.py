import pgzrun

TITLE = "quizz"
WIDTH = 860
HEIGHT = 600

scroller_box = Rect(0, 0, 860, 80)
q_box = Rect(20, 100, 630, 100)
time_box = Rect(670, 100, 170, 100)
skip_bu = Rect(670, 220, 170, 340)
abox_l1 = Rect(20, 220, 300, 100)
abox_l2 = Rect(20, 340, 300, 100)
abox_r1 = Rect(340, 220, 300, 100)
abox_r2 = Rect(340, 340, 300, 100)

current_q = 0
total_q = 0
timerrrr = 10
gameovere = False
score = 0

questiions = []
all = [abox_l1, abox_l2, abox_r1, abox_r2]

def draw():
    screen.clear()
    screen.fill("ghost white")
    screen.draw.filled_rect(scroller_box, "pale violet red")
    screen.draw.filled_rect(q_box, "pink")
    screen.draw.filled_rect(time_box, "light pink")
    screen.draw.filled_rect(skip_bu, "misty rose")
    screen.draw.filled_rect(abox_l1, "old lace")
    screen.draw.filled_rect(abox_l2, "ivory")
    screen.draw.filled_rect(abox_r1, "ivory")
    screen.draw.filled_rect(abox_r2, "old lace")
    scrollmess = f"Welcome to quizz... Q:{current_q}/{total_q}"
    screen.draw.textbox(scrollmess, scroller_box, color = "snow")
    screen.draw.textbox(q[0], q_box, color = "snow")
    screen.draw.textbox(q[1].strip(), abox_l1, color = "pink")
    screen.draw.textbox(q[2].strip(), abox_l2, color = "pink")
    screen.draw.textbox(q[3].strip(), abox_r1, color = "pink")
    screen.draw.textbox(q[4].strip(), abox_r2, color = "pink")
    screen.draw.textbox(str(timerrrr), time_box, color = "white")
    screen.draw.textbox("skip", skip_bu, color = "white")

def update():
    scroller_box.x -= 2
    if scroller_box.right < 0:
        scroller_box.x = 860

def questread():
    global questiions, total_q
    with open("questions.txt", "r") as file:
        for i in file:
            questiions.append(i)
            total_q += 1

def displaynextquest():
    global current_q
    current_q += 1
    return questiions.pop(0).split("|")

def on_mouse_down(pos):
    index = 1
    for i in all:
        if i.collidepoint(pos):
            if i is int(q[5]):
                anstick()
            else:
                gmaend()
        index += 1

def anstick():
    global q, questiions, score, timerrrr
    score += 1
    if questiions:
         q = displaynextquest()
         timerrrr = 10
    else:
        gmaend()

def gmaend():
    global timerrrr, gameovere, q
    message = f"G-G-G-G-G-G-Game oooooovvvvver!\nYou got {score} questions correct!"
    q = [message, "-", "-", "-", "-", 5]
    timerrrr = 0
    gameovere = True


questread()

q = displaynextquest()
print(q)

pgzrun.go()