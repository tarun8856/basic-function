def compute_lcm(x, y):

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm


if __name__ == '__main__':

    num1 = int(input(""))
    num2 = int(input(""))
    
    ans = compute_lcm(num1,num2)
    print (ans)