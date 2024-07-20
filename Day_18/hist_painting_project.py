# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('img.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
import random
import turtle as turtle_module

tim = turtle_module.Turtle()
turtle_module.colormode(255)
tim.penup()
tim.hideturtle()
tim.speed('fastest')
color_list = [(202, 166, 109), (240, 246, 241), (152, 73, 47), (236, 238, 244), (170, 153, 41), (222, 202, 138),
              (53, 93, 124),
              (135, 32, 22), (132, 163, 184), (48, 118, 88), (198, 91, 71), (16, 97, 75), (100, 73, 75), (67, 47, 41),
              (147, 178, 147), (163, 142, 156), (234, 177, 165), (55, 46, 50), (130, 28, 31), (184, 205, 174),
              (41, 60, 72),
              (83, 147, 126), (181, 87, 90), (31, 77, 84), (47, 65, 83), (215, 177, 182), (19, 71, 63), (175, 192, 212)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_counts in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_counts % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
