import turtle

wn = turtle.Screen()


def tree(t, branchLen):
    if branchLen > 0:
        t.forward(branchLen)
        t.right(20)
        tree(t, branchLen - 10)
        t.left(40)
        tree(t, branchLen - 10)
        t.right(20)
        t.backward(branchLen)


def main():
    t = turtle.Pen()
    t.speed(0)
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    tree(t, 75)


main()