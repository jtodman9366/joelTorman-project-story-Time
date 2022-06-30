print("~Tales of UMBC~")     
print("(A Work of Fiction)")
print()
print("You are a knight in the year 650 CE, and you are trying to become the most famous knight of them all.")
print()
print("You decided to go on an adventure at castle UMBC to earn your glory!")
print()
# Make Your Selection: 
print("You are outside the castle grounds, and see three different people asking for help, you can talk to:")
print("A. The local Blacksmith, who needs a rare sword ")
print("B. The town's Teacher, who has a question ")
print("C. The King, who needs a brave warrior ")
selection  = input("Who will you talk to, Pleaes select  option 'A' - 'C': ")
if(selection == "A"):
  print("you meet with the town Blacksmith, looking for legendary sword")
  print("They tell you the legen that the sword is frozen meet with the town Blacksmith, lookin ice waiting to be found.")
  print("You choose to search for it: ")
  print("A. In the Desert ")
  print("B. In the Forest ")
  print("C. In the Arctic ")
search = input("Pleaes select  option 'A' - 'C': ")
print()
if(search == "C"):
  print("After looking long and hard through the arctic, you.ve found it -  the legendary sword of programming. The Blacksmith is thrilled and reward you with a suit of armor worthy of a hero\n ~ The End ~  ")
print()
# Make Your Selection: A, B, C
if(search  == "A" or search =="B" ):
  print("You serached and searched for the rest of your life, but never found it.It might've have been a good idea to head the blacksmith advice and go to a cold place.\n ~ The End ~  ")
  
# Make Your Selection:

print("You meet with the town teacher, who is asking you a question, 'I have to be honest with you ,' they say. 'I am not really qualified to teach and strugglin with this question 'They gesture to the math equation that reads as follow:\n\n y = 6 + 2 + 1 ") 
print()
y = input("please enter the solution to this problem: ") 
y = int(y)
print()
if(y == 9):
  print()
print("That makes perfect sense' the teacher cries and they award you with an honary degree. You are forever known as one of the smartest in the land!\n~ The End ~ ")
if(y != 9):
  print()
print("Yankee Doodle")

#The King's Story
print()
print("You are outside the castle groundschoose to search , and see three differe; ")
print("A. The local Blacksmith, who needs a rare sword ")
print("B. The town's Teacher, who has a question ")
print("C. The King, who needs a brave warrior ")
select  = input("Who will you talk to, Pleaes select  option 'A' - 'C': ")
print()
print("You meet with thwe king of UMBC, looking for a brave warrior.\n' I need someone to conquer a nearby dragon to save the kingdon! There is no time, head east and be ready for battle!")
print()
print("You head east and find the dragon. You ready yourself for battle, but in a twist, the dragon ask you to sove a riddle in exchange for your kingdom.")
print()
print("'What two numbers, when aded together, equal ten?'")
print()
print("You ponder for a moment. There ae multiple nswers to this question, aren't there?\n After thinking for a moment, you answer with two numbers...")
firstNum = input("Enter your first number: ")
firstNum = int(firstNum)
secondNum = input("Enter your second number: ")
secondNum = int(secondNum)
sum = firstNum + secondNum
print()
if(sum == 10):
    print(f"'Ah yes, {firstNum} and {secondNum} add up to 10!' the dragon explained\n The dragon decides to leave your kingdom alone, and the king declare you are the greatest hero in all the land.\n ~ The End ~  ")
if(sum != 10):
  print("We Done!")
