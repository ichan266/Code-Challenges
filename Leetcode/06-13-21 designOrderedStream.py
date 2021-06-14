# Leetcode # 1656
# Easy
# https://leetcode.com/problems/design-an-ordered-stream/


# @ This one has a test that didn't pass when I was trying to submit it. But when I use that particular test case that failed in console, it passed... I do not know why
cache = set()


class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.ls = [0] * self.n

    def insert(self, idKey: int, value: str) -> List[str]:
        self.ls[idKey-1] = value
        result = []

        for i in range(len(self.ls)):
            if self.ls[i] == 0:
                return result
            if i in cache:
                continue
            elif self.ls[i] != 0 and i not in cache:
                result.append(self.ls[i])
                cache.add(i)

        return result


class OrderedStream1:

    def __init__(self, n: int):
        self.n = n
        self.ls = [0] * (n+1)
        self.index = 0

    def __repr__(self):
        return f"<ls: {self.ls}; index: {self.index}>"

    def insert(self, idKey: int, value: str) -> List[str]:
        self.ls[idKey-1] = value
        result = []

        while self.ls[self.index]:
            result.append(self.ls[self.index])
            self.index += 1

        print(self)

        return result


# ["OrderedStream","insert","insert","insert","insert","insert"]
# [[5],[3,"ccccc"],[1,"aaaaa"],[2,"bbbbb"],[5,"eeeee"],[4,"ddddd"]]

# <ls: [0, 0, 'ccccc', 0, 0, 0]; index: 0>
# <ls: ['aaaaa', 0, 'ccccc', 0, 0, 0]; index: 1>
# <ls: ['aaaaa', 'bbbbb', 'ccccc', 0, 0, 0]; index: 3>
# <ls: ['aaaaa', 'bbbbb', 'ccccc', 0, 'eeeee', 0]; index: 3>
# <ls: ['aaaaa', 'bbbbb', 'ccccc', 'ddddd', 'eeeee', 0]; index: 5>
