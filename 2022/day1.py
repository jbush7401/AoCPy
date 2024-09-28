TOTALS = []
class Solution:

    def solve(self):
        part1_result = 0
        part2_result = 0

        with open("input.txt", 'r') as file:
            data = [line.strip() for line in file]

            part1_result = part1(data)
            part2_result = part2(data)

        print(f"Part 1:  {part1_result}")
        print(f"Part 2:  {part2_result}")

    def part1(data):
        current = 0
        for line in data:
            if line == "":
                TOTALS.append(current)
                current = 0
            else:
                current +=  int(line)

        return max(TOTALS)

    def part2(data):
        return sum(sorted(TOTALS)[-3:])


    if __name__ == "__main__":
        solve()