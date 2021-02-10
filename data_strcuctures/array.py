stoke_price = [298, 305, 320, 301, 292]

# on what day price was 301?

for i in range(len(stoke_price)):
    if stoke_price[i] == 301:
        print(f'day was: {i+1}')

stoke_price.insert(1,400)

for i in range(len(stoke_price)):
    print(stoke_price[i], end=' ')

#stoke_price.remove(0)

for i in range(len(stoke_price)):
    print(stoke_price[i], end=' ')