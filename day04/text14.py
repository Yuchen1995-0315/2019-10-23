"""
    列表 list
    通过切片访问元素会创建新列表
    通过切片修改列表不会创建新元素

"""
a = [1,"asd"]
z = list("shfdh")
print(a,z)
# 添加
a.append("锡纸上")
print(a)
a.insert(1,"插入")
print(a)
# 修改
a
a[:3] = ["1","十大","4","aaaa"]
print(a)
a[1:3] = ["2","3"]
print(a)


a[1:3] = [100]
print(a)

# 删除

del a[0]
print(a)

b = [1,2,3,4,5,6,7,8,9]
del b[2:8:2]
print(b)

b.remove(1)
print(b)
