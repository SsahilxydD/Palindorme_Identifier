list1 = []
prefferedRange = int(input("How Long Is the Word you wanna Check for : "))
for i in range(prefferedRange):
    list1.append(int(input("Enter the Number : ")))
list2 = list1.copy()
list2.reverse()

if list1 == list2:
    print("Palindrome")
else:
    print("Not a palindrome")
