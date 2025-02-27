# User function Template for python3
def lower(N):
    for i in range(N, 0, -1):
        for j in range(i):
            if j + 1 < i:
                print("*", end=" ")
            else:
                print("*")


def upper(N):
    for i in range(1, N + 1):
        for j in range(i):
            if j + 1 < i:
                print("*", end=" ")
            else:
                print("*")

def print_triangle(n):
    upper(n)
    lower(n - 1)


n = int(input("input number of * your want to print: "))
print_triangle(n)
