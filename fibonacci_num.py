num = int(input())
def fibonancci(n):
    def get_fib(i):
        if i <= 1:
            return i
        return get_fib(i-1) + get_fib(i-2)
    #Formula: Fn = F{n-1} + F{n-2}
    for i in range(n):
        print(get_fib(i))
fibonancci(num)