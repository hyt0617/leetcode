# !/usr/bin/env python
# -*-coding: utf-8 -*-


def exist(board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """
    def match(i, j, board, c):
        valid = []
        if board[i-1][j] == c:
            valid.append((i-1, j))
        if board[i][j-1] == c:
            valid.append((i, j-1))
        if board[i][j+1] == c:
            valid.append((i, j+1))
        if board[i+1][j] == c:
            valid.append((i+1, j))
        return valid

    def travel(start_ind_list, board, words, path, results):
        if not words:
            for sil in start_ind_list:
                if sil not in path:
                    results.append(path + [sil])
            return
        for index in start_ind_list:
            start_x, start_y = index
            next_steps = match(start_x, start_y, board, words[0])
            if next_steps:
                if (start_x, start_y) not in path:
                    path.append((start_x, start_y))
                    travel(next_steps, board, words[1:], path, results)
                    path.pop()
                else:
                    continue
            else:
                continue
            if results:
                return
    m = len(board)
    n = len(board[0]) if m else 0
    if m * n < len(word):
        return False
    extend_board = [[0] * (n+2) for i in range(m+2)]
    for i in range(0, m+2):
        for j in range(0, n+2):
            if 1 <= i <= m and 1 <= j <= n:
                extend_board[i][j] = board[i-1][j-1]
            else:
                extend_board[i][j] = 0
    # find all possible index for first char
    possible_index = []
    for i in range(m):
        for j in range(n):
            if board[i][j] == word[0]:
                possible_index.append((i+1, j+1))

    results = []
    travel(possible_index, extend_board, word[1:], [], results)
    print(results)
    return True if results else False


print(exist([["a","a","a"],["a","b","b"],["a","b","b"],["b","b","b"],["b","b","b"],["a","a","a"],["b","b","b"],["a","b","b"],["a","a","b"],["a","b","a"]], "aabaaaabbb"))
print(exist([['a', 'a']], 'aa'))
print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))
print(exist([["C","A","A"],["A","A","A"],["B","C","D"]], "AAB"))
print(exist([["a", "a"]], "aaa"))
print(exist([["A", "B"], ["D", "C"]], "ABCD"))
print(exist([["A", "B"], ["C", "D"]], "ABCD"))
print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))