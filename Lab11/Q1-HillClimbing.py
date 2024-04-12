import random

class NQueens:
    def __init__(self, N):
        self.N = N
        self.board = [-1] * N
        self.initialize_board()

    def initialize_board(self):
        for i in range(self.N):
            self.board[i] = random.randint(0, self.N - 1)

    def display_board(self):
        for row in range(self.N):
            line = ""
            for col in range(self.N):
                if self.board[col] == row:
                    line += "Q "
                else:
                    line += ". "
            print(line)
        print("Attacking pairs:", self.get_attacking_pairs())
        print("Non-attacking pairs:",self.get_non_attacking_pairs())
        

    def get_attacking_pairs(self):
        attacking_pairs = 0
        for i in range(self.N):
            for j in range(i + 1, self.N):
                if self.board[i] == self.board[j] or abs(self.board[i] - self.board[j]) == abs(i - j):
                    attacking_pairs += 1
        return attacking_pairs
    
    def get_non_attacking_pairs(self):
        total_possible_pairs = (self.N * (self.N - 1)) // 2
        attacking_pairs = self.get_attacking_pairs()
        return total_possible_pairs - attacking_pairs


    def hill_climbing(self):
        current_attacking_pairs = self.get_attacking_pairs()
        iterations = 0
        while current_attacking_pairs > 0:
            iterations += 1
            best_moves = []
            min_attacking_pairs = current_attacking_pairs
            for i in range(self.N):
                for j in range(self.N):
                    if j != self.board[i]:
                        original_col = self.board[i]
                        self.board[i] = j
                        new_attacking_pairs = self.get_attacking_pairs()
                        if new_attacking_pairs < min_attacking_pairs:
                            min_attacking_pairs = new_attacking_pairs
                            best_moves = [(i, j)]
                        elif new_attacking_pairs == min_attacking_pairs:
                            best_moves.append((i, j))
                        self.board[i] = original_col
            if not best_moves:
                break
            row, col = random.choice(best_moves)
            self.board[row] = col
            current_attacking_pairs = min_attacking_pairs
            print("Iteration:", iterations, "Attacking pairs:", current_attacking_pairs)

if __name__ == "__main__":
    N = 100  
    queens = NQueens(N)
    print("Initial Board:")
    queens.display_board()
    queens.hill_climbing()
    print("Final Board:")
    queens.display_board()
