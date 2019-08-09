
def edit_distance(str_1, str_2, m, n):

	if m == 0:
		return n
	if n == 0:
		return m

	if str_1[m - 1] == str_2[n - 1]:
		return edit_distance(str_1, str_2, m - 1, n - 1)

	return 1 + min(edit_distance(str_1, str_2, m - 1, n - 1),
				   edit_distance(str_1, str_2, m - 1, n),
				   edit_distance(str_1, str_2, m, n - 1))


str1 = "cat"
str2 = "sweat"
edit_distance(str1, str2, len(str1), len(str2))

str_1 = "sunday"
str_2 = "saturday"
edit_distance(str_1, str_2, len(str_1), len(str_2))



def editDistDP(str1, str2, m, n): 
    # Create a table to store results of subproblems 
    dp = [[0 for x in range(n+1)] for x in range(m+1)] 
  
    # Fill d[][] in bottom up manner 
    for i in range(m+1):
        for j in range(n+1):

            if i == 0: 
                dp[i][j] = j

            elif j == 0: 
                dp[i][j] = i

            elif str1[i-1] == str2[j-1]: 
                dp[i][j] = dp[i-1][j-1] 
  
            else: 
            	i = 1, j = 2

                dp[i][j] = 1 + min(dp[i][j-1],        # Insert 
                                   dp[i-1][j],        # Remove 
                                   dp[i-1][j-1])    # Replace 
  
    return dp[m][n]

editDistDP(str1, str2, len(str1), len(str2))