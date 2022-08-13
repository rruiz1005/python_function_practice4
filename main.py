#1
def max_num(a, b, c):
    return max([a,b,c])

print(max_num(5,6,9))

#2
def mult_list(x, y, z):
    return x*y*z

print(mult_list(2, 2, 5))

#3
def rev_string(name):
    return name[::-1]

print(rev_string("Ryan"))
print(rev_string("racecar"))

#4
def num_within(n, a, b):
    return n in range(a, b+1)

print(num_within(6, 1, 10))
print(num_within(4, 6, 10))

#5
triangle = [[1], [1, 1]]
def pascal(n):
    if n < 1:
        print("invalid number of rows")
    elif n == 1:
        print(triangle[0])
    else:
        row_number = 2

        while len(triangle) < n:
            row = []
            row_prev = triangle[row_number - 1]

            length = len(row_prev)+1
            for i in range(length):

                if i == 0:
                    row.append(1)

                elif i > 0 and i < length-1:
                    row.append(triangle[row_number - 1][i-1]+triangle[row_number - 1][i])

                else:
                    row.append(1)
            triangle.append(row)
            row_number += 1

        for row in triangle:
            print(row)

pascal(2)
pascal(5)

