def Selection_Sort(marks):
    for i in range(len(marks)):
       min_idx = i
       for j in range(i+1,len(marks)):
          if marks[min_idx] > marks[j]:
            min_idx = j
          
       marks[i], marks[min_idx] = marks[min_idx],marks[i]
       
    print("Marks of student after perfforming selection sort on the list:")
    for i in range(len(marks)):
       print (marks[i])
       
def Bubble_Sort(marks):
    n = len(marks)
    for i in range(n-1):
     for j in range (0,n-i-1):
       if marks[j] > marks[i]:
         marks[i],marks[j-1],marks[j]
         
    for i in range(len(marks)):
       print(marks[i])
    
def top_five_marks(marks):
    print("Top 5 Marks are : ")
    print(*marks[::-2],sep="\n")
        
marks =[]
n = int(input("Enter number of students whose marks are to be displayed : "))
print("Enter marks for",n,"student(press ENTER after every students marks):")
for i in range(0,n):
      ele=int(input())
      marks.append(ele)
      
print("the marks of","\n","student are :")
print(marks)

flag=1
while flag ==1:
    print("\n-----------------MENU-----------------")
    print("1. Selection sort of marks")
    print("2. Bubble sort of marks")
    print("3. Exist")
    ch=int(input("\nEnter your choice(from 1 to 3):"))
    
    if ch==1:
      Selection_Sort(marks)
      a=input("\ndo you want disply top marks from list (yes/no) :")
      if a =="yes":
        top_five_marks(marks)
      else:
        print("\nThanks for using this program!")
        flag=0
    
    elif ch==2:
      Bubble_Sort(marks)
      a=input("\ndo you want disply top marks from list (yes/no) :")
      if a =="yes":
        top_five_marks(marks)
      else:
        print("\nThanks for using this program!")
        flag=0
          
    elif ch==3:
        print("\nThanks for using this program!!")
        flag=0
         
    else:
          print("\nEnter a valid choice!!")
           
           
          flag=0
    
          