# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

import util
def cornersHeuristic(state, problem):
  """
  A heuristic for the CornersProblem that you defined.
  
    state:   The current search state 
             (a data structure you chose in your search problem)
    
    problem: The CornersProblem instance for this layout.  
    
  This function should always return a number that is a lower bound
  on the shortest path from the state to a goal of the problem; i.e.
  it should be admissible.  (You need not worry about consistency for
  this heuristic to receive full credit.)
  """
  corners = problem.corners # These are the corner coordinates
  walls = problem.walls # These are the walls of the maze, as a Grid (game.py)
  j=0
  queue=util.PriorityQueue()
  corner_check = []
  current_state=[]
  current_state.append(state[0])
  for i in corners:
  	if not state[1][j]:
  		print"not visited",i,j
  		corner_check.append(i)
  		queue.push(i,( (current_state[0][0]-i[0]) ** 2 + (current_state[0][1] - i[1]) ** 2 ) ** 0.5)
  	j+=1
  cost=0
  j=len(corner_check)
  while j:
  	temp=queue.pop()
  	cost+=temp[1]
  	current_state[0]=temp
  	print"queue_pop", temp
  	print corner_check
  	corner_check.remove(temp)
  	while not queue.isEmpty():
  		queue.pop()
  	for i in corner_check:
  		queue.push(i,((current_state[0][0]-i[0]) ** 2 + (current_state[0][1] - i[1]) ** 2 ) ** 0.5)
  	j=j-1
  "*** YOUR CODE HERE ***"
  return cost # Default to trivial solution
 
def manhattanHeuristic(position, problem, info={}):
  "The Manhattan distance heuristic for a PositionSearchProblem"
  xy1 = position
  xy2 = problem.goal
  return abs(xy1[0] - xy2[0]) + abs(xy1[1] - xy2[1])

class SearchProblem:
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).
  
  You do not need to change anything in this class, ever.
  """
  
  def getStartState(self):
     """
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first [p 85].
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm [Fig. 3.7].
  
  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:
  """
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  start_state=problem.getStartState()
  path=[]
  path1=[]
  successors=problem.getSuccessors(problem.getStartState())
  dfs=util.Stack()
  instack=[]
  visited=[]
  parent=[]
  instack.append(start_state)
  temp=successors
  dfs.push(start_state)
  for i in successors:
  	print "init_pushed",i
  	dfs.push(i)
  	instack.append(i[0])
  flag2=0
  k=0
  flag=0
  k=0
  while flag==0:
  	temp=dfs.pop()
  	instack.remove(temp[0])
  	print "popped",temp
  	if(temp!=start_state):
  		next_state=temp[0]
  		next_action=temp[1]	
  		if next_state not in visited:
  			path.append(next_action)
  			print "not visited",next_state
  			visited.append(next_state)
  			current_state=next_state
  			if problem.isGoalState(current_state):
  				flag=1
  				print"goal state",current_state
  			else:
  				successor=problem.getSuccessors(current_state)
  				for i in successor:
  					if i[0] not in instack:
  							dfs.push(i)
  							instack.append(i[0])
  	 						parent.append(temp)
  	 						parent.append(i)
  	 						print i
  	 				if problem.isGoalState(i[0]):
  	 						parent.append(temp)
  	 						parent.append(i)
  	 						flag=1
  	 						break
  	 						
  		
  k=0
  parent2=[]
  for i in parent:
  	parent2.append(i)
  parent.reverse()
  i=parent[0]
  while i not in successors:
  	k=len(parent)
  	a=parent2.index(parent[1])
  	b=k-a-1
  	while b>0:
  		parent2.pop()
  		b=b-1
  	p=k
  	while p:
  		parent.pop()
		p=p-1
	for x in parent2:
		parent.append(x)
  	parent.reverse()
  	path.append(i[1])
  	i=parent[0]
  		
  "*** YOUR CODE HERE ***"
  path.append(parent[0][1])
  path.reverse()
  return path
  util.raiseNotDefined()

def breadthFirstSearch(problem):
  "Search the shallowest nodes in the search tree first. [p 81]"
  "*** YOUR CODE HERE ***"
  """
  Search the deepest nodes in the search tree first [p 85].
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm [Fig. 3.7].
  
  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:
  """
  start_state=problem.getStartState()
  path=[]
  path1=[]
  successors=problem.getSuccessors(problem.getStartState())
  dfs=util.Queue()
  instack=[]
  visited=[]
  parent=[]
  instack.append(start_state)
  temp=successors
  dfs.push(start_state)
  print start_state
  for i in successors:
  	dfs.push(i)
  	instack.append(i[0])
  	print "init",i
  flag2=0
  k=0
  flag=0
  k=0
  while flag==0:
  	temp=dfs.pop()
  	print "temp",temp
  	if(temp!=start_state):
  		next_state=temp[0]
  		next_action=temp[1]	
  		if next_state not in visited:
  			visited.append(next_state)
  			current_state=next_state
  			if problem.isGoalState(current_state):
  				flag=1
  			else:
  				successor=problem.getSuccessors(current_state)
  				for i in successor:
  					if i[0] not in instack:
  							dfs.push(i)
  							instack.append(i[0])
  	 						parent.append(temp)
  	 						parent.append(i)
  	 						print i
  	 				if problem.isGoalState(i[0]):
  	 						parent.append(temp)
  	 						parent.append(i)
  	 						flag=1
  	 						break
  	 						
  		
  k=0
  parent2=[]
  for i in parent:
  	parent2.append(i)
  parent.reverse()
  i=parent[0]
  while i not in successors:
  	k=len(parent)
  	a=parent2.index(parent[1])
  	b=k-a-1
  	while b>0:
  		parent2.pop()
  		b=b-1
  	p=k
  	while p:
  		parent.pop()
		p=p-1
	for x in parent2:
		parent.append(x)
  	parent.reverse()
  	path.append(i[1])
  	i=parent[0]
  		
  "*** YOUR CODE HERE ***"
  path.append(parent[0][1])
  path.reverse()
  return path
  util.raiseNotDefined()

  util.raiseNotDefined()
      
def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  "*** YOUR CODE HERE ***"
  start_state=problem.getStartState()
  path=[]
  path1=[]
  successors=problem.getSuccessors(problem.getStartState())
  dfs=util.PriorityQueue()
  instack=[]
  visited=[]
  parent=[]
  instack.append(start_state)
  temp=successors
  dfs.push(start_state,0)
  print start_state
  for i in reversed(successors):
  	dfs.push(i,i[2])
  	print"init",i
  	instack.append(i[0])
  flag2=0
  k=0
  flag=0
  k=1
  while flag==0:
  	temp=dfs.pop()
  	print "temp",temp
  	if(temp!=start_state):
  		next_state=temp[0]
  		next_action=temp[1]	
  		if next_state not in visited:
  			visited.append(next_state)
  			current_state=next_state
  			if problem.isGoalState(current_state):
  				flag=1
  			else:
  				successor=problem.getSuccessors(current_state)
  				for i in successor:
  					if i[0] not in instack:
  							if temp[2]==i[2]:
  								dfs.push(i,i[2]+k)
  							else:
  								dfs.push(i,i[2])
  							instack.append(i[0])
  	 						parent.append(temp)
  	 						parent.append(i)
  	 						print i
  	 				if problem.isGoalState(i[0]):
  	 						parent.append(temp)
  	 						parent.append(i)
  	 						flag=1
  	 						break
  	 			k=k+1
  		
  k=0
  parent2=[]
  for i in parent:
  	parent2.append(i)
  parent.reverse()
  i=parent[0]
  while i not in successors:
  	k=len(parent)
  	a=parent2.index(parent[1])
  	b=k-a-1
  	while b>0:
  		parent2.pop()
  		b=b-1
  	p=k
  	while p:
  		parent.pop()
		p=p-1
	for x in parent2:
		parent.append(x)
  	parent.reverse()
  	path.append(i[1])
  	i=parent[0]
  		
  "*** YOUR CODE HERE ***"
  path.append(parent[0][1])
  path.reverse()
  return path
  util.raiseNotDefined()

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  "*** YOUR CODE HERE ***"
  start_state=problem.getStartState()
  path=[]
  path1=[]
  successors=problem.getSuccessors(problem.getStartState())
  dfs=util.PriorityQueue()
  instack=[]
  visited=[]
  parent=[]
  instack.append(start_state)
  temp=successors
  f=[]
  dfs.push(start_state,0)
  print start_state
  for i in reversed(successors):
  	a=cornersHeuristic(i[0],problem)
  	a=a+i[2]
  	f.append(i[0])
  	f.append(i[2])
  	dfs.push(i,a)
  	print"init",i,f
  	instack.append(i[0])
  flag2=0
  k=0
  flag=0
  k=1
  while flag==0:
  	temp=dfs.pop()
  	print "temp",temp
  	if(temp!=start_state):
  		next_state=temp[0]
  		next_action=temp[1]	
  		if next_state not in visited:
  			visited.append(next_state)
  			current_state=next_state
  			if problem.isGoalState(current_state):
  				flag=1
  			else:
  				successor=problem.getSuccessors(current_state)
  				for i in successor:
  					if i[0] not in instack:
  							a=cornersHeuristic(i[0],problem)				
  							s=f.index(temp[0])
  							c=a+i[2]+f[s+1] 
  							print"manhattan ",temp[0],s,a,c
  							f.append(i[0])
  							f.append(c)
  							print f
  							dfs.push(i,c)
  							instack.append(i[0])
  	 						parent.append(temp)
  	 						parent.append(i)
  	 						print i
  	 				if problem.isGoalState(i[0]):
  	 						parent.append(temp)
  	 						parent.append(i)
  	 						flag=1
  	 						break
  	 			k=k+1
  		
  k=0
  parent2=[]
  for i in parent:
  	parent2.append(i)
  parent.reverse()
  i=parent[0]
  while i not in successors:
  	k=len(parent)
  	a=parent2.index(parent[1])
  	b=k-a-1
  	while b>0:
  		parent2.pop()
  		b=b-1
  	p=k
  	while p:
  		parent.pop()
		p=p-1
	for x in parent2:
		parent.append(x)
  	parent.reverse()
  	path.append(i[1])
  	i=parent[0]
  path.append(parent[0][1])
  path.reverse()
  return path
  util.raiseNotDefined()
  util.raiseNotDefined()
    
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch