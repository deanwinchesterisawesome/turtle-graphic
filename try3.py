from turtle import *
speed(0) 
pencolor('blue') 
bgcolor('yellow') 

x = 0
y = 0
z = 0
up() 

rt(70) 
fd(90) 
rt(150) 

down() 
while x < 60: 
    fd(200)     
    rt(88)
    fd(200)
    rt(88)
    fd(200)
    rt(88)
    fd(200)
    rt(88)
    fd(200)
    rt(88)
    fd(200)
    rt(88)

    rt(11.1111) 
    x = x+1 
setpos(0,0)
pencolor('red')
while y < 60: 
    fd(200)     
    rt(88)
    fd(200)
    rt(88)
    fd(200)
    rt(88)
    fd(200)
    rt(88)
    fd(200)
    rt(88)
    fd(200)
    rt(88)

    rt(11.1111) 
    y = y+1 
setpos(0,0)
pencolor('green')
while z < 60:
    fd(200)     
    lt(88)
    fd(200)
    lt(88)
    fd(200)
    lt(88)
    fd(200)
    lt(88)
    fd(200)
    lt(88)
    fd(200)
    lt(88)

    rt(11.1111) 
    z = z+1             
        
exitonclick() 
