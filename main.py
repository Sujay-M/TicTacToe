import os
import sys
import numpy as np
from tictactoe import Game
import pickle

#learning part
def getKey(l):
	pl1 = l[0:][::2]
	pl1.sort()
	pl2 = l[1:][::2]
	pl2.sort()
	key = tuple(pl1)+tuple(pl2)
	return key

def stateVal(l):
	global win
	for a in win:
		if all(value in l[0:][::2] for value in a ):
			return 1.0
		elif all(value in l[1:][::2] for value in a ):
			return -1.0
		else:
			val = 0.5
	return val
def predictMove(l):
	global states,learn
	cur = getKey(l)
	if states.has_key(cur)==False:
		states[cur] = .5
	costs = {}
	winCheck = [l+[x] for x in range(1,10) if x not in l]
	loseCheck = [l+[0,x]for x in range(1,10) if x not in l]
	if any(stateVal(ch)==-1.0 for ch in loseCheck):
		lose = [l[-1] for l in loseCheck if stateVal(l)==-1]
		for i in winCheck:
			key = getKey(i)
			if states.has_key(key)==False:
				if i[-1] in lose:
					states[key] = 1.0
				elif stateVal(i) == 1.0:
					states[key] = 1.0
				else:
					states[key] = -1.0
			costs[i[-1]] = states[key]
	else:
		for i in winCheck:
			key = getKey(i)
			if states.has_key(key)==False:
				states[key] = stateVal(i)
			costs[i[-1]] = states[key]
	maxi = 0
	prob = np.random.randint(1,10)
	move = None
	if prob<7:
		for i in costs:
			if costs[i]>maxi:
				maxi = costs[i]
				move = i
		if move==None:
			sel = [x for x in range(1,10) if x not in l]
			prob = np.random.randint(0,len(sel))
			move = sel[prob]
	else:
		l1 = [i for i in costs]
		prob = np.random.randint(0,len(l1))
		move = l1[prob]
	if learn==True:
		states[cur] = states[cur]+alpha*(costs[move]-states[cur])
	return move

def learner(num):
	for i in range(num):
		main()
	with open('init.pk', 'wb') as f:
	 	pickle.dump(states, f)


#NON LEARNING PART

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

def main(pname2='CPU1',pname1='CPU2'):
	player = [Game(pname1,pname1=='CPU2'),Game(pname2,pname2=='CPU1')]
	coorMap = {}
	coorMapRev = {}
	for i in range(3):
		for j in range(3):
			coor = 3*i+j+1
			coorMap[coor] = (i,j)
			coorMapRev[(i,j)] = coor
	turn = 0
	turnNo = 0
	state = []
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
			if player[turn].pname == 'CPU1':
				coor = np.random.randint(1,10)
				[r,c] = coorMap[coor]
				status = player[turn].makeMove(r,c)
				while status==-1:
					coor = np.random.randint(1,10)
					[r,c] = coorMap[coor]
					status = player[turn].makeMove(r,c)
			else:
				coor = predictMove(state)
			[r,c] = coorMap[coor]
			status = player[turn].makeMove(r,c)
		display(player[0].state,player[1].state)	
		if status==1:
			print player[turn].pname,' is the winner'
			status = turn^1 #if player 1 wins turn is 0 and we get the status as 1 otherwise 0
			break
		elif status == 2:
			print 'Game Draw'
			status = 0
			break
		state.append(coor)
		turn = turn^1
		turnNo = turnNo+1
	del player
	return status

if __name__=='__main__':
	try:
		with open('init.pk', 'rb') as f:
	 		states = pickle.load(f)
	except:
		states = {}
		states[()] = .5
		with open('init.pk', 'wb') as f:
	 		pickle.dump(states, f)
	learn = False
	alpha = .9
	win = ((1,2,3),(4,5,6),(7,8,9),(1,5,9),(3,5,7),(1,4,7),(2,5,8),(3,6,9))
	if sys.argv[1] == 'learn':
		learn = True
		learner(1000)
		
	elif len(sys.argv)==1:
		status = main()
	elif len(sys.argv)==2:
		status = main(sys.argv[1])
	elif len(sys.argv)==3 and sys.argv[2]=='-l':
		learn = True
		status = main(sys.argv[1])
		
	elif len(sys.argv)==3:
		status = main(sys.argv[1],sys.argv[2])