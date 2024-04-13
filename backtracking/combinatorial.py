from typing import List

def letter_combination(n: int) -> List[str]:
    paths = []
    def dfs(start_idx, path):
        if start_idx == n:
            paths.append("".join(path))
            return
        for edge in ["a", "b"]:
            path.append(edge)
            dfs(start_idx + 1, path)
            path.pop()
    dfs(0, [])
    return paths

if __name__ == '__main__':
    n = 2
    res = letter_combination(n)
    for line in sorted(res):
        print(line)
