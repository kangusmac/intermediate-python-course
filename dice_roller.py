def main():
  import random
  dice_rolls = int(input('How many dices would you like ti roll?'))
  dice_sizes = int(input('How many sides are the dice?'))
  dice_sum   = 0
  for i in range(0,dice_rolls):
    roll = random.randint(1,6)
    dice_sum += roll
    if roll == 1:
      print(f'You rolled a {roll} ! Critical Fail')
    elif roll == dice_sizes:
      print(f'You rolled a {roll} ! Critical success!')
    else:
      print(f'You rolled a {roll}')
  print(f'You have rolled a total of {dice_sum}')

if __name__== "__main__":
  main()
