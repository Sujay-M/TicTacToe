import numpy as np
class Game:
	count = 0
	
	def __init__(self,pname,ptype):
		if Game.count==0:
			Game.GameState = np.array([[0,0,0],[0,0,0],[0,0,0]])
		self.pname = pname
		self.ptype = ptype
		self.state = np.array([[0,0,0],[0,0,0],[0,0,0]])
		Game.count = Game.count+1
	def makeMove(self,r,c):
		if Game.GameState.item(r,c)==1:
			return -1
		else:
			Game.GameState.itemset(r,c,1)
			self.state.itemset(r,c,1)
			return self.winCheck()
	
	def winCheck(self):
		if 3 in np.sum(self.state,axis=0) or 3 in np.sum(self.state,axis=1):
			return 1
		if np.sum(np.diag(np.fliplr(self.state)))==3 or np.sum(np.diag(self.state))==3:
			return 1
		if np.sum(Game.GameState)==9:
			return 2
		return 0
	def __del__(self):
		Game.count = Game.count-1
		if Game.count==0:
			Game.GameState = None