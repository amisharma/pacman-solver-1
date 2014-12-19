A=[[0 for x in range(10)] for y in range(10)]
i=0
while i<10:
	j=0
	while j<10:
		A[i][j]=i+j
		j+=1
	i+=1
print A

( (current_state[0][0] - i[0]) ** 2 + (current_state[0][1] - i[1]) ** 2 ) ** 0.5