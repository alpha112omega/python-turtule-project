import turtle as t
t.tracer(50)
t.setup(1537,865)
t.bgcolor('black')
color=('red','black')
t.width(2)
for i in range(1800):
    t.pencolor(color[i%2])
    t.bk(i)
    t.lt(30)
    t.fd(i)
    t.rt(120)
    t.fd(i)
    t.rt(240)
    t.fd(i)
    t.lt(30)
t.done()

