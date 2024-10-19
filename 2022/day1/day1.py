from helper import read_input_file

class Solution:

    def __init__(self):
        self.data = read_input_file("2022/day1/input.txt")
        self.TOTALS = []

    def solve(self):

        part1_result = self.part1(self.data)
        part2_result = self.part2()

        print(f"Part 1:  {part1_result}")
        print(f"Part 2:  {part2_result}")

    def part1(self, data):
        current = 0
        for line in data:
            if line == "":
                self.TOTALS.append(current)
                current = 0
            else:
                current +=  int(line)

        return max(self.TOTALS)

    def part2(self):
        return sum(sorted(self.TOTALS)[-3:])

if __name__ == "__main__":
    Solution().solve()
