import random

def problem2_4():
    """ Make a list of 10 random reals between 30 and 35 """
    random.seed(70)
    num_lis = []
    for i in range(10):
        n = (random.random()*5 +30)
        num_lis.append(n)
    print(num_lis)