print('''
_______
      .'_/_|_\_'.
      \`\  |  /`/
       `\\ | //'
   jgs   `\|/`
           `

                        '
               '                 '
       '         '      '      '        '
          '        \    '    /       '
              ' .   .-"```"-.  . '
                    \`-._.-`/
         - -  =      \\ | //      =  -  -
                    ' \\|// '
      jgs     . '      \|/     ' .
           .         '  `  '         .
        .          /    .    \           .
                 .      .      .

''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 



left_or_right = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right'. ").lower()


if left_or_right == "left":
  swim_or_wait = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. ").lower()
  if swim_or_wait == "wait":
    which_door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose? ").lower()
    if which_door == "red":
      print("Burned by fire. Game over.")
    elif which_door == "blue":
      print("Attacked by beasts. Game over.")
    elif which_door == "yellow":
      print("You found the treasure! Enjoy your loot!")
    else:
      print("Game over.")
  else:
    print("Eaten by alligator. Game over.")
else: 
  print("Fell into a hole. Game over.")
  


