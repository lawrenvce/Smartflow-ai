
print("=== SMARTFLOW TRADE CALCULATOR ===\n")

# Simulated account
account_balance = 500
risk_percentage = 2

# Trade setup
direction = "BUY"

entry_price = 1.08500
stop_loss = 1.08300
take_profit = 1.08900

# Calculate risk amount
risk_amount = account_balance * (risk_percentage / 100)

# Calculate pip distances
if direction == "BUY":
    risk_pips = (entry_price - stop_loss) * 10000
    reward_pips = (take_profit - entry_price) * 10000

elif direction == "SELL":
    risk_pips = (stop_loss - entry_price) * 10000
    reward_pips = (entry_price - take_profit) * 10000

else:
    raise ValueError("Invalid trade direction")

# Validate trade
if risk_pips <= 0 or reward_pips <= 0:
    raise ValueError("Invalid SL or TP placement")

# Risk-to-reward
rr_ratio = reward_pips / risk_pips

print("Account Balance: $", account_balance)
print("Risk Amount: $", risk_amount)
print("Direction:", direction)

print("\nEntry:", entry_price)
print("Stop Loss:", stop_loss)
print("Take Profit:", take_profit)

print("\nRisk:", risk_pips, "pips")
print("Reward:", reward_pips, "pips")

print("Risk-to-Reward: 1:", round(rr_ratio, 2))
