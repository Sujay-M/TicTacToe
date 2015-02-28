import sys
class Game:
	GameState = [[0,0,0],[0,0,0],[0,0,0]]
	m = 3

	def __init__(self,pname):
		self.pname = pname
		self.state = [[0,0,0],[0,0,0],[0,0,0]]

	def getState(self):
		return self.state

	def makeMove(self,r,c):
		if Game.GameState[r][c]!=0:
			return -1
		else:
			Game.GameState[r][c] = 1
			self.state[r][c] = 1
			return self.winCheck()
	
	def winCheck(self):
		for i in range(self.m):
			if sum(self.state[i])==3:
				return 2
			elif sum([row[i] for row in self.state])==3:
				return 2
		diag1 = 0
		diag2 = 0
		for i in range(self.m):
			diag1 = diag1+self.state[i][i]
			diag2 = diag2+self.state[i][self.m-i-1]
		if diag1==3 or diag2==3:
			return 2
		if sum([sum(row) for row in Game.GameState])==9:
			return 3
		return 0

def main(pname1='sujay',pname2='tars'):
	player = [Game(pname1),Game(pname2)]
	toggle = 0
	while True:
		print 'player ',player[toggle].pname
		[r,c] = raw_input('enter your move r c').split()
		r = int(r)
		c = int(c)
		status = player[toggle].makeMove(r,c)
		while status==-1:
			print 'wrong move'
			[r,c] = raw_input('enter your move r c').split()
			r = int(r)
			c = int(c)
			status = player[toggle].makeMove(r,c)
		print 'status :',status
		if status==2:
			print 'player ',player[toggle].pname,' is the winner'
			break
		elif status == 3:
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