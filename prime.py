num = int(input("Enter a number from 1 to: "))
for i in range(2,num):
    if((i==1 or i%2 == 0 or i%3 == 0 or i%5==0 or i%7==0) and (i!=2 and i!=3 and i!=5 and i!=7)):
        continue
    else:
        print(i)