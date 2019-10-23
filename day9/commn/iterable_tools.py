class IterableHelper:
    """
        可迭代对象助手
    """

    # 静态方法：函数(不需要操作实例/类数据) --> 方法
    @staticmethod  # 为了不隐式(自动)传参(self/cls)
    def find_all(iterable_target, func_condition):
        """
            在可迭代对象中，根据指定条件搜索元素.
        :param iterable_target:需要搜索的可迭代对象
        :param func_condition:需要判断的条件
        :return:生成器对象,存储满足条件的结果.
        """
        for item in iterable_target:
            if func_condition(item):
                yield item

    @staticmethod
    def find_single(iterable_target, func_condition):
        for item in iterable_target:
            if func_condition(item):
                return item

    @staticmethod
    def get_count(iterable_target, func_condition):
        count = 0
        for item in iterable_target:
            if func_condition(item):
                count += 1
        return count

    @staticmethod
    def sum(iterable_target, func_handle):
        """
            在可迭代对象中,累加其中的元素
        :param iterable_target:需要累加的数量
        :param func_handle: 需要累加的逻辑
        :return: 累加的结果
        """
        sum_value = 0
        for item in iterable_target:
            sum_value += func_handle(item)
        return sum_value

    @staticmethod
    def is_exists(iterable_target, func_condition):
        """
            在可迭代对象中,根据逻辑判断
        :param iterable_target: 需要搜索的可迭代对象
        :param func_handle:  需要判断的逻辑
        :return: 判断的bool类型
        """
        for item in iterable_target:
            if func_condition(item):
                return True
        return False

    @staticmethod
    def get_max(iterable_target, func_handle):
        """

        :param iterable_target:
        :param func_handle:
        :return:
        """
        max = iterable_target[0]
        for i in range(1, len(iterable_target)):
            # if max.attck < iterable_target[i]:
            if func_handle(max) < func_handle(iterable_target[i]):
                max = iterable_target[i]
        return max

    @staticmethod
    def select(iterable_target, func_condition):
        """
            在可迭代对象中,查找某些元素
        :param iterable_target: 需要搜索的数据
        :param func_condition: 需要处理的逻辑
        :return:
        """
        result = []
        for item in iterable_target:
            result.append((func_condition(item)))
        return result

    @staticmethod
    def order_by(iterable_target, func_condition):
        for i in range(len(iterable_target) - 1):
            for c in range(i + 1, len(iterable_target)):
                if func_condition(iterable_target[i]) > func_condition(iterable_target[c]):
                    iterable_target[i], iterable_target[c] = iterable_target[c], iterable_target[i]

    @staticmethod
    def get_min(iterable_target, func_condition):
        min = iterable_target[0]
        for i in range(1, len(iterable_target)):
            # if max.attck < iterable_target[i]:
            if func_condition(min) > func_condition(iterable_target[i]):
                min = iterable_target[i]
        return min

    @staticmethod
    def delete_all(iterable_target, func_condition):
        for i in range(len(iterable_target) - 1, -1, -1):
            if func_condition(iterable_target[i]):
                del iterable_target[i]
