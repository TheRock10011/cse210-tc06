class Move:
    """A manuver in the game. 
    Responsibility: Keep track of what numbers have been guessed correctly

    Sterotype: Information Holder

    Attributes: 
        
    """
    def __init__(self, pile, charcters):
        """
        pile = the row of input (similar to the stones game from Solo Checkpoint)
        characters = the indiviual instances of the password characters (much like 'stones')
        """
        self._pile = pile
        self._characters = charcters

    def get_pile(self):
        """Returns the pile to change 
        """
        return self._pile

    def get_characters(self):
        """Returns the number of characters to remove
        """
        return self._stones 
        