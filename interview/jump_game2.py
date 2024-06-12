#
# Title: jump_game2.py
# Description: from borat
# 
#
class Solution:

    def level(self, obstacles: list[int], instructions: str) -> bool:
        """returns true if end can be reached"""

        game = [" "] * 10

        for temp in obstacles:
            game[temp] = 'X'
    
        game_ndx = 0
        last_move = ""
        
        buffer = list(instructions)
        for temp in buffer:
            #print(f"{temp} {game_ndx}")

            if temp == 'R':
                last_move = temp
                game_ndx += 1
            elif temp == 'L':
                last_move = temp
                game_ndx -= 1
            elif temp == 'J':
                if last_move == 'R':
                    game_ndx += 2
                else:
                    game_ndx -= 2
            else:
                print(f"unknown command {temp}")
            
            if game_ndx < 0:
                return False
            
            if game_ndx > len(game)-1:
                return True
            
            if game[game_ndx] == 'X':
                return False

        # print(f"exit {game_ndx}")

        return False

if __name__ == '__main__':
    print("main")

    obstacles_1 = [4, 6]
    obstacles_2 = [9, 4, 2]
    obstacles_3 = []

    instructions_1 = "RRRJJRRR"
    instructions_2 = "RRRLJ"
    instructions_3 = "RRRJJRRRL"
    instructions_4 = "RRRLRJJRRR"
    instructions_5 = "RRRRRRRRRR"
    instructions_6 = "RRJJJJ"
    instructions_7 = "RLRRRJJRRLLJJJLRRRJJRRR"
    instructions_8 = "RRRJJRLJJJRRR"
    instructions_9 = "R"
    instructions_10 = "RJJJJR"
    instructions_11 = "RJJRRRRR"
    instructions_12 = "RJJRRRJ"

    solution = Solution()
    print(solution.level(obstacles_1, instructions_1)) # True
    print(solution.level(obstacles_1, instructions_2)) # False
    print(solution.level(obstacles_1, instructions_3)) # True
    print(solution.level(obstacles_1, instructions_4)) # True
    print(solution.level(obstacles_1, instructions_5)) # False
    print(solution.level(obstacles_1, instructions_6)) # False
    print(solution.level(obstacles_1, instructions_7)) # True
    print(solution.level(obstacles_1, instructions_8)) # False
    print(solution.level(obstacles_1, instructions_9)) # False
    print(solution.level(obstacles_1, instructions_10)) # True
    print(solution.level(obstacles_2, instructions_11)) # False
    print(solution.level(obstacles_2, instructions_12)) # True
    print(solution.level(obstacles_3, instructions_9))  # False

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
