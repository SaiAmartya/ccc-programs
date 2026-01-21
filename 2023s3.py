def solve():        
    N, M, R, C = map(int, input().split())
    
    # Grid initialization with 'a'
    # 'a' is a palindrome of itself
    grid = [['a' for _ in range(M)] for _ in range(N)]
    
    # Case 1: R=N and C=M
    # Initial grid of all 'a's satisfies this immediately.
    if R == N and C == M:
        for row in grid:
            print("".join(row))
        return

    # Case 2: R=N (All rows must be palindromes)
    if R == N:
        # If N=1, then all columns are length 1, so they are automatically palindromes.
        # Thus, if we need C < M palindromic columns with N=1, it is impossible.
        if C < M and N == 1:
             print("IMPOSSIBLE")
             return

        # If M is even and C is odd, we cannot achieve exactly C palindromic columns
        # because palindromic columns must appear in symmetric pairs (j, M-1-j) 
        # when all rows are palindromes.
        if M % 2 == 0 and C % 2 == 1:
            print("IMPOSSIBLE")
            return
            
        # We need to break (M - C) columns.
        columns_to_break = M - C
        
        # We modify Row 0 to break columns.
        # Setting grid[0][j] = 'b' breaks columns j and M-1-j (if N > 1).
        # We perform changes symmetrically to keep Row 0 a palindrome.
        j = 0
        while columns_to_break > 0:
            if columns_to_break >= 2:
                grid[0][j] = 'b'
                grid[0][M - 1 - j] = 'b'
                columns_to_break -= 2
                j += 1
            else:
                # M must be odd here if columns_to_break is odd (and > 0)
                mid = M // 2
                grid[0][mid] = 'b'
                columns_to_break -= 1
        
        for row in grid:
            print("".join(row))
        return

    # Case 3: C=M (All columns must be palindromes)
    if C == M:
        # Symmetric to Case 2
        # If M=1, rows are length 1, always P. So R must be N.
        if M == 1 and R < N:
            print("IMPOSSIBLE")
            return
            
        if N % 2 == 0 and R % 2 == 1:
            print("IMPOSSIBLE")
            return
            
        rows_to_break = N - R
        i = 0
        while rows_to_break > 0:
            if rows_to_break >= 2:
                grid[i][0] = 'b'
                grid[N - 1 - i][0] = 'b'
                rows_to_break -= 2
                i += 1
            else:
                mid = N // 2
                grid[mid][0] = 'b'
                rows_to_break -= 1
                
        for row in grid:
            print("".join(row))
        return

    # Case 4: R < N and C < M
    # If N=1, we can't break columns (they are always length 1 palindromes) -> Impossible since C < M.
    if N == 1:
        print("IMPOSSIBLE")
        return
    # If M=1, we can't break rows (always length 1 palindromes) -> Impossible since R < N.
    if M == 1:
        print("IMPOSSIBLE")
        return

    # Strategy: 
    # 1. Fill grid with 'a'.
    # 2. Break 'N - R' rows by setting their last character to 'b'.
    # 3. Break 'M - C' columns by setting their last character (bottom row) to 'b'.
    
    # Break rows R to N-1
    for i in range(R, N):
        grid[i][M-1] = 'b'
        
    # Break columns C to M-1
    for j in range(C, M):
        grid[N-1][j] = 'b'
        
    # Edge case: If C=0, we need to ensure the broken row (N-1) doesn't accidentally form a palindrome.
    # The standard logic fills row N-1 with 'b's which might form a palindrome "bb...b".
    # We change the start of this row to 'c' to break its symmetry.
    if C == 0:
        grid[N-1][0] = 'c'
        
    # Edge case: If R=0, we need to ensure the broken column (M-1) doesn't accidentally form a palindrome.
    # The standard logic fills col M-1 with 'b's which might form a palindrome "bb...b".
    # We change the start of this column to 'c' to break its symmetry.
    if R == 0:
        grid[0][M-1] = 'c'
        
    for row in grid:
        print("".join(row))

solve()
