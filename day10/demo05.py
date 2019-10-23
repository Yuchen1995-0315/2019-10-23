"""
    装饰器
"""
def verif_permission(func):#外部函数接受旧功能
    def wrapper(*args, **kwargs):
        print("验证权限")#新功能
        return func(*args, **kwargs)#旧功能　内部函数的返回值就是旧功能的返回值
    return wrapper

@verif_permission
def enter_background(id, name):
    print("进入后台",id,name )

@verif_permission
def dele_order():
    print("删除订单")

enter_background("01","yuchen")
dele_order()