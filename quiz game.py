print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing != "yes" :
    quit()

print("Okay! Let's play :)")
scroe = 0
answer = input("what does CPU stand for? ")
if answer == "central processing unit":
   print('correct!')
   scroe += 1
else:
   print("Incorrect!")

answer = input("what does RAM stand for? ")
if answer == "random access memory":
 print('correct!')
 scroe += 1
else:
   print("Incorrect!")

answer = input("what does PSU stand for? ")
if answer ==  "power supply":
 print('correct!')
 scroe += 1
else:
   print("Incorrect!")

answer = input("what does GPU stand for? ")
if answer == "graphics processing unit":
 print('correct!')
 scroe += 1
else:
   print("Incorrect!")

   print("you got " + str(scroe) + "questions correct!")
   print("you got " + str((scroe / 4) *100) +"%.")


