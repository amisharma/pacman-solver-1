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
  				if successor:
  						print"pushed",temp
  						instack.append(temp[0])
  						print"instack",instack
  						dfs.push(temp)
  				for i in successor:
  					if i[0] not in instack:
  						print"pushed2",i
  						dfs.push(i)
  						instack.append(i[0])
  	 					print"instack2",instack
  				if not successor:
  					path.pop()
  					print path
  		else:
  			path.pop()
  			print path
  		
  print visited
  "*** YOUR CODE HERE ***"
  print"path",path
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
  util.raiseNotDefined()
    
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch