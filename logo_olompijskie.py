import turtle as t
x = [-130,0,130,-60,70]
y = [0,0,0,-60,-60]
color = ['blue', 'black', 'red','yellow','green']

def draw_circle(x, y, color):
  t.penup()
  t.pensize(10)
  t.setposition(x,y)
  t.pendown()
  t.color(color)
  t.circle(60)
  
for i in range(0,5):
  draw_circle(x[i],y[i],color[i])