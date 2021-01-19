c = input("Enter a string: ")
ch = c.split()
ch = ch[::-1]
ch = " ".join(ch)
print(ch[::-1])