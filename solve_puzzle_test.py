import unittest
from solve_puzzle import bfs, make_tuple, print_path

class TestSolvePuzzle(unittest.TestCase):
    #test case 1
    def test_hmw_ex1(self):
        start = make_tuple([[0,1,3],
                           [4,2,5],
                           [7,8,6]])
        sol = bfs(start)
        correct_path = [start,
                        make_tuple([[1,0,3],
                                   [4,2,5],
                                   [7,8,6]]),
                        make_tuple([[1,2,3],
                                   [4,0,5],
                                   [7,8,6]]),
                        make_tuple([[1,2,3],
                                   [4,5,0],
                                   [7,8,6]]),
                        make_tuple([[1,2,3],
                                   [4,5,6],
                                   [7,8,0]])]

        self.assertEqual(sol, correct_path)
        #print_path(sol)

    #test case 2
    def test_hmw_ex2(self):
        start = make_tuple([[8,7,6],
                           [5,4,3],
                           [2,1,0]])
        sol = bfs(start)
        correct_path = [start,
                        make_tuple([[8,7,6],
                                   [5,4,0],
                                   [2,1,3]]),
                        make_tuple([[8,7,6],
                                   [5,0,4],
                                   [2,1,3]]),
                        make_tuple([[8,7,6],
                                   [0,5,4],
                                   [2,1,3]]),
                        make_tuple([[8,7,6],
                                   [2,5,4],
                                   [0,1,3]]),
                        make_tuple([[8,7,6],
                                   [2,5,4],
                                   [1,0,3]])]
        self.assertEqual(len(sol), 31)

        #print_path(sol)

    #test case 3
    def test_ex3(self):
        start = make_tuple([[1,2,3],
                           [0,8,5],
                           [4,7,6]])
        sol = bfs(start)
        correct_path = [start,
                        make_tuple([[1,2,3],
                                   [4,8,5],
                                   [0,7,6]]),
                        make_tuple([[1,2,3],
                                   [4,8,5],
                                   [7,0,6]]),
                        make_tuple([[1,2,3],
                                   [4,0,5],
                                   [7,8,6]]),
                        make_tuple([[1,2,3],
                                   [4,5,0],
                                   [7,8,6]]),
                        make_tuple([[1,2,3],
                                   [4,5,6],
                                   [7,8,0]])]

        self.assertEqual(sol, correct_path)
        #print_path(sol)

    #test case 4
    def test_ex4(self):
        start = make_tuple([[1,5,2],
                           [4,0,3],
                           [7,8,6]])
        sol = bfs(start)

        correct_path = [start,
                        make_tuple([[1,0,2],
                                   [4,5,3],
                                   [7,8,6]]),
                        make_tuple([[1,2,0],
                                   [4,5,3],
                                   [7,8,6]]),
                        make_tuple([[1,2,3],
                                   [4,5,0],
                                   [7,8,6]]),
                        make_tuple([[1,2,3],
                                   [4,5,6],
                                   [7,8,0]])]

        self.assertEqual(sol, correct_path)
        print_path(sol)

    #test case 5
    def test_already_solved(self):
        start = make_tuple([[1,2,3],
                           [4,5,6],
                           [7,8,0]])
        sol = bfs(start)
        correct_path = [start]
        self.assertEqual(sol, correct_path)
        #print_path(sol)

    #test case 6
    def test_invalid_input(self):
        start = make_tuple([[1,2,2],
                           [4,5,6],
                           [7,8,0]])
        sol = bfs(start)
        self.assertEqual(sol, None)

    
if __name__ == '__main__':
    unittest.main()
