def word_break(s, word_dict):
    dp = [False for _ in range(len(s)+1)]
    dp[len(s)] = True

    for i in range(len(s)-1, -1, -1):
        for w in word_dict:
            if i + len(w) <= len(s) and s[i:i+len(w)] == w:
                dp[i] = dp[i+len(w)]
            if dp[i]:
                break
    return dp[0]
    
if __name__ == '__main__':
    s = 'catsanddog'
    d = ['cat', 'and', 'cats', 'sand', 'dog']
    s = 'highway'
    d = ["crash","cream","high","low","away"]
    res = word_break(s, d)
    print(res)