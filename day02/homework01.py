"""
    温度转换器：
    摄氏度 = （华氏度 - 32） 除以 1.8
    开氏度 = 摄氏度 + 273.15
    (1)在终端中录入华氏度，计算摄氏度
    (2)在终端中录入摄氏度，计算开氏度
"""
# 输入华氏温度
print("华氏温度——》摄氏温度")
fahrenheit = float(input("请输入华氏温度："))

centigrade_result = (fahrenheit - 32)/1.8
print("摄氏温度为"+str(centigrade_result))

# 输入摄氏温度
print("摄氏温度——》开氏温度")
centigrade = float(input("请输入摄氏温度："))
kelvin_result = centigrade + 273.15

print("开氏温度为"+str(kelvin_result))


