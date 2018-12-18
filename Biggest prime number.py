# Python program to check if the input number is prime or not

loop = True
n = 0
while loop == True:
    
    num1 = 2 ** n
    num = num1 - 1
    

    # take input from the user
    # num = int(input("Enter a number: "))

    # prime numbers are greater than 1
        
    if num > 1:
        # check for factors
        for i in range(2,num):
            
            if (num % i) == 0:

                print('')
                
                print(num,'is not a prime number')
                #print(i,"times",num//i,"is",num)
                n = n + 1
                break
                
        else:
            print('')
            print('prime number is %.7e'%num , ', n is ', n ,'<<<-----------------------------------------')
            n = n + 1
            
           
           
    # if input number is less than
    # or equal to 1, it is not prime
    else:
       print(num,'is not a prime number')
       n = n + 1
       
