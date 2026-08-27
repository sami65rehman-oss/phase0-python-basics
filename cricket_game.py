def my_function(user):
    player = user.lower()
    if "6" in player:
       
        print("Player hit the six")
    elif "4" in player:
        
        print("Player hit the four")
    elif "1" in player:
        
        print("Player get 1 run")
    elif "2" in player:
       
        print("Player get 2 runs")
    elif "w" in player:
        print("Player out and gone to pavillion")
    else:
        print("Player leave the ball")
print("_"*100)
print("Welcome to the cricket stadium \n (Control is 6 for six 4 for four w for wicket 1 for one run and 2 four 2 rurns )")
print("_"*100)
while True:
    user_player = input("Enter the number: ")
    if user_player.lower() in ["quit" , "exit" , "stop"]:
        print("Game is Close")
        print("Thank you very much")
        break
    my_function(user_player)
