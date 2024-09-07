import random
stages= ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
word_list =["baboon","camel","lion","cat"]
word = random.choice(word_list)
revel=[]
word_length=len(word)
end_game= False
lives=6
for _ in range(word_length):
  revel+="_"

  
while not end_game:
  guess_word= input("Guess a letter ").lower()

  for position in range(word_length):
    letter= word[position]
    if letter==guess_word:
      revel[position]=letter
      
  if guess_word not in word:
    lives-=1
    if lives==0:
      end_game=True
      print("You lose")
    
  print(f"{' '.join(revel)}")

  if "_" not in revel:
    end_game=True
    print("YOU WON")
    
  print(stages[6-lives])