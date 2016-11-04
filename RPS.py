import random
import RPSPlayer

def main():
    rps_list = []
    rps_list.append("rock")
    rps_list.append("paper")
    rps_list.append("scissors")

    comp = RPSPlayer.RPSPlayer("Computer")

    player_name = input("Enter your name \n")
    player = RPSPlayer.RPSPlayer(player_name)
    playing = True
    y_n = ""
    
    def game():
        player_c = player.player_turn()
        comp_c = comp.comp_turn()
        if (player_c == 0 and comp_c == 2) or (player_c == 1 and comp_c == 0) or (player_c == 2 and comp_c == 1):
            player.win()
            print(player.name, " chose ", rps_list[player.get_choice()], " and ", comp.name, " chose ", rps_list[comp.get_choice()])
            print(player.name, " WINS")
        elif (comp_c == 0 and player_c == 2) or (comp_c == 1 and player_c ==0) or (comp_c == 2 and player_c == 1):
            comp.win()
            print(comp.name, " chose ", rps_list[comp.get_choice()], " and ", player.name, " chose ", rps_list[player.get_choice()])
            print(comp.name, " WINS")
        else:
            print(player.name, " chose ", rps_list[player.get_choice()], " and ", comp.name, " chose ", rps_list[comp.get_choice()])
            print("Tie game")
        print("The score is ", player.name, ": ", player.get_wins(), comp.name, ": ", comp.get_wins())
        print("\n")
            
    while(playing):
        y_n = input("Would you like to play? (Y) or (N) ").upper()
        if y_n == "Y":
            game()
        elif y_n == "N":
            playing = False

    print("\n")       
    player.toString()
    comp.toString()
    
    
    
    
    

if __name__ == '__main__':
    main()
