#1

n = int(input("Enter a four-digit number: "))
a = n//1000
b = n//100%10
c = n//10%10
d = n%10
print(a, b, c, d, sep='\n')



#2
#Знайшов це рішення в інтернеті і підправив під задачу, але так і не зрозумів як воно працює)))
n = int(input("Enter a four-digit number: "))
a1, n = divmod(n, 1000)
a2, n = divmod(n, 100)
a3, n = divmod(n, 10)
print(a1, a2, a3, n, sep='\n')


#Draft
value = input("Enter a four-digit number: ")
print('\n'.join(value))
#Draft2
value = input("Enter a four-digit number: ")
value2 = list(value)
for i in value2:
    print(i)









