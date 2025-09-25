def storage_contract(injection_dates, withdrawal_dates, prices,

                     injection_rate, withdrawal_rate,
                     max_storage, storage_cost):
    # start with no gas and no money
    storage = 0
    value = 0

    # buy gas on injection dates
    for d in injection_dates:
        if storage + injection_rate <= max_storage:
            storage += injection_rate
            value -= prices[d] * injection_rate   # spend money to buy

    # sell gas on withdrawal dates
    for d in withdrawal_dates:
        if storage >= withdrawal_rate:
            storage -= withdrawal_rate
            value += prices[d] * withdrawal_rate  # earn money from selling

    # pay storage cost for each period (just count total days)
    total_days = max(injection_dates + withdrawal_dates) - min(injection_dates + withdrawal_dates) + 1
    value -= total_days * storage_cost

    return value


# ----- test example -----
prices = {0: 2.0, 1: 2.2, 2: 3.0, 3: 3.2}
inj = [0, 1]       # inject on day 0 and 1
withd = [2, 3]     # withdraw on day 2 and 3

ans = storage_contract(inj, withd, prices,
                       injection_rate=1000000,
                       withdrawal_rate=1000000,
                       max_storage=2000000,
                       storage_cost=100000)

print("Contract Value =", ans)
