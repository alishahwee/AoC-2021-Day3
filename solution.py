def part_one(nums: list[str]) -> int:
    gamma_rate = ""
    epsilon_rate = ""
    num_length = len(nums[0])

    for i in range(num_length):
        zeros_count = 0
        ones_count = 0
        for num in nums:
            if num[i] == "0":
                zeros_count += 1
            elif num[i] == "1":
                ones_count += 1
        if zeros_count > ones_count:
            gamma_rate += "0"
            epsilon_rate += "1"
        else:
            gamma_rate += "1"
            epsilon_rate += "0"

    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def part_two(nums: list[str]) -> int:
    pass
