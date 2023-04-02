prizes = [5, 10, 50, 100, 1000]


def double(x):
    double_prize = []
    for item in x:
        double_prize.append(item * 2)
    print(double_prize)


double(prizes)

# comperhension method

dbl_prizes = [prize*2 for prize in prizes]

print(dbl_prizes)

# squering numbers

nums= [1,2,3,4,5,6,7,8,9,10]

dbl_nums = []

for num in nums:
    if (num ** 2) % 2 == 0:
        dbl_nums.append(num ** 2)
 
print(dbl_nums)

#Comperhansion method

square_even_nums = [num **2 for num in nums if (num **2) % 2 == 0]

print(square_even_nums)