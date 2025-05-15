def find_connected_components(matrix):
    """
    Find all connected components in a binary matrix.

    Args:
        matrix (list of list of int): A binary matrix where 1 represents land and 0 represents water.

    Returns:
        list of list of tuple: A list of connected components, where each component is represented as a list of (row, col) tuples.
    """
    if not matrix or not matrix[0]:
        return []

    rows, cols = len(matrix), len(matrix[0])
    visited = [[False] * cols for _ in range(rows)]
    components = []

    def dfs(r, c, component):
        if r < 0 or r >= rows or c < 0 or c >= cols or visited[r][c] or matrix[r][c] == 0:
            return
        visited[r][c] = True
        component.append((r, c))
        # Explore all 8 directions
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                dfs(r + dr, c + dc, component)

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1 and not visited[i][j]:
                component = []
                dfs(i, j, component)
                components.append(component)

    return components
# Example usage
if __name__ == "__main__":
    matrix = [
        [1, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 1]
    ]
    print(find_connected_components(matrix))
# The output represents the connected components in the binary matrix.

