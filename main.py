import turtle

jerry_turtle = turtle.Turtle()
jerry_turtle.speed(12)

def square():
  jerry_turtle.forward(100)
  jerry_turtle.right(90)
  jerry_turtle.forward(100)
  jerry_turtle.right(90)
  jerry_turtle.forward(100)
  jerry_turtle.right(90)
  jerry_turtle.forward(100)
  

# square()
# jerry_turtle.forward(200)
# square()

elephant_weight = 3000
ant_weight = 0.1

# if elephant_weight < ant_weight:
  # square()
#  else:
#   jerry_turtle.forward(100)

# jerry = 'happy'
# while jerry == 'sad':
  # jerry_turtle.forward(10)

for count in range(4):
  square()