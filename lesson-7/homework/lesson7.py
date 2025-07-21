#1


def is_prime(n):
    if n > 0 and n % 2 ==1:
        return True
    else:
        return False

is_prime(1)

#2


def digit_sum(k):
    digit = [int(i) for i in str(k)]
    print(sum(digit))

digit_sum(int(502))

#3


def power_2_not_exceed (n):
    nb = 1
    while n > 2**nb:
        print(2**nb)
        nb +=1

power_2_not_exceed(int(10))
