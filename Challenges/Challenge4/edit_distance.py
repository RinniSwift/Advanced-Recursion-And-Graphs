
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


str1 = "happy"
str2 = "happpy"
print(edit_distance(str1, str2, len(str1), len(str2)))