from tkinter import *
from tkinter import messagebox
import pyautogui as pg
from eq_solver import eq_solver


class setting():
    def fun_1():
        pg.getWindowsWithTitle("Calculator")[0].activate()
        input_from_cal.focus()
        pg.press("num1")
    def fun_2():
        pg.getWindowsWithTitle("Calculator")[0].activate()
        input_from_cal.focus()
        pg.press("num2")
    def fun_3():
        pg.getWindowsWithTitle("Calculator")[0].activate()
        input_from_cal.focus()
        pg.press("num3")
    def fun_4():
        pg.getWindowsWithTitle("Calculator")[0].activate()
        input_from_cal.focus()
        pg.press("num4")
    def fun_5():
        pg.getWindowsWithTitle("Calculator")[0].activate()
        input_from_cal.focus()
        pg.press("num5")
    def fun_6():
        pg.getWindowsWithTitle("Calculator")[0].activate()
        input_from_cal.focus()
        pg.press("num6")
    def fun_7():
        pg.getWindowsWithTitle("Calculator")[0].activate()
        input_from_cal.focus()
        pg.press("num7")
    def fun_8():
        pg.getWindowsWithTitle("Calculator")[0].activate()
        input_from_cal.focus()
        pg.press("num8")
    def fun_9():
        pg.getWindowsWithTitle("Calculator")[0].activate()
        input_from_cal.focus()
        pg.press("num9")
    def fun_0():
        pg.getWindowsWithTitle("Calculator")[0].activate()
        input_from_cal.focus()
        pg.press("num0")

    def fun_add():
        pg.getWindowsWithTitle("Calculator")[0].activate()
        input_from_cal.focus()
        pg.press("+")

    def fun_sub():
        pg.getWindowsWithTitle("Calculator")[0].activate()
        input_from_cal.focus()
        pg.press("-")

    def fun_div():
        pg.getWindowsWithTitle("Calculator")[0].activate()
        input_from_cal.focus()
        pg.press("/")

    def fun_mul():
        pg.getWindowsWithTitle("Calculator")[0].activate()
        input_from_cal.focus()
        pg.press("*")

    def fun_dot():
        pg.getWindowsWithTitle("Calculator")[0].activate()
        input_from_cal.focus()
        pg.press(".")
    
    def fun_back():
        pg.getWindowsWithTitle("Calculator")[0].activate()
        input_from_cal.focus()
        pg.press("backspace")
    
    def fun_clear():
        pg.getWindowsWithTitle("Calculator")[0].activate()
        input_from_cal.focus()
        pg.keyDown("ctrl")
        pg.press("a")
        pg.keyUp("ctrl")
        pg.press("backspace")

    def fun_enter():
        
        
        
        
        ########### main solution algorethom  ############
        eq_string = input_from_cal.get()

        bodmas_rule = ["/", "*", "+", "-"]
        
        result = eq_solver(eq_string)
        if result == None:
            input_from_cal.focus()
        else:
            print(result)
            setting.fun_clear()
            
            pg.typewrite(str(result))
        
        '''
        eq_string = eq_string.replace("+"," + ")
        eq_string = eq_string.replace("-"," - ")
        eq_string = eq_string.replace("/"," / ")
        eq_string = eq_string.replace("*"," * ")
        lis = eq_string.split(" ")
        
        ###  if the eq starts with + or - then insert the 0 to the first position 
        # example : if eq = -2+3  then convert it into  : 0-2+3
        if lis[0] == "":
            if lis[1] == "+" or lis[1]=="-":
                lis[0] = "0"
                  
        for l in range(0, len(bodmas_rule)):
            for i in range(0, lis.count(bodmas_rule[l])):
                op_index = lis.index(bodmas_rule[l])
                try:
                    first_num = float(lis[op_index-1])
                    second_num = float(lis[op_index+1])
                except Exception as e:
                    print(e)
                    messagebox.showerror("Error", "You equation is not valid! :-]")
                if lis[op_index] == "+":
                    result = first_num + second_num
                elif lis[op_index] == "-":
                    result = first_num - second_num
                elif lis[op_index] == "*":
                    result = first_num * second_num
                elif lis[op_index] == "/":
                    result = first_num / second_num
                else:
                    messagebox.showerror("Error", "You entered wrong operator")
                lis.remove(lis[op_index-1])
                lis.remove(lis[op_index-1])
                lis.remove(lis[op_index-1])
                lis.insert(op_index-1,result)

        print("result full list : ",lis)
        print("result = ",lis[0])
        setting.fun_clear()
        input_from_cal.focus()
        val = str(lis[0])
        pg.typewrite(val)
        print("done")
        '''
        

    def but_(master, text="NONE", command=None, place=[0,0]):
        b = Button(master=master, text=text,command=command, font=("AREAL",18), bg="gray60", fg="white")
        b.place(x=place[0], y=place[1])


if __name__=="__main__":

    win = Tk()
    win.geometry("400x450+10+10")
    win.maxsize(400,450)
    win.minsize(400,450)
    win.config(bg="lightgray")
    win.title("Calculator")

    input_from_cal = Entry(win, bg="white", font=("AREAL", 20), width=30)
    input_from_cal.pack(padx=10,pady=20)
    input_from_cal.focus()

    _0 = setting.but_(win, text="    0     ", command=lambda: setting.fun_0(), place=[20,380])
    _1 = setting.but_(win, text="1", command=lambda: setting.fun_1(), place=[20,100])
    _2 = setting.but_(win, text="2", command=lambda: setting.fun_2(), place=[90,100])
    _3 = setting.but_(win, text="3", command=lambda: setting.fun_3(), place=[160,100])
    _4 = setting.but_(win, text="4", command=lambda: setting.fun_4(), place=[20,200])
    _5 = setting.but_(win, text="5", command=lambda: setting.fun_5(), place=[90,200])
    _6 = setting.but_(win, text="6", command=lambda: setting.fun_6(), place=[160,200])
    _7 = setting.but_(win, text="7", command=lambda: setting.fun_7(), place=[20,300])
    _8 = setting.but_(win, text="8", command=lambda: setting.fun_8(), place=[90,300])
    _9 = setting.but_(win, text="9", command=lambda: setting.fun_9(), place=[160,300])

    _add = setting.but_(win, text=" + ", command=lambda: setting.fun_add(), place=[230,100])
    _sub = setting.but_(win, text=" - ", command=lambda: setting.fun_sub(), place=[230,200])
    _div = setting.but_(win, text=" / ", command=lambda: setting.fun_div(), place=[320,100])
    _mul = setting.but_(win, text=" * ", command=lambda: setting.fun_mul(), place=[320,200])

    _clear = setting.but_(win, text="C", command=lambda: setting.fun_clear(), place=[230,300])
    _enter = setting.but_(win, text=" =", command=lambda: setting.fun_enter(), place=[320,300])

    _dot = setting.but_(win, text=" . ", command=lambda: setting.fun_dot(), place=[160,380])
    _back = setting.but_(win, text="     <-      ", command=lambda: setting.fun_back(), place=[230,380])




    mainloop()

