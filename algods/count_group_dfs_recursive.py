def count_group_dfs_recursive(matrix):
    def dfs(person):
        visited[person]=True
        for friend in range(len(matrix)):
            if matrix[person][friend] == 1 and not visited[friend]:
                dfs(friend)

    visited = [False] * len(matrix)
    group_count = 0

    for person in range(len(matrix)):
        if not visited[person]:
            dfs(person)
            group_count += 1
    return group_count
# Example usage:    
if __name__ == "__main__":
    matrix = [
        [1, 1, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 1, 1],
        [0, 0, 1, 1]
    ]
    print(count_group_dfs_recursive(matrix)) # Output: 2
# This code defines a function to count the number of groups in a friendship matrix using depth-first search (DFS) recursively.
# The function `count_group_dfs_recursive` takes a matrix as input, where each element indicates whether two people are friends (1) or not (0).
# It uses a helper function `dfs` to explore all friends of a person recursively, marking them as visited.
# The main function iterates through each person in the matrix, and if they haven't been visited, it calls `dfs` on them and increments the group count.
# The example usage demonstrates how to call the function with a sample matrix and prints the number of groups found.
# The output is 2, indicating that there are two groups of friends in the given matrix.