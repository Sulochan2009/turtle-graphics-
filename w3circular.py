import turtle 
window = turtle.Screen()
window.bgcolor("Red")
situ = turtle.Turtle()
situ.shape("turtle")
situ.color("blue")
situ.speed(10)

aayu = turtle.Turtle()
aayu.shape("arrow")
aayu.color("black")

def draw_circle():
    aayu.circle(100)
    aayu.speed(10)
    #aayu.position(20,20)

def draw_square(a):
    for i in range(1,5):
      a.fd(100)
      a.right(90)

def pattern():
    for i in range(1,40):
        draw_square(situ)
        situ.right(10)
#i=0
 #   x=2

   # while(i<4):
  #  for j in range(1,50):
   #     situ.right(89+x)
    #    situ.forward(100)
      #  x=x+1
     #   for i in range(1,4):
       #     situ.right(90)
        #    situ.forward(100)
        
    
#draw_circle()
#
#draw_square()
pattern()
window.exitonclick()
