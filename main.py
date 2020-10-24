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
k = 1 
for i in range(5,130):

  draw_circle(-130+i,0,color[k])
  if k == 4:
    k = 0
  else:
    k+=1
    
