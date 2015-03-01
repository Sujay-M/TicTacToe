import sys
import os
import numpy as np
class Game:
	GameState = np.array([[0,0,0],[0,0,0],[0,0,0]])

	def __init__(self,pname,ptype):
		self.pname = pname
		self.ptype = ptype
		self.state = np.array([[0,0,0],[0,0,0],[0,0,0]])

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

def main(pname1='CPU1',pname2='CPU2'):
	player = [Game(pname1,pname1=='CPU1'),Game(pname2,pname2=='CPU2')]
	coorMap = {}
	coorMapRev = {}
	for i in range(3):
		for j in range(3):
			coor = 3*i+j+1
			coorMap[coor] = (i,j)
			coorMapRev[(i,j)] = coor
	turn = 0
	turnNo = 0
	GamePlay = np.zeros((9,9),np.uint8)
	display(player[0].state,player[1].state)
	
	while True:

		if player[turn].ptype==False:
			print 'player ',player[turn].pname
			coor = int(raw_input('enter your move coordinate from 1-9\n'))
			[r,c] = coorMap[coor]
			status = player[turn].makeMove(r,c)
			while status==-1:
				print 'wrong move'
				coor = int(raw_input('enter your move coordinate from 1-9\n'))
				[r,c] = coorMap[coor]
				status = player[turn].makeMove(r,c)
		else:
			coor = np.random.randint(1,10)
			[r,c] = coorMap[coor]
			status = player[turn].makeMove(r,c)
			while status==-1:
				coor = np.random.randint(1,10)
				[r,c] = coorMap[coor]
				status = player[turn].makeMove(r,c)

		GamePlay[turnNo:,coor-1] = turn+1
		display(player[0].state,player[1].state)

		if status==1:
			print player[turn].pname,' is the winner'
			break
		elif status == 2:
			print 'Game Draw'
			break
		
		turn = turn^1
		turnNo = turnNo+1

	return status,GamePlay
	
if __name__=='__main__':
	if len(sys.argv)==1:
		[status,GamePlay] = main()
	elif len(sys.argv)==2:
		[status,GamePlay] = main(sys.argv[1])
	elif len(sys.argv)==3:
		[status,GamePlay] = main(sys.argv[1],sys.argv[2])
	