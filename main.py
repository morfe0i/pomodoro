from tkinter import *
import math
import winsound
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg = GREEN)
    checkmark_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    
    global reps
    reps = 0
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    global reps
    reps +=1
    if reps % 8 == 0:
        countdown(long_break_sec)
        winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
        window.bell()
        timer_label.config(text = "Break", fg = RED)
    elif reps%2 == 0:
        countdown(short_break_sec)
        winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
        timer_label.config(text = "Break", fg = PINK)
    else:
        countdown(work_sec)
        winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
        timer_label.config(text = "Work", fg = GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    global timer
    
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        num_chkmarks = math.floor(reps / 2)
        chkmarks = ""
        for _ in range(num_chkmarks):
            chkmarks += "✔"
        checkmark_label.config(text=chkmarks)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=103, pady=50, bg=YELLOW)
window.after(1000)


canvas = Canvas(width=200, height=224, bg = YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="G:\Python Learning\Tkinter\Pomodoro\Tomato.png")
canvas.create_image(100,112, image=tomato_img)
timer_text = canvas.create_text(103,130, text="00:00", fill="white",font=(FONT_NAME, 35,"bold"))
canvas.grid(column=1, row=1)



timer_label = Label(text="Timer", bg = YELLOW, fg = GREEN, font=(FONT_NAME, 50, "bold"))
timer_label.grid(column=1, row=0)

start_btn = Button(text="Start", font=(FONT_NAME, 10, "bold"), command = start_timer)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="Reset", font=(FONT_NAME, 10, "bold"), command = reset_timer)
reset_btn.grid(column=2, row=2)

# ✔
checkmark_label = Label(fg = GREEN, font=(FONT_NAME, 20, "bold"))
checkmark_label.grid(column=1, row=3)









window.mainloop()