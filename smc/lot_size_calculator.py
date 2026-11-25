print("=== SMARTFLOW LOT SIZE CALCULATOR ===\n")

# Account settings
account_balance = 500
risk_percentage = 2

# Trade settings
direction = "BUY"

entry_price = 1.08500
stop_loss = 1.08300

# Forex settings
pip_value_per_lot = 10

# Calculate risk amount
risk_amount = account_balance * (risk_percentage / 100)

# Calculate stop loss distance
if direction == "BUY":
    stop_loss_pips = (entry_price - stop_loss) * 10000

elif direction == "SELL":
    stop_loss_pips = (stop_loss - entry_price) * 10000

else:
    raise ValueError("Invalid trade direction")

# Validate stop loss
if stop_loss_pips <= 0:
    raise ValueError("Invalid Stop Loss")

# Calculate lot size
lot_size = risk_amount / (stop_loss_pips * pip_value_per_lot)

# Calculate units
units = lot_size * 100000

print("Account Balance: $", account_balance)
print("Risk Percentage:", risk_percentage, "%")
print("Maximum Risk: $", risk_amount)

print("\nTrade Direction:", direction)
print("Entry Price:", entry_price)
print("Stop Loss:", stop_loss)
print("Stop Loss Distance:", stop_loss_pips, "pips")

print("\nRecommended Lot Size:", round(lot_size, 3))
print("Position Units:", round(units))

print("\n=== CALCULATION COMPLETE ===")
