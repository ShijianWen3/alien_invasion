

class User:
    def __init__(self) -> None:
        self.score=0
        self.level=0
        self.last_level=0
        self.MaxScore=self.get_max()
    
    def score_add(self,num:int):
        self.score+=num
        if self.score>=self.MaxScore:
            self.MaxScore=self.score
        self.level=self.score//100
        
    def reset(self):
        self.score=0
        self.level=0
    def get_max(self):
        with open('./MaxScore.txt') as file:
            score=eval(file.read())
        return score
    
    def storage_max(self):
        with open('./MaxScore.txt','w') as file:
            file.write(str(self.MaxScore))
        