import pandas as pd
songs = pd.read_pickle('songs.pkl')
print('''Welcome, please select a song from this top 10 songs:''')
dic = {}
for i,j in enumerate(songs['Title']):
  dic[str(i+1)] = j
  print(f'{i+1} : {j}')
print()
play = True
while play == True:
  while play == True:
    n = input(f'Enter number or song name: ').lower().strip()
    if n in dic.keys() or n in dic.values():
      for i,j in enumerate(songs['Title']):
        if n == str(i+1) or n == j:
          print(f"You choose '{j}' by {songs.iloc[i][2]} Here you go:\n")
          print(songs.iloc[i][1])
      print()
      while True:
        select = input('Enter * to continue and q to quit: ')
        if select == 'q':
          play = False
          break
        elif select == '*':
          break
        else:
          print('Incorrect Input')
    else:
      print('Incorrect Input')
  break
