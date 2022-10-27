from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import RPi.GPIO as GPIO
import time

root=Tk()
root.title('login')
root.geometry('1000x350+200+200')
root.configure(bg='#fff')
root.resizable(False,False)

    

def signin():
    username=user.get()
    password=code.get()
    
    if username=='admin' and password=='1234':
        def action2():
            GPIO.setmode(GPIO.BOARD)
            ControlPin= [7,11,13,15]
            for pin in ControlPin:
                GPIO.setup(pin,GPIO.OUT)
                GPIO.output(pin,0)
                    
            seq = [ [1,0,0,0],
                    [1,1,0,0],
                    [0,1,0,0],
                    [0,1,1,0],
                    [0,0,1,0],
                    [0,0,1,1],
                    [0,0,0,1],
                    [1,0,0,1]]
            seq1 = [[1,0,0,1],
                    [0,0,0,1],
                    [0,0,1,1],
                    [0,0,1,0],
                    [0,1,1,0],
                    [0,1,0,0],
                    [1,1,0,0],
                    [1,0,0,0]]


            N = int(entre1.get())
            N1= int(entre2.get())
            N2=0
            if N>0 and N1==0 and N2==0:
                N2=N
                for i in range(N2):
                    for halfstep in range(8):
                        for pin in range(4):
                            GPIO.output(ControlPin[pin], seq[halfstep] [pin])
                        time.sleep(0.001)
                time.sleep(3)
                GPIO.cleanup()
                
            elif N<N1 and N2<N1:
                N2= N1-N
                N=N1
                print("hello")
                for i in range(N2):
                    for halfstep in range(8):
                        for pin in range(4):
                            GPIO.output(ControlPin[pin], seq[halfstep] [pin])
                        time.sleep(0.001)
                time.sleep(3)
                GPIO.cleanup()
            elif N>N1 and N2<N1:
                N2=N-N1
                N=N
                for i in range(N2):
                    for halfstep in range(8):
                        for pin in range(4):
                            GPIO.output(ControlPin[pin], seq1[halfstep] [pin])
                        time.sleep(0.001)
                time.sleep(3)
                GPIO.cleanup()




 
   
        def action():
            GPIO.setmode(GPIO.BOARD)
            ControlPin= [7,11,13,15]
            for pin in ControlPin:
                GPIO.setup(pin,GPIO.OUT)
                GPIO.output(pin,0)
                    
            seq = [ [1,0,0,0],
                    [1,1,0,0],
                    [0,1,0,0],
                    [0,1,1,0],
                    [0,0,1,0],
                    [0,0,1,1],
                    [0,0,0,1],
                    [1,0,0,1]]
            seq1 = [[1,0,0,1],
                    [0,0,0,1],
                    [0,0,1,1],
                    [0,0,1,0],
                    [0,1,1,0],
                    [0,1,0,0],
                    [1,1,0,0],
                    [1,0,0,0]]


                
            N = int(entre1.get())
            N1= 0
            N2 = 0
            print("la valeur de n est",N,N1,N2)
            

            for i in range(N):
                    for halfstep in range(8):
                        for pin in range(4):
                            GPIO.output(ControlPin[pin], seq[halfstep] [pin])
                        time.sleep(0.001)
            time.sleep(3)
            GPIO.cleanup()
        root.destroy()
        fen = Tk()
        fen.geometry("700x420+300+100")
        fen.configure(bg='#fff')
        fen.resizable(False,False)

        
        frame1=Frame(fen,width= 500,height=500,bg="white")
        frame1.place(x=200,y=10)
        
        

        heading=Label(frame1,text='Cutting Control', fg='#57a1f8',bg='white',font=('Microsoft YaHel UI Light',23,'bold'))
        heading.place(x=100,y=10)

        label1 = Label(frame1, text = "Give the length",fg='black',bg='white',font=('Microsoft YaHel UI Light',15))
        label1.place(x=60, y=90 ) 

        entre1= Entry(frame1,width=15 ,fg='black',border=0,bg="white",font=('Microsoft YaHel UI Light',15))
        entre1.place(x =270 , y = 90 )
        button1 = Button(frame1,width=19,pady=7,bg='#57a1f8',fg='white',border=0 ,text = "valider" , command = action )
        button1.place( x = 170 , y = 170)
           
        label2 = Label(frame1, text = "Change The Length",fg='black',bg='white',font=('Microsoft YaHel UI Light',15))
        label2.place(x=60, y=270 ) 
        entre2 = Entry(frame1,width=15 ,fg='black',border=0,bg="white",font=('Microsoft YaHel UI Light',15))
        entre2.place(x =270 , y = 270 )
        button2 = Button(frame1,width=19,pady=7,bg='#57a1f8',fg='white',border=0 ,text = "valider" , command = action2 )
        button2.place( x = 170 , y = 350)
        img1 = PhotoImage(file='motor.png')
        Label(fen,image = img1,bg='white').place(x=0,y=0)
        N1 = int(entre2.get()) 
        
        
    elif username!='admin' and password!='1234':
        messagebox.showerror("Invalid","invalid username and password")
    elif password!='1234':
        messagebox.showerror("Invalid","invalid password")
    elif username!='admin':
        messagebox.showerror("Invalid","invalid username")

img = PhotoImage(file='test1.png')
Label(root,image=img,bg='white').place(x=0,y=0)

frame=Frame(root,width=380,height=300,bg="white")
frame.place(x=590,y=10)

heading=Label(frame,text='Sign In' , fg='#57a1f8',bg='white',font=('Microsoft YaHel UI Light',23,'bold'))
heading.place(x=160,y=10)

################--------------

def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')

user = Entry (frame,width=30,fg='black',border=0,bg="white",font=('Microsoft YaHel UI Light',11))
user.place(x=100,y=100)
user.insert(0,'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame,width=275,height=2,bg='black').place(x=100,y=120)


################--------------


def on_enter(e):
    code.delete(0,'end')

def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0,'Username')
code = Entry (frame,width=30,fg='black',border=0,bg="white",font=('Microsoft YaHel UI Light',11))
code.place(x=100,y=180)
code.insert(0,'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)
Frame(frame,width=275,height=2,bg='black').place(x=100,y=200)

##############################################
Button(frame,width=19,pady=7,text='Sing In',bg='#57a1f8',fg='white',border=0,command=signin).place(x=150,y=270)
label=Label(frame,text="Dont'thave an account?",fg='black',bg='white',font=('Microsoft YaHel UI Light',9))
label.place(x=100, y=220)
sign_up = Button(frame,width=4,text='Sign up',border=0,bg='white',cursor='hand2',fg='#57a1f8')
sign_up.place(x=250,y=215)
root.mainloop()

