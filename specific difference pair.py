def specificDifferencePair(arr, K):
    arr.sort() 
    N=len(arr)
    dp = [0] * N
    dp[0] = 0
    for i in range(1, N):
        dp[i] = dp[i-1]
        if (arr[i] - arr[i-1] < K):
            if (i >= 2): 
                dp[i] = max(dp[i], dp[i-2] + arr[i] + arr[i-1]); 
            else: 
                dp[i] = max(dp[i], arr[i] + arr[i-1]);
    return dp[N - 1]
