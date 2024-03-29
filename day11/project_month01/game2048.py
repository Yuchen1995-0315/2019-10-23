# """
#     2048 游戏核心算法
# """
list_merge = [2, 0, 2, 0]
#
#
# # 1. 定义函数　zero_to_end()
# # [2,0,2,0]  -->  [2,2,0,0]
# # [2,0,0,2]  -->  [2,2,0,0]
# # [2,4,0,2]  -->  [2,4,2,0]
def zero_to_end():
    """
        零元素向后移动
        思想：从后向前判断，如果是0则删除,在末尾追加.
    """
    for i in range(len(list_merge) - 1, -1, -1):
        if list_merge[i] == 0:
            del list_merge[i]
            list_merge.append(0)
#

# zero_to_end()
# print(list_merge)
#
#
# # 2. 定义函数　merge()
# # [2,0,2,0]  -->[2,2,0,0]  -->  [4,0,0,0]
# # [2,0,0,2]  -->[2,2,0,0]  -->  [4,0,0,0]
# # [4,4,4,4]  -->  [8,8,0,0]
# # [2,0,4,2]  -->  [2,4,2,0]
# def merge():
#     """
#         合并
#           核心思想：零元素后移，判断是否相邻相同。如果是则合并.
#     """
#     zero_to_end()
#     for i in range(len(list_merge) - 1):
#         if list_merge[i] == list_merge[i + 1]:
#             list_merge[i] += list_merge[i + 1]
#             del list_merge[i + 1]
#             list_merge.append(0)
#
#
# # merge()
# # print(list_merge)
#
# # 3. 向左移动
# # map = [
# #     [2, 0, 0, 2],
# #     [4, 2, 0, 2],
# #     [2, 4, 2, 4],
# #     [0, 4, 0, 4],
# # ]
#
#
def move_left():
    """
        向左移动map
        思想：获取每行，交给list_merge，在通知merge()进行合并
    :return:
    """
    global list_merge
    for line in map:
        list_merge = line
        merge()
#

move_left()
print(map)
#
# # 4. 向右移动 move_right
def move_right():
    """
        向左移动map
        思想：获取每行，交给list_merge，在通知merge()进行合并
    :return:
    """
    global list_merge
    for line in map:
        # 从右向左获取数据形成新列表
        list_merge = line[::-1]
        # 处理数据
        merge()
        # 将处理后的数据再从右向左还给map
        line[::-1] = list_merge
#
#
move_right()
print(map)

# 5. 向上移动 move_up   转置  move_left　转置
# def square_matrix_transposition(list_matrix):
#     """
#         方阵转置（列转换为行）
#     :param list_matrix: 需要转置的方阵
#     :return:
#     """
#     for c in range(1, len(list_matrix)):  # 1 2 3
#         for r in range(c, len(list_matrix)):
#             list_matrix[r][c - 1], list_matrix[c - 1][r] = list_matrix[c - 1][r], list_matrix[r][c - 1]


def move_up():
    """
        向上移动
        思想：  转置  move_left　转置　
    """
    square_matrix_transposition(map)
    move_left()
    square_matrix_transposition(map)

#
# 6. 向下移动
def move_down():
    """
        向下移动
        思想: 转置  move_right　转置
    :return:
    """
    square_matrix_transposition(map)
    move_right()
    square_matrix_transposition(map)


# move_up()
move_down()
print(map)
