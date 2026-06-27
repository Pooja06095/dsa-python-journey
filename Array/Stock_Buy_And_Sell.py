class Stock_Sale:
    def stock_and_sale(self):
        min_price = arr[0]
        max_profit = 0

        for price in arr:
            profit = price - min_price

            max_profit = max(max_profit, profit)

            min_price = min(min_price, price)

        return max_profit
arr = arr = [7, 1, 5, 3, 6, 4]
obj = Stock_Sale()
res = obj.stock_and_sale()
print(res)
