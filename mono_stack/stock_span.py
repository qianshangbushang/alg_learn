

class StockSpan:
    def __init__(self) -> None:
        self.stock_list = []
        self.span_list = []
        return

    def next(self, price: int) -> int:
        """
        当天大于等于之前的次数
        """

        # 如果上一天不存在，或者当天小于上一天，那么span=1
        # 当前大于之前上一天
        i = len(self.stock_list) - 1
        while i >= 0 and self.stock_list[i] < price:
            i -= self.span_list[i]
        self.span_list.append(len(self.stock_list) - i)
        self.stock_list.append(price)
        return self.span_list[-1]


if __name__ == "__main__":
    s = StockSpan()
    for p in [100, 80, 60, 70, 60, 75, 85]:
        print(s.next(p))
