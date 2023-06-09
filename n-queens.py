import numpy as np
import copy

# Noah Finestone

class n_queens: 

    def __init__(self, n):
        # generate a random board state as the starting state
        self.state = np.random.randint(0, n, size=n)

    # returns all neighboring states - neighboring states are other state's
    # board configurations that differ w.r.t only one queen,
    # for all queens in each column, given an initial state
    def getNeighborStates(self, pArray):
        neighbors = []
        for i in range(len(pArray)):
            for j in range(len(pArray)):
                new = copy.deepcopy(pArray)
                # find all successors of our state such that row != col for the queen we are looking at
                if j != pArray[i]:
                    new[i] = j
                    neighbors.append(new)
        return neighbors

    # evaluation function, returns number of collisions for a given state
    def numberOfCollisions(self, pArray): 
        numCollisions = 0
        # checking condition for all queens -> for each col, for each row in col
        for i in range(len(pArray)):
            for j in range(len(pArray)):
                if i != j:
                    # cannot be in same diagonal  
                    if abs(pArray[i] - pArray[j]) == abs(i - j):
                        numCollisions += 1
                    # cannot be in same row
                    if pArray[i] == pArray[j]:
                        numCollisions += 1 
        return numCollisions

        
    # main function that uses best first hill climbing
    def nQueens(self, start): 
        best = start
        currentEval = self.numberOfCollisions(start)

        while True:
            board = best
            # generate all neighboring states
            neighborStates = self.getNeighborStates(board)
            # go through all neighboring states
            for state in neighborStates:
                neighborEval = self.numberOfCollisions(state)
                # we care about the state with the lowest number of collisions 
                if neighborEval < currentEval:
                    board = state
                    currentEval = neighborEval 

            # if we have reached a peak
            if np.array_equal(board, best):
                return best
            best = board

            
    # n-queens with random-restart hill-climbing to escape local minimum
    def nQueensRR(self):
        localMin = 0
        state = self.nQueens(self.state)

        while True:
            # if the peak is a global optimum
            if self.numberOfCollisions(state) == 0:
                break
            # otherwise we have reached a local minimum
            else:
                # random restart if it is not a solution
                state = np.random.randint(0, n, size=n)
                state = self.nQueens(state)
                localMin += 1
        print("####ANSWER####")
        print("LOCAL MINS HIT: " + str(localMin))
        print("COLLISIONS: " + str(self.numberOfCollisions(state)))
        return state
         
            

if __name__ == '__main__': 
    n = 8
    nQueens = n_queens(n)
    print("N = " + str(n))
    stateQueen = nQueens.state
    print("INITIAL BOARD STATE: " + "[" + str(', '.join(map(str, stateQueen))) + "]")
    state = nQueens.nQueensRR()
    commaSeparated = ', '.join(map(str, state))
    print("FINAL STATE: [" + commaSeparated + "]")








