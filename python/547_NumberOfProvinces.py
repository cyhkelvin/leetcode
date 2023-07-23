class Solution:
    # sol2: dfs
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        rows = len(isConnected)
        visited = set()

        def dfs(row):
            visited.add(row)
            for col in range(rows):
                if isConnected[row][col] == 1 and col not in visited:
                    # visited.add(col)
                    dfs(col)
        count = 0
        for i in range(rows):
            if i not in visited:
                dfs(i)
                count += 1
        return count

    # sol1: loop all array
    # runtime 18.45%(243ms) memory:63.00%(16.97mb)
    # def findCircleNum(self, isConnected: List[List[int]]) -> int:
    #     provinces = list()
    #     num = len(isConnected)
    #     for city_connect in isConnected:
    #         connected = set([i for i in range(num) if city_connect[i]])
    #         appeared = -1
    #         for index in range(len(provinces)-1, -1, -1):
    #             for city in connected:
    #                 if city in provinces[index]:
    #                     if appeared == -1:
    #                         provinces[index] = provinces[index].union(connected)
    #                     else:
    #                         provinces[index] = provinces[index].union(provinces[appeared])
    #                         del provinces[appeared]
    #                     appeared = index
    #                     break
    #         if appeared == -1:
    #             provinces.append(connected)
    #     return len(provinces)
