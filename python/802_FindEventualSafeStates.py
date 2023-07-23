class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        seen = set()
        unsafe = set()
        safe = set()

        def dfs(node):
            seen.add(node)
            if node in safe or node in unsafe:
                return
            for gotonode in graph[node]:
                if gotonode in unsafe:
                    unsafe.add(node)
                    if node in seen:
                        seen.remove(node)
                    return
                elif gotonode in safe:
                    continue
                elif gotonode in seen:
                    unsafe.add(gotonode)
                    seen.remove(gotonode)
                    unsafe.add(node)
                    if node in seen:
                        seen.remove(node)
                    return
                else:
                    dfs(gotonode)
                    if gotonode in unsafe:
                        unsafe.add(node)
                        if node in seen:
                            seen.remove(node)
                        return
            safe.add(node)
            if node in seen:
                seen.remove(node)

        for node in range(len(graph)):
            if node in safe or node in unsafe:
                continue
            else:
                dfs(node)
        return sorted(safe)

# Output Limit Exceeded: print out too long information