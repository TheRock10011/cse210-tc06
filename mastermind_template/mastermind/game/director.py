from game.board import Board
from game.console import Console
from game.move import Move
from game.player import Player
from game.roster import Roster
import random

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        board (Hunter): An instance of the class of objects known as Board.
        console (Console): An instance of the class of objects known as Console.
        keep_playing (boolean): Whether or not the game can continue.
        move (Rabbit): An instance of the class of objects known as Move.
        roster (Roster): An instance of the class of objects known as Roster.
    """

    def __init__(self):

        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self._board = Board()
        self._console = Console()
        self._keep_playing = True
        self._move = None
        self._roster = Roster()


        self.create_code = random.randint(1000, 9999)
        self.code = str(self.create_code)
        self.code = self.split(self.code)
        print(self.code)
        self.correct_code_solved_so_far = ["*", "*", "*", "*"]

        self.Players = ""

    def split(self,word):
        return [char for char in word]



    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        self._prepare_game()
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _prepare_game(self):
        """Prepares the game before it begins. In this case, that means getting the player names and adding them to the roster.
        
        Args:
            self (Director): An instance of Director.
        """
        playerCount =  int(input("How many players will there be? "))
        
        for n in range(playerCount):
            name = self._console.read(f"Enter a name for player {n + 1}: ")
            
            player = Player(name)
            self._roster.add_player(player)
    
    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the move from the current player.

        Args:
            self (Director): An instance of Director.
        """
        # display the game board
        player = self._roster.get_all_players()
        self.players = self._roster.get_all_players()
        
        

        newPlayers = self._board.to_string(self.players, self.correct_code_solved_so_far)
        
        
        self._console.write(newPlayers)
        
        player = self._roster.get_current()
        self._console.write(f"{player.get_name()}'s turn:")
        theGuess = self._console.read("What is your guess? ")



        
        
        self.correct_code_solved_so_far = self._board.useTheGuess(theGuess, self.code)
        

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means updating the board with the current move.

        Args:
            self (Director): An instance of Director.
        """
       
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if there are stones left and declaring the winner.

        Args:
            self (Director): An instance of Director.
        """
        
        if self._board.is_winner(self.correct_code_solved_so_far):
            winner = self._roster.get_current()
            name = winner.get_name()
            print(f"\n{name} won!")
            self._keep_playing = False
        self._roster.next_player()

     
       