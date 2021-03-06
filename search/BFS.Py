# BFS

def BFS(x, visit):
	length = len(matrix)
	# the start point is 0
	ls = [0]
	ls_order = [0]
	visit[0] = 1
	while len(ls) != 0:
		i = ls.pop()
		for j in range(length):
			if matrix[i][j] == 1 and visit[j] == 0:
				visit[j] = 1
				ls.append(j)
				ls_order.append(j)
	return ls_order 


if __name__=='__main__':
	matrix = [[0,1,0,1],[1,0,1,0],[0,1,0,0],[1,0,0,0]]
	visit = [0] * len(matrix)

	ls_order = BFS(matrix, visit)
	print(ls_order)

