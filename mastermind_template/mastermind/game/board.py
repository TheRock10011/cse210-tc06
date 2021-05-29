import random


class Board:
   """The responsibility of the board class is to keep track of the x’s and o’s in the game. 
   2.These are function it will need in order to run the game properly.a.Define the ‘self’ function for you class.
   """
  
    


   def apply(self, move):
      pass
      #pile = move.get_pile()
      #stones = move.get_stones()
      #self._piles[pile] = max(0, self._piles[pile] - stones)



   def is_winner(self, correctCodeState):
      dummyCounter = 0
      for i in range(len(correctCodeState)):
         if correctCodeState[i] == "x":
            dummyCounter += 1
      
      if dummyCounter >= 4:
         return True
      else:
         return False

   


   def listToString(self, string): 
    
    # initialize an empty string
      str1 = "" 
    
    # traverse in the string  
      for ele in string: 
        str1 += ele  
    
    # return string  
      return str1 
        
   def to_string(self, players, currentCode):
      
      text =  "\n--------------------"
      newCurrentCode = self.listToString(currentCode)
      for i in range(len(players)):
         text += (f"\n{players[i]}: {newCurrentCode}")
      text += "\n--------------------"
      return text

   def split(self, word):
      return [char for char in word]


   def useTheGuess(self, guess, code):
      #0 = wrong 1 = right
      dummyRightWrong = [0, 0, 0, 0]
      new_guess = self.split(guess) 
      for i in range(len(new_guess)):
         new_guess[i]
         new_new_guess = int(new_guess[i])
         
         if int(new_new_guess) == int(code[i]):
            
            dummyRightWrong[i] = "x"
         else:
            dummyRightWrong[i] = "o"
      return dummyRightWrong
         
   