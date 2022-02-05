#Introduction to the game, city ASCII art by amc 99 (?)
print('''      
                               .-~ | ~-.
                               |   |   |
                               |  _:_  |                    .-:~--.._
                             .-"~~ | ~~"-.                .~  |      |
            _.-~:.           |     |     |                |   |      |
           |    | `.         |     |     |                |   |      |
  _..--~:-.|    |  |         |     |     |                |   |      |
 |      |  ~.   |  |         |  __.:.__  |                |   |      |
 |      |   |   |  |       .-"~~   |   ~~"-.              |   |      |
 |      |   |  _|.--~:-.   |       |       |         .:~-.|   |      |
 |      A   | |      |  ~. |       |   _.-:~--._   .' |   |   |      |
 |      M   | |      |   | |       |  |   |     |  |  |   |   |      |
 |      C   | |      |   | |       |  |   |     |  |  |   |   |      |
 |      |   | |      |   | |       |  |   |     |  |  |   |   |      |
 |      9   | |      |   | |       |  |   |     |  |  |   |   |      |
 |      9   | |      |   | |       |  |   |     |  |  |   |   |      |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ''')
print("You woke up in a dark room, without memories of how you end up here!")
print("From unknown source you hear following words:")
print("'Welcome to the mysterious City.'")
print("'Your mission is to escape!'")

#Brief declaring of rules
print("On each intersection you will need to choose your path.")
print("'Every action has reaction!'")

#Adding some white space
print("\n"*10)
print("Let's Start!")
print("\n"*10)

#start of the game
print("You look around and you notice some light, coming under something that appears like a door!")
print("You open the door and now you have to choose:")

#variable declaring for the first choice 
choice1 = input("Do you want to go Left or Right(L/R): ")
choice1_low = choice1.lower()

#First intersection
#Going left
if (choice1_low == 'l') or (choice1_low == 'left'):
  print("You went left")
  print("You are running down the hallway!")
  print("The path is narrowing down.")
  print("Slowly you are starting to run out of the air!")
  print("You try to turn around, but scary noises are pushing you further into the darkness!")
  print("Eventually you lost your breath!")
  print("GAME OVER")

#Going right
elif (choice1_low == 'r') or (choice1_low == 'right'):
  print("After walking 100m, you have reached an old wooden bench with a backpack sitting on it.")
  print("You lift the backpack, it feels pretty heavy. You decide to look inside!")
  print("You see inside a wrench, bundle of ropes, pack of tissues and three lighters! ")
  print("Weight of backpack doesn't match it contents. You are confused :S.")

  #second intersection(also a sub intersection) - backpack
  choice2r_backpack = input("Do you want to take a backpack with you?(y/n)")
  backpack_low = choice2r_backpack.lower()

  #Going with backpack
  if (backpack_low == 'y') or (backpack_low == 'yes'):
    print("You choosed to take the backpack with you.")
    print("You are walking forward, backpack is slowing you down.")
    print("Thinking that ropes and few other items may be usefull, you decide against dropping the backpack.")
    print("You get out of abandoned warehouse!")
    print("There are small city car and middle sized motorcycle, both with the keys in igniton!!")

    #final choice on the right path with backpack
    choice3_r = input("What do you take?(Car/Motorcycle): ")
    vehicle_choice = choice3_r.lower()
    if (vehicle_choice == "car") or (vehicle_choice == "c"):
      print("You sit in the car and drive away!")
      print("After 5min the bomb that was hidden in backpack exploded!!!!!!!")
      print("'GAME OVER'")

    elif (vehicle_choice == "motorcycle") or (vehicle_choice == "m"):
      print("You sit on the motorcycle and ride away!")
      print("After 5min the bomb that was hidden in backpack exploded!!!!!!!")
      print("'GAME OVER'")

    #Invalid choice  
    else:
      print("You couldn't make valid choice!")
      print("After 5min the bomb that was hidden in backpack exploded!!!!!!!")
      print("'GAME OVER'")


  #Going without the backpack
  else:
    print("You choosed to leave the backpack alone.")
    print("You are quickly moving down the halls,\nand you get out of old abandoned warehouse.")
    print("There are small city car and middle sized motorcycle, both with the keys in igniton!!")

    #Choosing the vehicle
    choice3_r2 = input("What do you take?(Car/Motorcycle): ")
    vehicle_choice_without_backpack = choice3_r2.lower()

    #Vehicle choice without backpack
    if (vehicle_choice_without_backpack == "car") or (vehicle_choice_without_backpack == "c"):
      print("You sit in the car and drive away!")
      print("After 5min you arrive to the intersection.")
      print("On the left side is the tunnel, that seems to leads under the sea.")
      print("On the right there is a bridge, it seems that it leads to the big gates")
      choice4_car = input("Do you want to go Left or Right?(L/R)")
      car = choice4_car.lower()

      #Car left without backpack
      if (car == 'l') or (car == 'left'):
        print("You choosed left road.")
        print("You are driving down the nice scenic road!")
        print("You enter the tunnel and after 200m the tunnel collapses!!!")
        print("'GAME OVER'")

      #Car right without backpack
      elif (car == 'r') or (car == 'right'):
        print("You choosed the right road,leading to the bridge.")
        print("After driving for some time you arrived at the gate")
        print("It appears to be closed!")
        print("You look around.")
        print("You have spotted a console!")
        print("You have opened the gate!!!")
        print("You escaped the city with a brand new Blue Trabant!!!!")
        print("Congratulations!")

      #Invalid choice
      else:
        print("You couldn't make valid choice!")
        print("After 5min the bomb that was hidden in backpack exploded!!!!!!!")
        print("'GAME OVER'")

    #Motorcycle
    elif (vehicle_choice_without_backpack == "motorcycle") or (vehicle_choice_without_backpack == "m"):
      print("You sit on the motorcycle and ride away!")
      print("You hear a loud noise quickly aproaching from the far!")
      print("It appears that plane is crashing straight into you!")
      print("You managed to dodge the crashing plane")
      print("Unfortunately you didn't have the helmet and flying toilet lid hit you straight in the head!!")
      print("'GAME OVER'")
    #Invalid choice
    else:
      print("You couldn't make valid choice!")
      print("After 5min the bomb that was hidden in backpack exploded!!!!!!!")
      print("'GAME OVER'")


#unvalid choice == game over
else:
  print("You couldn't make a valid choice!")
  print("Something sneaked from the back, and ate you!!!")
  print("Game over!!")

