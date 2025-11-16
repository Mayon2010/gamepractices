import sys

class ChessPiece:
    def __init__(self, color):
        self.color = color

    def get_moves(self, board, x, y):
        return []

class King(ChessPiece):
    def __str__(self):
        return 'K' if self.color == 'w' else 'k'

    def get_moves(self, board, x, y):
        moves = []
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < 8 and 0 <= ny < 8:
                    if not board[ny][nx] or board[ny][nx].color != self.color:
                        moves.append((nx, ny))
        return moves

class Queen(ChessPiece):
    def __str__(self):
        return 'Q' if self.color == 'w' else 'q'

    def get_moves(self, board, x, y):
        moves = []
        directions = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            while 0 <= nx < 8 and 0 <= ny < 8:
                if board[ny][nx]:
                    if board[ny][nx].color != self.color:
                        moves.append((nx, ny))
                    break
                moves.append((nx, ny))
                nx += dx
                ny += dy
        return moves

class Rook(ChessPiece):
    def __str__(self):
        return 'R' if self.color == 'w' else 'r'

    def get_moves(self, board, x, y):
        moves = []
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            while 0 <= nx < 8 and 0 <= ny < 8:
                if board[ny][nx]:
                    if board[ny][nx].color != self.color:
                        moves.append((nx, ny))
                    break
                moves.append((nx, ny))
                nx += dx
                ny += dy
        return moves

class Bishop(ChessPiece):
    def __str__(self):
        return 'B' if self.color == 'w' else 'b'

    def get_moves(self, board, x, y):
        moves = []
        directions = [(1,1),(-1,-1),(1,-1),(-1,1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            while 0 <= nx < 8 and 0 <= ny < 8:
                if board[ny][nx]:
                    if board[ny][nx].color != self.color:
                        moves.append((nx, ny))
                    break
                moves.append((nx, ny))
                nx += dx
                ny += dy
        return moves

class Knight(ChessPiece):
    def __str__(self):
        return 'N' if self.color == 'w' else 'n'

    def get_moves(self, board, x, y):
        moves = []
        for dx, dy in [(1,2),(2,1),(-1,2),(-2,1),(1,-2),(2,-1),(-1,-2),(-2,-1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 8 and 0 <= ny < 8:
                if not board[ny][nx] or board[ny][nx].color != self.color:
                    moves.append((nx, ny))
        return moves

class Pawn(ChessPiece):
    def __str__(self):
        return 'P' if self.color == 'w' else 'p'

    def get_moves(self, board, x, y):
        moves = []
        direction = -1 if self.color == 'w' else 1
        # Move forward
        if 0 <= y + direction < 8 and not board[y + direction][x]:
            moves.append((x, y + direction))
            # First move double step
            if (self.color == 'w' and y == 6) or (self.color == 'b' and y == 1):
                if not board[y + 2 * direction][x]:
                    moves.append((x, y + 2 * direction))
        # Captures
        for dx in [-1, 1]:
            nx = x + dx
            ny = y + direction
            if 0 <= nx < 8 and 0 <= ny < 8 and board[ny][nx] and board[ny][nx].color != self.color:
                moves.append((nx, ny))
        return moves

def create_board():
    board = [[None for _ in range(8)] for _ in range(8)]
    # Place pieces
    for i in range(8):
        board[1][i] = Pawn('b')
        board[6][i] = Pawn('w')
    board[0][0] = board[0][7] = Rook('b')
    board[7][0] = board[7][7] = Rook('w')
    board[0][1] = board[0][6] = Knight('b')
    board[7][1] = board[7][6] = Knight('w')
    board[0][2] = board[0][5] = Bishop('b')
    board[7][2] = board[7][5] = Bishop('w')
    board[0][3] = Queen('b')
    board[7][3] = Queen('w')
    board[0][4] = King('b')
    board[7][4] = King('w')
    return board

def print_board(board):
    for y in range(8):
        print(8-y, end=' ')
        for x in range(8):
            piece = board[y][x]
            print(str(piece) if piece else '.', end=' ')
        print()
    print('  a b c d e f g h')

def parse_move(move):
    if len(move) != 4:
        return None
    x1 = ord(move[0]) - ord('a')
    y1 = 8 - int(move[1])
    x2 = ord(move[2]) - ord('a')
    y2 = 8 - int(move[3])
    if 0 <= x1 < 8 and 0 <= y1 < 8 and 0 <= x2 < 8 and 0 <= y2 < 8:
        return (x1, y1, x2, y2)
    return None

def main():
    board = create_board()
    turn = 'w'
    while True:
        print_board(board)
        print(f"{'White' if turn == 'w' else 'Black'} to move.")
        move = input("Enter move (e.g. e2e4): ").strip()
        if move == 'exit':
            break
        parsed = parse_move(move)
        if not parsed:
            print("Invalid move format.")
            continue
        x1, y1, x2, y2 = parsed
        piece = board[y1][x1]
        if not piece or piece.color != turn:
            print("No piece to move or wrong color.")
            continue
        moves = piece.get_moves(board, x1, y1)
        if (x2, y2) not in moves:
            print("Illegal move.")
            continue
        board[y2][x2] = piece
        board[y1][x1] = None
        turn = 'b' if turn == 'w' else 'w'

if __name__ == "__main__":
    main()