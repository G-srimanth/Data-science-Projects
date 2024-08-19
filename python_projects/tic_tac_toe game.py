import sys
import os
import time
from random import choice
def begin():
	while True:
		players = int(input(' select no.of players(1/2) :  '))
		if players==2:
			print()
			two_players()
			break
		elif players ==1:
			computer_vs_player()
			break
		else:
			print(' please enter valid no. of players only 1 or 2  ')

#2p players
def two_players():
	print()
	print(" * "*5,'  player_1 vs player_2  '," * "*5)
	while True:
		player_1=input('player one ...please  Choose X / O: ').upper()
		if player_1 in ['X','O']:
			player_2='O' if player_1=='X' else 'X'
			break
		print(' * '*5,'choose only X or Y',' * '*5)
	print()
	print()
	print(' * '*5,f'  1p: {player_1}   2p: {player_2}',' * '*5)
	player_moves(player_1,player_2)
	
#computer_vs_1p
def computer_vs_player():
	print(" * "*5,'computer vs player..',' * '*5)
	while True:
		player_1=input('player one ...please  Choose X / O: ').upper()
		if player_1 in ['X','O']:
			cpu='O' if player_1=='X' else 'X'
			break
		print(' * '*5,'choose only X or Y',' * '*5)
	print()
	print()
	print(' * '*5,f'  1p: {player_1}   2p: {cpu}',' * '*5)
	computer_moves(player_1,cpu)
	
def row_col(position):
	col =2 if position % 3 ==0 else position%3-1
	row = position //3 -1 if position%3==0 else position//3
	return row,col

#computet moves
def computer_moves(player_1,cpu):
	count=0
	moves =[1,2,3,4,5,6,7,8,9]
	XOX_moves=[["" for j in range(3)] for _ in range(3)]
	while count<9:
		XOX_board(XOX_moves)
		count,XOX_moves,moves=player_1_move(player_1,count,XOX_moves,moves)
		if count >2:
			if winning(XOX_moves):
				os.system("clear")
				print(' * '*5,f' player_1 won({player_1}) ',' * '*5)
				break
		if count!=9:
			time.sleep(2)
		if count <9:
			cpu_move = choice(moves)
			row,col=row_col(cpu_move)
			XOX_moves[row][col]+=cpu
			moves.pop(moves.index(cpu_move))
			os.system('clear')
			count+=1
		if count >2:
			if winning(XOX_moves):
				os.system('clear')
				print(' * '*5,f'cpu won{cpu}',' * '*5)
				break
		if count==9:
				print(" * "*5,'match tie'," * "*5)
			
#player moves
def player_moves(player_1,player_2):
	count=0
	XOX_moves=[["" for j in range(3)] for _ in range(3)]
	while count<9:
		XOX_board(XOX_moves)
		count,XOX_moves=player_1_move(player_1,count,XOX_moves)
		if count >2:
			if winning(XOX_moves):
				os.system("clear")
				print(' * '*5,f' player_1 won({player_1}) ',' * '*5)
				break			
		if count<9:
			while True:
				print(' * '*5,'player two Choose the position 1-9 ',' * '*5)
				position = int(input())
				while True:
					if position in [i for i in range(1,10)]:
						row,col=row_col(position)
						break
					print(' * '*3,'please enter valid position',' * '*3)
				
				if len(XOX_moves[row][col])==0:
					XOX_moves[row][col]+=player_2
					os.system('clear')
					count+=1
					break
				print('position already filled')
				print('Enter valid position')
			if count >2:
				if winning(XOX_moves):
					print(' * '*5,f'player_2 won({player_2}) ',' * '*5)
					break
		if count==9:
			print(" * "*5,'match tie'," * "*5)
#player_1 move
def player_1_move(player_1,count,XOX_moves,moves=[]):
		moves1=len(moves)
		while True:
			while True:
				print(' * '*3,' player one Choose postion [1-9] ',' * '*3)
				position = int(input())
				if position in [i for i in range(1,10)]:	
					row,col=row_col(position)
					break
				print('... Pls Enter a valid postion..')
			if len(XOX_moves[row][col])==0:
				XOX_moves[row][col]+=player_1
				os.system('clear')
				if len(moves)!=0:
					moves=list(set(moves)-set([position]))
				XOX_board(XOX_moves)
				count+=1
				break			
			print('position already filled')
			print('Enter valid position')
		if moves1!=0:		
			return count,XOX_moves,moves
		else:
			return count,XOX_moves
			
#xox_board	
def XOX_board(board):
	print()
	for row in board:
		for col in row:
			print(col,end=" | ")
		print()
		print("-"*10)
	print()
	
#winning declare	
def winning(xox):
	row = []
	dia=[]
	col=[]
	str_diaL=''
	str_diaR=''
	for i in range(3):
		str_row=''
		str_col=''
		for j in range(3):
			str_col+=xox[j][i]
			str_row+=xox[i][j]
			if i==j:
				str_diaL+=xox[i][j]
			if i+j==2:
				str_diaR+=xox[i][j]
		row.append(str_row)
		col.append(str_col)
	dia.append(str_diaL)
	dia.append(str_diaR)
	if 'XXX' in row or 'OOO' in row:
		return True
	elif 'XXX' in col or 'OOO' in col:
		return True
	elif 'XXX' in dia or 'OOO' in dia:
		return True
	else:
		return None
#tic tac toe game	
def tic_tac_toe():
	print(' * '*5,'Let\'s begin tic tac toe',' * '*5)
	while True:
		begin()
		play_again = input('Do you need to play again Y/N: ').upper()
		if play_again == 'Y':
			os.system('clear')
			tic_tac_toe()
		else:
			os.system('clear')
			print(' * '*5,"  Remeber me! you got bored  ",' * '*5)
			sys.exit()

tic_tac_toe()
	