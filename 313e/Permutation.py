def permute(a, idx):
    hi = len(a)
    if (idx == hi):
        return a
    else: 
        for i in range (idx, hi):
            # swap and recurse
            a[idx], a[i] = a[i], a[idx]
            permute(a, idx+1)
            a[idx], a[i] = a[i], a[idx]

def permute1(a, idx, lst):
    hi = len(a)
    if (idx == hi):
        lst.append(0)
        lst[-1] = a
    else: 
        for i in range (idx, hi):
            # swap and recurse
            a[idx], a[i] = a[i], a[idx]
            permute1(a, idx+1, lst)
            a[idx], a[i] = a[i], a[idx]


def main():
    a = ['A', 'B', 'C']
    lst = []
    lst.append(permute (a, 0))
    permute1(a, 0, lst)
    print(lst)


# source is the first, spare is the second, and dest is the last
# n is the number of disks
# def towers(n, source, spare, dest):
#     if n == 1:
#         print('Move disk from', source, 'to', dest)
#     else:
#         towers(n-1, source, dest, spare)
#         print('Move disk from {} to {}'.format(source, dest))
#         towers(n-1, spare, source, dest)

# def main():
#     towers(4, 'A', 'B', 'C')


# use memory to gain speed
# def fib_memo(n, memo):
#     if n == 0 or n == 1:
#         return memo[n]
#     else:
#         if (n >= len(memo)):
#             f = fib_memo(n-1, memo) + fib_memo(n-2, memo)
#             memo.append(f)
#             return f
#         else:
#             return memo[n]

# def fib_rec(n):
#     if (n == 0) or (n == 1):
#         return n
#     else:
#         return fib_rec(n-1) + fib_rec(n-2)

# def main():
#     memo = [0, 1]
#     for i in range(50):
#         print(i, ' ', fib_memo(i, memo))


# print(fib_memo(100,[0,1]))
# print(fib_rec(100))



main()