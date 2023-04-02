def cough_dec(func):

    def func_wrapper():
        #code before function
        print('*cough*')
        func()
        print('*cough*')
        #code after function 

    return func_wrapper

@cough_dec
def question():
    print('Can you give me a discount on that')

@cough_dec
def answer():
    print('Its only 50 p u cheepskate')
question()

answer()