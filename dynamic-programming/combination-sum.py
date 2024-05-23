def dfs(nums, i, s, t, cur, res):
    if s > t:
        return
    if i >= len(nums) or s == t:
        if s == t:
            res.append(cur[:])
        return
    
    cur.append(nums[i])
    dfs(nums, i, s + nums[i], t, cur, res)
    cur.pop()
    dfs(nums, i+1, s, t, cur, res)

def combination_sum(nums, target):
    res = []
    dfs(nums, 0, 0, target, [], res)
    return res
if __name__ == '__main__':
    a = [2,3,4]
    t = 6
    res = combination_sum(a, t)
    print(res)