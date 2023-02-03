import random

def choose_options():
  options = ["piedra", "papel", "tijera"]
  user_option = input("¿Piedra, papel o tijera? ")
  user_option = user_option.lower()

  if not user_option in options:
    print("* ¡Opción inválida! *")
    return None, None

  computer_option = random.choice(options)

  print("Tú Opción => ", user_option)
  print("Opción de la compu => ", computer_option)
  return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
  if user_option == computer_option:
    print(f"*** ¡Empatate! La compu también eligió {computer_option}. ***")
  elif user_option == "piedra":
    if computer_option == "tijera":
      user_wins += 1
      print(f"**** La compu eligió {computer_option}. ¡Ganáste! ****")
    else:
      computer_wins += 1
      print(f"**** ¡Upps, perdíste! La compu eligió {computer_option}. ****")
  elif user_option == "tijera":
    if computer_option == "papel":
      user_wins += 1
      print(f"**** La compu eligió {computer_option}. ¡Ganáste! ****")
    else:
      computer_wins += 1
      print(f"¡Upps, perdíste! La compu eligió {computer_option}. ****")
  elif user_option == "papel":
    if computer_option == "piedra":
      user_wins += 1
      print(f"**** La compu eligió {computer_option}. ¡Ganáste! ****")
    else: 
      computer_wins += 1
      print(f"**** ¡Upps, perdíste! La compu eligió {computer_option}. ****")
  return user_wins, computer_wins

def check_winner(user_wins, computer_wins):
  if user_wins == 3:
    print("*********************************")
    print("*    ¡Ganaste el campeonato!    *") 
    print("*                               *")
    print("*********************************") 
    exit()

  if computer_wins == 3:
    print("********************************************")
    print("*    ¡Qué mal! ¡La computadora te ganó!    *") 
    print("*                                          *")
    print("********************************************")
    exit()

def run_game():
  user_wins = 0
  computer_wins = 0
  rounds = 1

  while True:
    print("*" * 40)
    print("    RONDA", rounds)
    print("    TÚ => ", user_wins)
    print("    COMPUTADORA => ", computer_wins)
    print("*" * 40)
    rounds += 1

    user_option, computer_option = choose_options()
    user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)
    check_winner(user_wins, computer_wins)

run_game()