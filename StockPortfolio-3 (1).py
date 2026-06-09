# StockPortfolio.py

class StockPortfolio:
    def __init__(self):
        self.portfolio = {}

    def buy_stock(self, symbol, quantity, price):
        if symbol in self.portfolio:
            self.portfolio[symbol]["quantity"] += quantity
        else:
            self.portfolio[symbol] = {"quantity": quantity, "price": price}
        print(f"Bought {quantity} shares of {symbol} at ₹{price} each.")

    def sell_stock(self, symbol, quantity):
        if symbol not in self.portfolio:
            print("Stock not found in portfolio.")
            return

        if quantity > self.portfolio[symbol]["quantity"]:
            print("Not enough shares to sell.")
            return

        self.portfolio[symbol]["quantity"] -= quantity

        if self.portfolio[symbol]["quantity"] == 0:
            del self.portfolio[symbol]

        print(f"Sold {quantity} shares of {symbol}.")

    def display_portfolio(self):
        if not self.portfolio:
            print("Portfolio is empty.")
            return

        print("\\nCurrent Portfolio")
        print("-" * 30)
        total_value = 0

        for symbol, data in self.portfolio.items():
            value = data["quantity"] * data["price"]
            total_value += value
            print(
                f"{symbol}: {data['quantity']} shares @ ₹{data['price']} "
                f"= ₹{value}"
            )

        print("-" * 30)
        print(f"Total Portfolio Value: ₹{total_value}")


# Example Usage
portfolio = StockPortfolio()

portfolio.buy_stock("TCS", 10, 3500)
portfolio.buy_stock("INFY", 5, 1500)

portfolio.display_portfolio()

portfolio.sell_stock("INFY", 2)

portfolio.display_portfolio()
