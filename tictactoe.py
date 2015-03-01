import sys
import os
import numpy as np
class Game:
	GameState = np.array([[0,0,0],[0,0,0],[0,0,0]])

	def __init__(self,pname):
		self.pname = pname
		self.state = np.array([[0,0,0],[0,0,0],[0,0,0]])

	def getState(self):
		return self.state

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
def display(state1,state2):
	if os.name=='nt':
			os.system('cls')
	elif os.name=='posix':
		os.system('clear')
	displayMat = np.chararray((3, 3))
	displayMat[:] = '-'
	displayMat[state1==1] = 'X'
	displayMat[state2==1] = 'O'
	print displayMat
def main(pname1='sujay',pname2='tars'):
	player = [Game(pname1),Game(pname2)]
	coorMap = {}
	for i in range(3):
		for j in range(3):
			coorMap[3*i+j+1] = (i,j)
	toggle = 0
	while True:
		display(player[0].getState(),player[1].getState())
		print 'player ',player[toggle].pname
		coor = int(raw_input('enter your move coordinate from 1-9\n'))
		[r,c] = coorMap[coor]
		status = player[toggle].makeMove(r,c)
		while status==-1:
			print 'wrong move'
			coor = int(raw_input('enter your move coordinate from 1-9\n'))
			[r,c] = coorMap[coor]
			status = player[toggle].makeMove(r,c)
		if status==1:
			print 'player ',player[toggle].pname,' is the winner'
			break
		elif status == 2:
			print 'Game Draw'
			break
		toggle = toggle^1
		
if __name__=='__main__':
	if len(sys.argv)==1:
		main()
	elif len(sys.argv)==2:
		main(sys.argv[1])
	elif len(sys.argv)==3:
		main(sys.argv[1],sys.argv[2])