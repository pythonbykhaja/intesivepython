### Daily stock price in $

price = [
    [ 9.9, 9.8, 9.7, 9.5, 9.4 ],
    [ 9.5, 9.6, 9.4, 9.4, 9.2 ],
    [ 8.4, 7.9, 7.9, 8.2, 8.1 ],
    [ 7.1, 5.9, 4.1, 4.8, 5.2 ]
]

sample = [ line[::2] for line in price ]
print(sample)