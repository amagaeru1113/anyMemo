import turtle

# 資格
# turtle.color("red", "yellow")
# turtle.begin_fill()
# for i in range(4):
#     turtle.forward(100)
#     turtle.right(90)
# turtle.end_fill()

# turtle.done()

# ほし
# turtle.color("red", "yellow")

# turtle.begin_fill()
# for i in range(5 * 3):
#     turtle.forward(100 + i * 10)
#     turtle.right(360 / 5 * 2)
# turtle.end_fill()

# turtle.done()

# 三角形
# turtle.pencolor("green")
# for i in range(60):
#     turtle.forward(50)
#     turtle.right(360 / 3 + 10)

# turtle.pencolor("red")
# for i in range(60):
#     turtle.forward(200)
#     turtle.right(360 / 3 + 10)
# turtle.done()


for i in range(200):
    turtle.forward(i)
    turtle.right(360 / 4 + 10)
turtle.done()
