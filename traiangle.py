import math
def compute_triangle(a,b,c): 

    s = (a + b + c) / 2
    ans = math.sqrt(s * (s-a) * (s-b) * (s-c) )
    return ans

if __name__ == '__main__':

    num1 = int(input(""))
    num2 = int(input(""))
    num3 = int(input(""))

    age = compute_triangle(num1,num2,num3)
    print(age)