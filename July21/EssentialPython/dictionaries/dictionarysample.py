portfolio = dict()
portfolio['Microsoft'] = 286.54
portfolio['IBM'] = 142.75
portfolio['Amazon'] = 3626.39
portfolio['Apple'] = 146.77
portfolio['Google'] = 2638

for name, price in portfolio.items():
    print(f"{name} ==> {price}")

for name in portfolio.keys():
    print(f"{name} --> {portfolio[name]}")