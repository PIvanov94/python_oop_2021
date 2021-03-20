def solution():
    def integers():
        number = 1
        while True:
            yield number
            number += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        halves_nums = []
        for i in seq:
            if len(halves_nums) == n:
                return halves_nums
            halves_nums.append(i)

    return (take, halves, integers)
