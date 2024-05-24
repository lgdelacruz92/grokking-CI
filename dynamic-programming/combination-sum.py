def dfs(nums, i, s, t, cur, res, memo):
    if nums[i] in memo:
        return
    if s > t:
        return
    if i >= len(nums) or s == t:
        if s == t:
            res.append(cur[:])
        return
    memo.add(nums[i])
    cur.append(nums[i])
    dfs(nums, i, s + nums[i], t, cur, res, memo)
    cur.pop()
    dfs(nums, i+1, s, t, cur, res, memo)

def combination_sum(nums, target):
    res = []
    memo = set()
    dfs(nums, 0, 0, target, [], res, memo)
    return res

if __name__ == '__main__':
    a = [2,3,4]
    t = 6
    res = combination_sum(a, t)
    print(res)