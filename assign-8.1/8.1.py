import random

def computer_num_generator():
    com_num=random.sample("0123456789",4)
    com_num="".join(com_num)
    # print(com_num)
    return(com_num)

def player_num_generator():
    while(True):
        try:
            global player_num
            z=player_num=input("Enter Your Number:")
            z=int(z)
            if(len(player_num)!=4):
                print("Enter a 4 digit number")
                continue
        except ValueError:
            print("The input you entered is not a number")
        else:
            same_num_count=0
            for i in range(0,4):
                same_num_count+=player_num.count(player_num[i])
            if(same_num_count!=4):
                print("Enter a number with different digits")
                continue
            else:
                return

def value_comparison(com_gen,player_gen):
    com_gen=str(com_gen)
    player_gen=str(player_gen)
    for i in range(0,4):
        for j in range(0,4):
            if(i==j)and(com_gen[i]==player_gen[j]):
                global bull_count
                bull_count+=1
            elif(i!=j)and(com_gen[i]==player_gen[j]):
                global cow_count
                cow_count+=1
            else:
                pass


print(" <------WELCOME TO COWS AND BULLS GAME ------>")


player_num=0
user_choice=True
while(user_choice):
    cow_count=0
    bull_count=0
    game_num=computer_num_generator()
    score_counter=0
    while(True):
        player_num_generator()
        score_counter=score_counter+1
        value_comparison(game_num,player_num)
        if(bull_count==4):
            print("\n !!!!    YOU WON    !!!!\n")
            print(" YOU HAVE COMPLETED THE GAME IN ",str(score_counter)," CHANCES \n")
            print(" DO YOU WANT TO PLAY AGAIN   \n")
            print(" ENTER \" YES \" TO PLAY AGAIN \n")
            print(" ENTER ANYTHING ELSE TO EXIT \n")
            choice=input("ENTER YOUR CHOICE:  ")
            if(choice.lower()=="yes"):
                user_choice=True
            else:
                user_choice=False
            break
        else:
            print("cow_count",cow_count)
            print("bull_count",bull_count)
            cow_count=0
            bull_count=0