import timeit
from unittest import TestCase
from minichallenge_hashmap.minichallenge import Solution, SolutionFast


class TestSolution(TestCase):
    def test_correct_solution(self):
        solution = Solution()
        nums = [2, 7, 11, 15]
        target = 9
        assert (solution.twoSum(nums, target) == [0, 1])
        nums = [3, 2, 4]
        target = 6
        assert (solution.twoSum(nums, target) == [1, 2])
        nums = [3, 3]
        target = 6
        assert (solution.twoSum(nums, target) == [0, 1])

    def test_running_time(self):
        iterations = 1
        running_time = timeit.timeit(lambda: self.large_input(Solution()), number=iterations)
        print(f"\nExecution of twoSum took {running_time} seconds for {iterations} iterations")

    def large_input(self, solution):
        nums = [i for i in range(1, 10001)]
        target = 19999
        assert (solution.twoSum(nums, target) == [9998, 9999])

    # def test_correct_solution_fast(self):
    #     solution = SolutionFast()
    #     nums = [2, 7, 11, 15]
    #     target = 9
    #     assert(solution.twoSum(nums, target) == [0, 1])
    #     nums = [3, 2, 4]
    #     target = 6
    #     assert(solution.twoSum(nums, target) == [1, 2])
    #     nums = [3, 3]
    #     target = 6
    #     assert(solution.twoSum(nums, target) == [0, 1])
    #
    # def test_running_time_fast(self):
    #     iterations=10
    #     running_time = timeit.timeit(lambda: self.large_input(SolutionFast()), number=iterations)
    #     print(f"\nExecution of fast twoSum took {running_time} seconds for {iterations} iterations")