#a='''hello word
#this is a test'''
#print(a)
#tuple =('i love you','i love your eyes')
#print(tuple) 

import turtle
  

pen = turtle.Turtle()
  

def curve():
    for i in range(200):
  
        
        pen.right(1)
        pen.forward(1)
  

def heart():
  
    
    pen.fillcolor('pink')
  
    
    pen.begin_fill()
  
    
    pen.left(140)
    pen.forward(113)
  
   
    curve()
    pen.left(120)
  
    
    curve()
  
    
    pen.forward(112)
  
    
    pen.end_fill()
    pen("i love you")
  

def txt():
  
    
    pen.up()
  
    
    pen.setpos(-68, 95)
  
   
    pen.down()
  
    pen.color('red')
  
    
    pen.write("yolo", font=(
      "Verdana", 12, "bold"))
  
  

heart()
  

txt()
  

pen.ht()