# 
# function search() is a function that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space


grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]

heuristic = [[9, 8, 7, 6, 5, 4],
             [8, 7, 6, 5, 4, 3],
             [7, 6, 5, 4, 3, 2],
             [6, 5, 4, 3, 2, 1],
             [5, 4, 3, 2, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost, heuristic):
    #open list elements are of the type: [g, x, y]
    #closed list is a list for cells that has been expanded before, so we don't repeat expansion
	closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
	closed[init[0]][init[1]] = 1 	#initialized starting location as checked
	expand = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]

	x = init[0]
	y = init[1]
	g = 0
	f = g + heuristic[x][y]

	open = [[f, x, y]]	#put f at first to be able to catch smallest f-value

	found = False #flag that is set when search complete
	resign = False #flag set if we can't find expand 	,	it will be the case when open list is empty
	count = 0  #count number of expands, i.e: g-value

	#these lines for Debugging
		#print 'initial open list:'
		#for i in range(len(open)):
			#print '  ', open[i]
		#print '----'

	while found is False and resign is False:

		# check if we still have elements on the open list
		if len(open) == 0:
			resign = True
			print 'fail'
			#print '##### Search terminated without success'

		else:
			# remove node with smallest g-value from list
			open.sort()	#sort elements in increasing order, so g-value will be 1st node
			open.reverse()	#switch 1st node to last node, to pop node with smallest g-value out
			next = open.pop() #assign next to node with smallest g-value
			#print 'take list item'
			#print next
			x = next[1]	#new x
			y = next[2]	#new y
			f = next[0]	#new f

			expand[x][y] = count
			count += 1

			#check if we are done

			if x == goal[0] and y == goal[1]:
				found = True
				#print next
				#print '###### Search successful'

			else:
				# expand winning element and add to new open list
				for i in range(len(delta)):
					x2 = x + delta[i][0]
					y2 = y + delta[i][1]
					if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]):	#if x2 and y2 falls into the grid
						if closed[x2][y2] == 0 and grid[x2][y2] == 0:	#if [x2,y2] is not checked, and [x2,y2] is not an obstacle
							g2 = g + cost	#increament the cost, which is g-value
							f = g2 + heuristic[x2][y2]
							open.append([f, x2, y2])	#add the new triplet to my open list
							#print 'append list item'
							#print [g2, x2, y2]
							closed[x2][y2] = 1 	#check [x2,y2] to never expand it again
							
	for i in range(len(expand)):
		print expand[i]

			#print 'new open list:'
			#for i in range(len(open)):
				#print '  ', open[i]
			#print '----'



search(grid,init,goal,cost, heuristic)