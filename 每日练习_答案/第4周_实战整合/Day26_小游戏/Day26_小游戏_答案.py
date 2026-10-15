# ===== Day26_小游戏 参考答案 =====

# 【题1】井字棋（双人版）：3x3 棋盘，轮流落子，判断胜负。
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

board = [[" "]*3 for _ in range(3)]
player = "X"
for turn in range(9):
    print_board(board)
    try:
        r = int(input(f"玩家{player} 行(0-2): "))
        c = int(input(f"玩家{player} 列(0-2): "))
    except ValueError:
        print("请输入数字")
        continue
    if board[r][c] != " ":
        print("此处已有棋子")
        continue
    board[r][c] = player
    if check_win(board, player):
        print_board(board)
        print(f"玩家{player}获胜！")
        break
    player = "O" if player == "X" else "X"
else:
    print("平局")

# 想跑交互版取消注释: main 循环已内置，直接运行本文件即可

# ==================================================

