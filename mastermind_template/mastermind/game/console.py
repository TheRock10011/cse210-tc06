class Console:
    """The responsibility of the console class is to get text or numerical inputand display text output. 
    2.These are function it will need in order to run the game properly.a.Define the ‘self’ function for you class.
    """
    def read(self, prompt):
        
        return input(prompt)

    def read_number(self, prompt):
       
        return int(input(prompt))
        
    def write(self, text):
        
        print(text)