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
    screen.draw.textbox(scrollmess, scroller_box, color = "white")

def update():
    scroller_box.x -= 2

pgzrun.go()