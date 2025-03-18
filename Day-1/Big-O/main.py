# Big O: (O n)
# this is O(n) since it needs to iterate for every item in the array and print it on the console.
# worst case, we have a huge dataset
def bigo_lin(n):
    for i in range(n):
        print(i)


# DO NOT CHANGE THIS LINE:
# bigo_lin(10)

print('\n')

# Big O: (O n ^ 2)
# Since this is a nested loop it takes twice the time because the inner loop is O(n) and outer loop is also O(n)
# therefore O(n) * O(n) => (O n ^ 2)


def bigo_sqr(n):
    for i in range(n):
        for j in range(n):
            print(i, j)


# DO NOT CHANGE THIS LINE:
# bigo_sqr(10)
