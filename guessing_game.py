class GuessingGame:
    def __init__(self, answer):
        self.answer=answer  
    
    def guess(self,gues=None,solved=False):
        self.gues=gues
        self.solved=solved
        if self.gues==None:
            return solved
        elif self.gues>self.answer:
            return 'high'
        elif self.gues<self.answer:
            return 'low'
        elif self.gues==self.answer:
            self.solved= True
            return 'correct'
        
#game=GuessingGame(10)
#print(game.answer)
#print(game.guess(15))
#print(game.guess(5))
#print(game.solved)
#print(game.guess(10), game.solved)
#print(game.guess())