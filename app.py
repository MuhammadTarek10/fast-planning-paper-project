import random
import fastpathplanning as fpp
import numpy as np
import matplotlib.pyplot as plt


class Tester:
    def __init__(self) -> None:
        self.size = 10
        self.start = 0
        self.maxLimit = 10
        self.L = np.array(
            [
                [6.25, 4],
                [5.5, 2.5],
                [1, 4],
                [0.25, 0.1],
                [2.25, 0.75],
                [0.5, -0.25],
                [2, 0],
                [4.75, -0.25],
                [0, 5.2],
                [1.5, 3.5],
            ]
        )
        self.U = np.array(
            [
                [7.25, 5.75],
                [7.5, 4.75],
                [6, 5],
                [7, 3],
                [3, 2.5],
                [1.5, 4.5],
                [6.25, 1],
                [6, 3.75],
                [7, 6],
                [2.5, 4.5],
            ]
        )
        self.safeSet = fpp.SafeSet(self.L, self.U, verbose=True)

    def base(self):  # upper bounds of the safe boxes
        pInit = np.array([1, 0.25])  # initial point
        pTerminal = np.array([0.5, 5.5])  # terminal point
        T = 10  # traversal time
        alpha = [2000, 12, 100, 21, 23, 0.4]
        p = fpp.plan(self.safeSet, pInit, pTerminal, T, alpha)
        self.safeSet.plot2d(alpha=0.5)
        p.plot2d()
        plt.title(
            f"Start: {[round(i, 2) for i in pInit]} | End: {[round(i, 2) for i in pTerminal]})"
        )

    def setRandomPoints(self):
        self.pInit = np.array(
            [
                random.uniform(self.start, self.maxLimit),
                random.uniform(self.start, self.maxLimit),
            ]
        )
        self.pTerminal = np.array(
            [
                random.uniform(self.start, self.maxLimit),
                random.uniform(self.start, self.maxLimit),
            ]
        )
        self.alpha = [random.uniform(0, 1) for _ in range(self.size // 2)]
        self.sampleTime = random.randint(5, 20)

    def plan(self):
        self.p = fpp.plan(
            self.safeSet,
            self.pInit,
            self.pTerminal,
            self.sampleTime,
            self.alpha,
        )

    def plot(self):
        plt.figure()
        self.safeSet.plot2d(alpha=0.5)
        self.p.plot2d(alpha=0.5)
        plt.title(
            f"Start: {[round(i, 2) for i in self.pInit]} | End: {[round(i, 2) for i in self.pTerminal]})"
        )

    def run(self):
        self.plan()
        self.plot()


if __name__ == "__main__":
    counter = 10
    baseTester = Tester()
    baseTester.base()
    i = 1
    while i < counter:
        try:
            baseTester.setRandomPoints()
            baseTester.run()
            i += 1
        except Exception as e:
            print(e)
            continue
    plt.show()
