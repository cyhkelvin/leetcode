class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # 1067ms 54.7MB
        vertices = set()
        for edge in edges:
            vertices.add(edge[1])
        return list(set(range(n))-vertices)
        
        # 1016ms 54.8MB
        # vertices = set(range(n))
        # for edge in edges:
        #     vertices.discard(edge[1])
        # print(time()-t1)
        # return list(vertices)


    # TLE
    # def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
    #     self.leaves = [[set(), False] for i in range(n)]
    #     vertices = set(range(n))
    #     for edge in edges:
    #         self.leaves[edge[0]][0].add(edge[1])
    #         vertices.discard(edge[1])
    #     print(len(vertices))
    #     for vertex in vertices:
    #         if not self.leaves[vertex][1]:
    #             self.traverse(vertex)
    #             vertices = vertices-self.leaves[vertex][0]
    #     return list(vertices)
        
    # def traverse(self, index):
    #     if self.leaves[index][1]:
    #         return self.leaves[index][0]
    #     elif len(self.leaves[index][0]) == 0:
    #         self.leaves[index][1] = True
    #         return self.leaves[index][0]
    #     else:
    #         leaf_vertex = list(self.leaves[index][0])
    #         for vertex in leaf_vertex:
    #             tmp = self.traverse(vertex)
    #             self.leaves[index][0] = self.leaves[index][0].union(tmp)
    #         self.leaves[index][1] = True
    #         return self.leaves[index][0]
