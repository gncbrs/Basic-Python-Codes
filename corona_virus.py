#corona virus with turtle library.
from turtle import *

speed(15)
color("yellow")
bgcolor("black")
b = 200

while b > 0:
    left(b)
    forward(b * 3)
    b = b - 1
