
def accept_roll():
    roll_no=[]
    n=int(input("\nEnter the total no. of students"))
    for i in range(n):
        roll=int(input(f"\nEnter the roll no. of student {i+1}"))
        roll_no.append(roll)
    return roll_no

def print_roll(roll_no):
    for i in range(len(roll_no)):
        print(roll_no[i], sep="\n")

def insertion_sort(roll_no):
    for i in range(1,len(roll_no)):
        key = roll_no[i]
        j = i-1
        while j >= 0 and key < roll_no[j]:
            roll_no[j+1] = roll_no[j]
            j -= 1
            roll_no[j+1] = key
    return roll_no

def ternary_search(roll, left, right, roll_find):
    if (right >= left):
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        if (roll[mid1]==roll_find):
            return mid1
        if (roll[mid2]==roll_find):
            return mid2

        if (roll_find < mid1):
            return ternary_search(roll, left, mid1-1, roll_find)
        elif (roll_find > mid2):
            return ternary_search(roll, mid2+1, right, roll_find)
        else:
            return ternary_search(roll, mid1+1, mid2-1, roll_find)
    return -1

unsort_roll=[]
sort_roll=[]
flag=1
while flag==1:
    print("\n**********MENU**********")
    print("1. Accept Student Roll Numbers")
    print("2. Display Student Roll Numbers")
    print("3. Sort Roll Numbers from the list")
    print("4. Perform Ternary Search")
    print("5. Exit")

    ch = int(input("\nEnter your choice"))

    if(ch == 1):
        unsort_roll=accept_roll()

    elif(ch == 2):
        print_roll(unsort_roll)

    elif(ch == 3):
        print("Elements after performing Insertion sort: ")
        sort_roll=insertion_sort(unsort_roll)
        print_roll(sort_roll)

    elif(ch == 4):
        find_roll = int(input("\nEnter the Roll Number to be searched"))
        left = 0
        right = len(sort_roll)-1
        index = ternary_search(sort_roll, left, right, find_roll)
        if(index!=-1):
            print("The Roll Number is found at position", index+1)
        else:
            print("Roll Number not found")

    else:
        print("Thanks for using this program")
        flag=0