# Imposta il range di numeri in cui il numero immaginato può essere scelto
lower_bound = 1
upper_bound = 100

# Imposta il numero di tentativi che ogni giocatore può fare per indovinare il numero
max_attempts = 10

# Chiedi al primo giocatore di scegliere un numero segreto
secret_number = int(input("Giocatore 1, scegli un numero segreto compreso tra {} e {}: ".format(lower_bound, upper_bound)))


# Il secondo giocatore deve fare ipotesi fino a quando non indovina il numero o esaurisce tutti i tentativi
num_attempts = 0
last_guess = None
while num_attempts < max_attempts:
  # Chiedi al secondo giocatore di fare un'ipotesi
  guess = int(input("Giocatore 2, fai un'ipotesi: "))

  # Controlla se l'ipotesi del secondo giocatore è corretta
  if guess == secret_number:
    # Il secondo giocatore ha indovinato il numero, quindi il gioco è finito
    print("Indovinato! Il numero era {}".format(secret_number))
    break
  elif guess < secret_number:
    # L'ipotesi del secondo giocatore è troppo bassa, quindi dai un suggerimento e chiedi di fare un'altra ipotesi
    print("Il numero immaginato è maggiore")
  elif guess > secret_number:
    # L'ipotesi del secondo giocatore è troppo alta, quindi dai un suggerimento e chiedi di fare un'altra ipotesi
    print("Il numero immaginato è minore")

  # Incrementa il contatore dei tentativi fatti dal secondo giocatore
  num_attempts += 1

  # Memorizza l'ultima ipotesi fatta dal secondo giocatore
  last_guess = guess

# Se il secondo giocatore non è riuscito a indovinare il numero entro il numero massimo di tentativi, il gioco è finito
if num_attempts == max_attempts:
  print("Hai esaurito tutti i tentativi! Il numero era {}".format(secret_number))
