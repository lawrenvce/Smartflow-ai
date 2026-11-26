
class Backtester:

    def __init__(self, starting_balance):

        if starting_balance <= 0:
            raise ValueError("Starting balance must be positive")

        self.balance = starting_balance
        self.starting_balance = starting_balance

        self.total_trades = 0
        self.wins = 0
        self.losses = 0

    def add_trade(self, result, amount):

        result = result.upper()

        if result not in ["WIN", "LOSS"]:
            raise ValueError("Result must be WIN or LOSS")

        if amount <= 0:
            raise ValueError("Amount must be positive")

        if result == "LOSS" and amount > self.balance:
            raise ValueError("Insufficient account balance")

        self.total_trades += 1

        if result == "WIN":
            self.wins += 1
            self.balance += amount
        else:
            self.losses += 1
            self.balance -= amount

    def show_results(self):

        if self.total_trades == 0:
            print("No trades recorded.")
            return

        win_rate = (self.wins / self.total_trades) * 100
        profit = self.balance - self.starting_balance

        print("\n===== SMARTFLOW REPORT =====")
        print(f"Starting Balance: ${self.starting_balance:.2f}")
        print(f"Ending Balance: ${self.balance:.2f}")
        print(f"Profit/Loss: ${profit:.2f}")
        print(f"Total Trades: {self.total_trades}")
        print(f"Wins: {self.wins}")
        print(f"Losses: {self.losses}")
        print(f"Win Rate: {win_rate:.2f}%")
