def combination_sum(nums, target):
    dp = [[] for _ in range(target+1)]
    dp[0].append([])

    for t in range(target+1):
        sub_t_comb_set = set()
        for n in nums:
            if t-n >= 0:
                sub_row = dp[t-n]
                if sub_row:
                    for r in sub_row:
                        r_cp = r[:]
                        r_cp.append(n)
                        r_cp.sort()
                        r_cp_set = tuple(r_cp)
                        sub_t_comb_set.add(r_cp_set)
                else:
                    if n == t:
                        sub_t_comb_set.add(tuple([n]))
        dp[t] = [list(comb) for comb in sub_t_comb_set]
    return dp[target]

if __name__ == '__main__':
    a = [2,3,4]
    t = 6
    res = combination_sum(a,t)
    print(res)