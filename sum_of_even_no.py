n=int(input("Enter a number : "))
i=1
total=0
count=0
while i<=n:
    if i%2==0:
        total+=i
        count+=1
    i+=1
print(f"Sum of even numbers : {total}")
print(f"Number of even numbers : {count}")

    
