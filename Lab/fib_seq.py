def rec_fibo_seq(n):
    if n  == 0:
        return 0
    if n == 1:
        return 1
    return rec_fibo_seq(n - 1) + rec_fibo_seq(n - 2)

def iter_fibo_seq(n):
    count = 1
    a, b = 0 , 1
    while count < n:
        tmp = a
        a = b
        b = tmp + b
        count += 1
    return b
print(iter_fibo_seq(5))
print (rec_fibo_seq(5))
    