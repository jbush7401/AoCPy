from helper import read_input_file

WINNERS = {1:3, 2:1, 3:2}

class Solution:
    def __init__(self):
        self.data = read_input_file("2022/day2/input.txt")

    def solve(self):
        print("Part 1:" + str(self.part1()))
        print("Part 1:" + str(self.part2()))

    def part1(self):
        score = 0
        for line in self.data:
            score += is_winner(line[0], line[2])
        return score

    def part2(self):
        score = 0
        for line in self.data:
            if line[2] == 'X':
                score += ord(line[0]) - 87
            if line[2] == 'Y':
                score += 3 + ord(line[0]) - 87
            if line[2] == 'Z':
                score += 6 + ord(line[0]) - 87
        return score

def is_winner(opp, player):
    opp_num = ord(opp) - 64
    play_num = ord(player) - 87
    if play_num == opp_num:
        return 3 + play_num
    return 6 + play_num if WINNERS[play_num] == opp_num else play_num

if __name__ == "__main__":
    Solution().solve()