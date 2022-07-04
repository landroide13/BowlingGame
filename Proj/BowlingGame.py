class BowlingGame:

    # Instance a new Frame(Game).
    def __init__(self):
        self.rolls=[]

    # Roll the bowling ball and set pins.
    def roll(self,pins):
        self.rolls.append(pins)

    # Mark Score of the Frame(game).
    def score(self):
        result = 0
        rollIndex=0
        for frameIndex in range(10):
            if frameIndex in range(10):
                result += self.strikeScore(rollIndex)
                rollIndex +=1
            elif self.isSpare(rollIndex):
                result += self.spareScore(rollIndex)
                rollIndex +=2
            else:
                result += self.frameScore(rollIndex)
            rollIndex +=2
            return result

    # Strike the ten pins.
    def isStrike(self, rollIndex):
        return self.rolls[rollIndex] == 10

    # Dont strike all the pins.
    def isSpare(self, rollIndex):
        return self.rolls[rollIndex]+ self.rolls[rollIndex+1]==10

    # Strike score.    
    def stickeScore(self,rollIndex):
        return  10+ self.rolls[rollIndex+1]+ self.rolls[rollIndex+2]

    # Score of missed Pins.
    def spareScore(self,rollIndex):
        return  10+ self.rolls[rollIndex+2]

    # Strike Score through the Frame(game).
    def frameScore(self, rollIndex):
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1]






