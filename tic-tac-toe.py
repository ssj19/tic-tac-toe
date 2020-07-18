

board={
   "T1":" ","T2":" ","T3":" ",
   "M1":" ","M2":" ","M3":" ",
   "D1":" ","D2":" ","D3":" "
  }


player1=str(input("Enter player1 :"))
print()
player2=str(input("Enter player2 :"))
print(" ")
print("*************************************")
print()
print("TIC-TAC-TOE Welcomes "+player1+" and "+player2)
print(" ")
print("*************************************")
print(" ")

print('T1'+"  |  "+'T2'+"  |  "+'T3')
print("____+______+____")
print('M1'+"  |  "+'M2'+"  |  "+'M3')
print("____+______+____")
print('D1'+"  |  "+'D2'+"  |  "+'D3')

print()
print("**************come on lets play***********************")
print()

total_moves=0

print(player1+" starts first with code x ")
print()
print(player1+" starts second with code O ")
print()
print("######################################################")
print()
def check():
	if (board["D1"]=="x" and board["M2"]=="x" and board["T3"]=="x") or (board["D3"]=="x" and board["M2"]=="x" and board["T1"]=="x") or (board["T1"]=="x" and board["M1"]=="x" and board["D1"]=="x") or (board["T2"]=="x" and board["M2"]=="x" and board["D2"]=="x") or (board["D3"]=="x" and board["M3"]=="x" and board["T3"]=="x") or (board["D1"]=="x" and board["D2"]=="x" and board["D3"]=="x") or (board["M1"]=="x" and board["M2"]=="x" and board["M3"]=="x") or (board["T1"]=="x" and board["T2"]=="x" and board["T3"]=="x"):
		print()
		print("~~~~~~~~~~~~~~~~~~~~~WINNER~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
		print(player1+" won!!")
		print()
		print()
		return 1
	elif (board["D1"]=="O" and board["M2"]=="O" and board["T3"]=="O") or (board["D3"]=="O" and board["M2"]=="O" and board["T1"]=="O") or (board["T1"]=="O" and board["M1"]=="O" and board["D1"]=="O") or (board["T2"]=="O" and board["M2"]=="O" and board["D2"]=="O") or (board["D3"]=="O" and board["M3"]=="O" and board["T3"]=="O") or (board["D1"]=="O" and board["D2"]=="O" and board["D3"]=="O") or (board["M1"]=="O" and board["M2"]=="O" and board["M3"]=="O") or (board["T1"]=="O" and board["T2"]=="O" and board["T3"]=="O"):
		print()
		print("~~~~~~~~~~~~~~~~~~~~~WINNER~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
		print(player2+" won!!")
		print()
		print()
		return 1
	return 0

p=0


while total_moves<=9 and p==0:
	print(board['T1']+"  |  "+board['T2']+"  |  "+board['T3'])
	print("___+_____+___")
	print(board['M1']+"  |  "+board['M2']+"  |  "+board['M3'])
	print("___+_____+___")
	print(board['D1']+"  |  "+board['D2']+"  |  "+board['D3'])
	p=check()
	if p==1:
		break
	else:
		pos=str(input("Enter position : "))
		if(board[pos]==" " and (total_moves==0 or total_moves%2==0)):
			board[pos]="x"
			total_moves+=1
			
			
			
		elif(board[pos]==" " and (total_moves==1 or total_moves%2!=0)):
			board[pos]="O"
			total_moves+=1
			
			
			

		else:
			print("Please Enter Empty Cell")

	print()
	print("####################################################")
	print()

	
