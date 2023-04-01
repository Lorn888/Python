# for n in range(5):
#     print(n)


# for n in range(5,10):
#     print(n)

# for n in range(5,10,2):
#     print(n)


burgers = ['beef', 'chicken', 'veg', 'supreme',
           'double', 'quarter', 'bigmac', 'beyond meet']

# for n in range(len(burgers)):
#     print(n, burgers[n])
45
# for n in range(len(burgers) -1, -1, -1):
#     print(n+1, burgers[n])

for n in range(burgers.index('supreme'), len(burgers)):
    print(n, burgers[n])