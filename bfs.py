class queue:
    def __init__(self):
        self.items = []

    def enque(self, item):
        self.items.append(item)
    
    def dequeue(self):
        return self.items.pop(0)

    def is_empty(self):
        if self.items == [0]:
            return True
        return False
if __name__ = "main":
    graph = {
        'A' : ['B','C'],
        'B' : ['D', 'E'],
        'C' : ['F'],
        'D' : [],
        'E' : ['F'],
        'F' : []
    }
visited = []
queue = []

def bfs (visited, queue, node):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end =" ")

        for neighbour in graph[s]:
            visited.append(neighbour)
            queue.append(neighbour)

bfs(visited,graph, 'A')

