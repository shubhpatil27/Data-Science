def price_storage_contract(
    injection_dates,
    withdrawal_dates,
    prices,
    injection_rate,
    withdrawal_rate,
    max_storage,
    storage_cost
):
    cashflows = 0
    storage = 0   # current stored gas

    # Handle injections
    for date in injection_dates:
        qty = min(injection_rate, max_storage - storage)
        storage += qty
        cashflows -= qty * prices[date]   # pay for gas

    # Handle withdrawals
    for date in withdrawal_dates:
        qty = min(withdrawal_rate, storage)
        storage -= qty
        cashflows += qty * prices[date]   # earn from selling

    # Deduct storage cost
    total_periods = max(withdrawal_dates + injection_dates) - min(withdrawal_dates + injection_dates) + 1
    cashflows -= total_periods * storage_cost

    return cashflows


# ----- test example -----
prices = {0: 2.0, 1: 2.2, 2: 3.0, 3: 3.2}
inj = [0, 1]       # inject on day 0 and 1
withd = [2, 3]     # withdraw on day 2 and 3

result = price_storage_contract(
    injection_dates=inj,
    withdrawal_dates=withd,
    prices=prices,
    injection_rate=1000000,
    withdrawal_rate=1000000,
    max_storage=2000000,
    storage_cost=100000
)

print("Contract Value =", result)
