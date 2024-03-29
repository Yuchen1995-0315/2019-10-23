# 重构:　不改变功能,修改内部代码.
# 修改命名
# 修改结构(你想传递的思想是什么?)

shang_pin_info = {
    101: {"name": "屠龙刀", "price": 10000},
    102: {"name": "倚天剑", "price": 10000},
    103: {"name": "九阴白骨爪", "price": 8000},
    104: {"name": "九阳神功", "price": 9000},
    105: {"name": "降龙十八掌", "price": 8000},
    106: {"name": "乾坤大挪移", "price": 10000}
}

ding_dan = []


def gou_wu():
    """
        购物
    :return:
    """
    while True:
        item = input("1键购买,2键结算。")
        if item == "1":
            bything()
            print("添加到购物车。")
        elif item == "2":
            settlement()


def settlement():
    total_prices = calculate_total_prices()
    while True:
        qian = float(input("总价%d元,请输入金额：" % total_prices))
        if qian >= total_prices:
            print("购买成功,找回：%d元。" % (qian - total_prices))
            ding_dan.clear()
            break
        else:
            print("金额不足.")


def calculate_total_prices():
    total_prices = 0
    for item in ding_dan:
        shang_pin = shang_pin_info[item["cid"]]
        print_dingdans()
        total_prices += shang_pin["price"] * item["count"]
    return total_prices


def bything():
    """

    :return:
    """
    print_dity()
    cid, count = add_car()
    ding_dan.append({"cid": cid, "count": count})


def add_car():
    while True:
        cid = int(input("请输入商品编号："))
        if cid in shang_pin_info:
            break
        else:
            print("该商品不存在")
    count = int(input("请输入购买数量："))
    order = {"cid": cid, "count": count}
    return cid, count


def print_dity():
    """
    打印商品信息
    :return:
    """
    for key, value in shang_pin_info.items():
        print("编号：%d，名称：%s，单价：%d。" % (key, value["name"], value["price"]))


def print_dingdans():
    """
    打印所有订单信息
    :return:
    """
    for item in ding_dan:
        shang_pin = shang_pin_info[item["cid"]]
        print("商品：%s,单价：%d,数量:%d." % (shang_pin["name"], shang_pin["price"], item["count"]))


gou_wu()