from typing import List

def permutations(letters: str) -> List[str]:
    perms = []
    def dfs(idx, perm):
        if idx == len(letters):
            perms.append(''.join(perm))
            return
        for letter in letters:
            if letter in perm:
                continue
            perm.append(letter)
            dfs(idx + 1, perm)
            perm.pop()
    dfs(0, [])
        
    return perms

if __name__ == '__main__':
    letters = "abc"
    res = permutations(letters)
    for line in sorted(res):
        print(line)
