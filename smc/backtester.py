class Backtester:

    def __init__(self):
        self.total_trades = 0
        self.wins = 0
        self.losses = 0

    def add_trade(self, result):

        self.total_trades += 1

        if result.upper() == "WIN":
            self.wins += 1
        else:
            self.losses += 1

    def show_results(self):

        if self.total_trades == 0:
            print("No trades recorded.")
            return

        win_rate = (self.wins / self.total_trades) * 100

        print("\n=== SMARTFLOW BACKTEST RESULTS ===")
        print(f"Total Trades: {self.total_trades}")
        print(f"Wins: {self.wins}")
        print(f"Losses: {self.losses}")
        print(f"Win Rate: {win_rate:.2f}%")



backtester = Backtester()

backtester.add_trade("WIN")
backtester.add_trade("LOSS")
backtester.add_trade("WIN")
backtester.add_trade("WIN")
backtester.add_trade("LOSS")

backtester.show_results()
