"""
    路程 = 加速度×时间的平方×0.5 + 初速度×时间
    输入距离，时间，初速度
    求：加速度
"""
s = float(input("请输入距离："))
t = float(input("请输入时间："))
v0 = float(input("请输入初速度："))

a = str(((s - v0*t)/(t**2))*2)
print("加速度为"+a+"米每秒方")
