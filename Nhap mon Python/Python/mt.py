def rotateOuterRing(mat):
    m = len(mat)
    n = len(mat[0])

    # 1) Lấy danh sách phần tử của vòng ngoài theo chiều kim đồng hồ
    ring = []

    # Top row (trái → phải)
    for j in range(n):
        ring.append(mat[0][j])

    # Right column (trên → dưới, trừ góc đã lấy)
    for i in range(1, m):
        ring.append(mat[i][n-1])

    # Bottom row (phải → trái, trừ góc đã lấy)
    for j in range(n-2, -1, -1):
        ring.append(mat[m-1][j])

    # Left column (dưới → trên, trừ góc đã lấy)
    for i in range(m-2, 0, -1):
        ring.append(mat[i][0])

    # 2) Xoay vòng 1 bước theo chiều kim đồng hồ
    ring = [ring[-1]] + ring[:-1]

    # 3) Gán lại vào ma trận theo thứ tự vòng ngoài
    index = 0

    # Top row
    for j in range(n):
        mat[0][j] = ring[index]
        index += 1

    # Right column
    for i in range(1, m):
        mat[i][n-1] = ring[index]
        index += 1

    # Bottom row
    for j in range(n-2, -1, -1):
        mat[m-1][j] = ring[index]
        index += 1

    # Left column
    for i in range(m-2, 0, -1):
        mat[i][0] = ring[index]
        index += 1

    return mat
