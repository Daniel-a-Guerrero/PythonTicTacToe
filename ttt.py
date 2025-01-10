class LocationOverride(Exception):
    def __init__(self, message):
        self.message=message

class TBoard():
    def __init__(self, board=[' ']*9):
        self.board=board
        self.turns=0
        self.won=False
        self.turn='X'
    def switch(self):
        self.turn='Y' if (self.turn=='X') else 'X'
    def declareVictory(self, winner):
        print(f"Win for {winner}")
        self.won=True
    def checkForWin(self):
        winPatterns=[[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        for win in winPatterns:
            if(self.board[win[0]]==self.board[win[1]]==self.board[win[2]]!=' '):
                self.declareVictory(self.board[win[0]])
            
    def place(self, x, y):
        try:
            if not (x in range(3) and y in range(3)):
                raise ValueError(f"Coordinates not within bounds")
            place=(3*(2-y))+x
            if self.board[place]==' ':
                self.board[place]=self.turn
                self.switch()
                self.turns+=1
                if(self.turns>4):
                    self.checkForWin()
                    if(self.won==True):
                        return None
                if(self.turns==9):
                    self.declareVictory("Nobody")
            else:
                raise LocationOverride(f"({x}, {y}) is already taken by {self.board[place]}")
        except ValueError as e:
            print(f"Error: {e}")
        except LocationOverride as e:
            print(f"Location Error: {e}")
    def __str__(self):
        r=f"Turn: {self.turn}\n"
        for i, row in enumerate(self.board):
            for item in row:
                r+=f"| {item} |"
                if((i+1)%3==0):
                    r+="\n"+("|===|"*3)+"\n"
        return r
def main():
    b=TBoard()
    while (b.won==False):
        if(b.turn=='X'):
            print(f"Turn: {b.turns+1}")
            x=int(input("Enter X position: "))
            y=int(input("Enter Y position: "))
            b.place(x, y)
            print(b)
        elif(b.turn=="Y"):
            for i, ix in enumerate(b.board):
                if(ix==' '):
                    b.place(i%3, 2-(i//3))
                    break
            print(b)


if (__name__=="__main__"):
    main()