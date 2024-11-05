from tests_12_1 import Runner
import unittest


class RunnerTest(unittest.TestCase):
    """
        test_walk - метод, в котором создаётся объект класса Runner с произвольным именем.
        Далее вызовите метод walk у этого объекта 10 раз.
        После чего методом assertEqual сравните distance этого объекта со значением 50.
        """

    def test_walk(self):
        runner = Runner("Usain Bolt")
        for _ in range(1, 11):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    """
        test_run - метод, в котором создаётся объект класса Runner с произвольным именем.
        Далее вызовите метод run у этого объекта 10 раз.
        После чего методом assertEqual сравните distance этого объекта со значением 100.
        """

    def test_run(self):
        runner = Runner("Korobov")
        for _ in range(1, 11):
            runner.run()
        self.assertEqual(runner.distance, 100)

        """test_challenge - метод в котором создаются 2 объекта класса Runner с произвольными именами.
        Далее 10 раз у объектов вызываются методы run и walk соответственно.
        Т.к. дистанции должны быть разными, используйте метод assertNotEqual, чтобы убедится в неравенстве результатов"""

    def test_challenge(self):
        runner1 = Runner("Korobov")
        runner2 = Runner("Usain Bolt")
        for _ in range(1, 11):
            runner1.walk()
            runner2.run()
        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == '__main__':
    unittest.main()
