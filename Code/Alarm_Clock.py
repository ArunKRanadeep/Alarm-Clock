from threading import Thread
from tkinter.ttk import *
from tkinter import *

from PIL import ImageTk,Image
from pygame import mixer

from datetime import datetime
from time import sleep

#color
bg_color="#3D8EA4"
co1="blue"
co2="black"

#window
window=Tk()
window.title("Alarm Clock")
window.geometry('380x180')
window.configure(bg=bg_color)

#frames_UP
frame_line=Frame(window,width=400,height=6,bg=co1)
frame_line.grid(row=0,column=0)

frame_body=Frame(window,width=400,height=290,bg=bg_color)
frame_body.grid(row=1,column=0)

#Frame_body
img=Image.open("d:\Python Project Intern\Alarm Clock_Project_3\Icon\icons8-alarm-clock-100.png")
img.resize((100,100))
img=ImageTk.PhotoImage(img)

app_image=Label(frame_body,height=100,image=img,bg=bg_color)
app_image.place(x=10,y=10)

name=Label(frame_body,text="Alarm",height=1,font=('lvy 18 bold'),bg=bg_color)
name.place(x=125,y=2)

#hour
hr=Label(frame_body,text="Hour",height=1,font=('lvy 12 bold'),bg=bg_color,fg='#152C24')
hr.place(x=127,y=40)
c_hr=Combobox(frame_body,width=2,font=('arial 15'))
c_hr['values']=("00","01","02","03","04","05","06","07","08","09","10","11","12")
c_hr.current(0)
c_hr.place(x=130,y=60)


#mins
mins=Label(frame_body,text="Min",height=1,font=('lvy 12 bold'),bg=bg_color,fg='#152C24')
mins.place(x=177,y=40)
c_mins=Combobox(frame_body,width=2,font=('arial 15'))
c_mins['values']=("00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59")
c_mins.current(0)
c_mins.place(x=180,y=60)

#Sec
sec=Label(frame_body,text="Sec",height=1,font=('lvy 12 bold'),bg=bg_color,fg='#152C24')
sec.place(x=225,y=40)
c_sec=Combobox(frame_body,width=2,font=('arial 15'))
c_sec['values']=("00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59")
c_sec.current(0)
c_sec.place(x=230,y=60)


#Period
Period=Label(frame_body,text="Period",height=1,font=('lvy 12 bold'),bg=bg_color,fg='#152C24')
Period.place(x=300,y=40)
c_Period=Combobox(frame_body,width=3,font=('arial 15'))
c_Period['values']=("AM","PM")
c_Period.current(0)
c_Period.place(x=300,y=60)


def activate_alarm():
    t =Thread(target=alarm)
    t.start()

def deactivate_alarm():
    print("Deactivated alarm: ",selected.get())
    mixer.music.stop()
    
    


selected=IntVar()
rad1=Radiobutton(frame_body,font=('arial 10 bold'),value=1,text="Activate",bg=bg_color,command=activate_alarm,variable=selected)
rad1.place(x=125,y=95)


def sound_alarm():
    mixer.music.load('Music/dawn_chorus.mp3')
    mixer.music.play()
    selected.set(0)

    rad2=Radiobutton(frame_body,font=('arial 10 bold'),value=2,text="Deactivate",bg=bg_color,command=deactivate_alarm,variable=selected)
    rad2.place(x=187,y=95)

def alarm():
    while True:
        control =selected.get()
        print(control)

        alarm_hour=c_hr.get()
        alarm_mint=c_mins.get()
        alarm_sec=c_sec.get()
        alarm_period=c_Period.get()
        alarm_period=str(alarm_period).upper()

        now=datetime.now()

        hour=now.strftime("%I")
        mint=now.strftime("%M")
        sec=now.strftime("%S")
        period=now.strftime("%p")

        if control==1:
            if alarm_period==period:
                if alarm_hour==hour:
                    if alarm_mint==mint:
                        if alarm_sec==sec:
                            print("Time to take brake ")
                            sound_alarm()
        sleep(1)   

mixer.init()



window.mainloop()