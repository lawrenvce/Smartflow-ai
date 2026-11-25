print("=== SMARTFLOW RISK MANAGEMENT ===\n")

# Account settings
account_balance = 500
risk_percentage = 2

# Risk limits
max_daily_loss_percentage = 4
max_trades_per_day = 3
minimum_rr = 2

# Today's trading activity
daily_loss = 5
trades_taken = 1

# Proposed trade
planned_risk = 10
risk_reward = 2.5

# Calculate limits
max_risk = account_balance * (risk_percentage / 100)

max_daily_loss = account_balance * (
    max_daily_loss_percentage / 100
)

print("Account Balance: $", account_balance)
print("Maximum Risk Per Trade: $", max_risk)
print("Maximum Daily Loss: $", max_daily_loss)

print("\n=== TRADE VALIDATION ===")

# Check daily loss
if daily_loss >= max_daily_loss:
    print("TRADE REJECTED: Daily loss limit reached.")

# Check number of trades
elif trades_taken >= max_trades_per_day:
    print("TRADE REJECTED: Maximum daily trades reached.")

# Check risk amount
elif planned_risk > max_risk:
    print("TRADE REJECTED: Risk exceeds allowed limit.")

# Check risk-to-reward
elif risk_reward < minimum_rr:
    print("TRADE REJECTED: Risk-to-reward is too low.")

else:
    print("TRADE APPROVED!")
    print("Risk Amount: $", planned_risk)
    print("Risk-to-Reward: 1:", risk_reward)

print("\n=== RISK CHECK COMPLETE ===")
