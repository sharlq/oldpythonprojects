import random

words = ["Khilafah","genocid","holocust","secondnd holocust"]
x=random.choice(words)
valid = "abcdefghijklmnopqrstuvwxyz"
valid1 = valid.upper()
valid = valid + valid1
Turns = 10
missed = 0
guessmade =""
miss = ""
HM =["  0  \n"
     "     \n"
     "     \n",
     "  0  \n"
     "  |  \n"
     "     \n",
     "  0  \n"
     "  |  \n"
     " /   \n",
     " 0  \n"
     " |  \n"
     "/ \ \n",
     "\ 0  \n"
     "  |  \n"
     " / \ \n",
     "\ 0 / \n"
     "  |  \n"
     " / \ \n",
     "\ 0 /_ \n"
     "  |  \n"
     " / \ \n",
     "\ 0 /_|\n"
     "  |  \n"
     " / \ \n",
     "  0 _|\n"
     " /|\ \n"
     " / \ \n",
     ]


name = input("enter your name ")
print("welcome " + name)
print("______________________")
print("try to guess the word in less than 8 attempts")

while len(x)>0:
 main=""
 print("Guess the word")
 guess = input()


 if guess in valid:
  guessmade = guessmade +  guess
 else:
  print("Enter valid letter")
  guess = input()


 if guess in main:
  Turns = 8 - missed
  print("You have %s turn left" % Turns)
  print(HM[missed])
  missed += 1
  if Turns == 0:
    print("You Have killed him with your stupidity")
    break
  continue

 for item in x:
   i = x.index(item)
   if item in guessmade:
    main = main + item
   else:
    main = main + "_" + " "

 print(main)

 if main == x:
   print(main)
   print("You have won")
   break





 if guess not in x:
   Turns = 8 - missed
   print("You have %s turn left" %Turns)
   print(HM[missed])
   if Turns == 0:
    print("You Have killed him with your stupidity")
    break
   missed +=1


