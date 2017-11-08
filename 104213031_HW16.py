# pd：pen down，放下筆
# pu：pen up，抬起筆
# fd：向前移動
# bk：向後移動
# lt：向左轉
# rt：向右轉
n = int(input("請問你要幾邊形?"))
import turtle
draw = turtle.Turtle()    #turtle.Turtle() 用來建立一個繪圖的工具

draw.pd()
for i in range(0,n) :
    draw.fd(900/n)
    draw.lt(360/n)
#draw.pu()    
turtle.mainloop()    #turtle.mainloop() 用來開始視窗並執行


