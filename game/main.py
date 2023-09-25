import random
options = ('Piedra','Papel','Tijeras')
optionsb = (1,2,3)
score_player1 = 0
score_player2 = 0
print(f"{'*'*50}\nBienvenido al juego de piedra, papel o tijera \n1 => Piedra \n2 => Papel \n3 => Tijera")
while score_player1 < 2 or score_player2 < 2:
  player1 = int(input('Selecciona una opcion (Jugador 1): '))
  player2 = random.choice(optionsb)
  if (player1 == 1 and player2 == 3) or (player1 == 3 and player2 == 2) or (player1 == 2 and player2 == 1):
    score_player1 += 1
    print(f'{"*"*50}\nJugador: {options[player1-1]} - Computadora:  {options[player2-1]}\n{"*"*50}\nJugador: {score_player1} - Computadora:  {score_player2}\n{"*"*50}\n')
    if score_player1 == 2: 
      print('Ganaste!!!')
      break
  elif (player2 == 1 and player1 == 3) or (player2 == 3 and player1 == 2) or (player2 == 2 and player1 == 1):
    score_player2 += 1
    print(f'{"*"*50}\nJugador:  {options[player1-1]} - Computadora: {options[player2-1]}\n{"*"*50}\nJugador:  {score_player1} - Computadora: {score_player2}\n{"*"*50}\n')
    if score_player2 == 2: 
      print('Gano Computadora!!!')
      break
  else:
    print(f'{"*"*50}\nEmpate :(\nJugador 1 selecciono {options[player1-1]} y computadora selecciono {options[player2-1]}\nJugador:  {score_player1} - Computadora: {score_player2}\n{"*"*50}\n')