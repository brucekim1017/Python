# * Graph Exercise:
#   - Download the map of the towns in Virginia
# https://www.cs.utexas.edu/users/mitra/csSpring2021/cs313/notes/Virginia.pdf
#   - Download the spreadsheet and create the adjacency matrix
# https://www.cs.utexas.edu/users/mitra/csSpring2021/cs313/notes/Virginia_Towns.xlsx
# https://www.cs.utexas.edu/users/mitra/csSpring2021/cs313/notes/Virginia_Towns.pdf
#   - Create the adjacency list for the towns in Virginia

# * Graph Traversals
    #  Depth First Search (DFS)
    #  start at any vertax and go as far as you can go (using backtrack so that you can come up with every vertax in your graph)
    #   0. Create a Stack.
    #   1. Select a starting vertex. Make it the current vertex.
    #      Mark it visited. Push it on the stack.
    #   2. If possible, visit an adjacent unvisited vertex from the
    #      current vertex in order. Make it the current vertez.
    #      Mark it visited, and push it on the stack.
    #   3. If you cannot follow step 2, then if possible pop a vertex
    #      from the stack. Make it the current vertex.
    #   4. Repeat steps 2 and 3 until the stack is empty.

    #  Breadth First Search (BFS)
    #  start at a vertax and visit all neighbors of that vertax, and visit neighbors of the neighbors... and so forth...
    #   0. Create a Queue.
    #   1. Select a starting vertex. Make it the current vertex.
    #      Mark it visited.
    #   2. Visit an adjacent unvisited vertex (if there is one) in 
    #      order from the current vertex. Mark it visited and insert 
    #      it into the queue.
    #   3. If you cannot carry out step 2 because there are no more
    #      unvisited vertices, remove a vertex from the queue (if
    #      possible) and make it the current vertex.
    #   4. Repeat steps 2 and 3 until the queue is empty.

# Describing the Graph : Undirected / Unweighted


import sys

class Stack (object):
    def __init__ (self):
        self.stack= []
    # add an itemto the top of the stack
    # top could be beginning or end of the list depending on how you design it.
    def push (self, item):
        self.stack.append(item)
    # remove an item from the top of the stack
    def pop (self):
        return self.stack.pop()
    # it is error-prone because you cannot pop the empty stack.
    # check the item on top of the stack
    def peek (self):
        return self.stack[-1]
    # check if the stack is empty
    def is_empty (self):
        return (len(self.stack) == 0)
    # return the number of elements in the stack
    def size (self):
        return len(self.stack)

class Queue (object):
    def __init__ (self):
        self.queue = []

    # add an item to the end of the Queue
    def enqueue (self, item):
        self.queue.append(item)
    # remove an item from the beginning of the Queue
    def dequeue(self):
        return self.queue.pop(0)
    # check if the queue is empty
    def is_empty (self):
        return len(self.queue) == 0
    # return the size of the queue
    def size(self):
        return (len(self.queue))
    def peek (self):
        return self.queue[0]

class Vertex (object):
    def __init__ (self, label):
        self.label = label
        self.visited = False
    
    # determine if a vertex was visited 
    def was_visited(self):
        return self.visited

    # determine the label of the vertex
    def get_label (self):
        return self.label
    
    # string representation of the vertex
    def __str__ (self):
        return str(self.label)

# two different ways to represent a graph : Adjacency list & Adjacency matrix

class Graph (object):
    def __init__(self):
        self.Vertices = []      #list of Vertex objects
        self.adjMat = []        #adjacency matrix (2d)

    # check if a vertex is already in the graph (sequential search)
    def has_vertex (self, label):
        nVert = len (self.Vertices)
        for i in range (nVert):
            if (label == (self.Vertices[i]).get_label()):
                return True
        return False
    
    # given a label, get the index of a vertex
    def get_index (self, label):
        nVert = len(self.Vertices)
        for i in range (nVert):
            if (label == (self.Vertices[i]).get_label()):
                return i
        return -1

    # add a Vertex with a given label to the graph
    def add_vertex (self, label):
        self.Vertices.append(Vertex (label))
        
        # add a new column in the adjacency matrix
        nVert = len(self.Vertices)
        for i in range (nVert - 1):
            (self.adjMat[i]).append(0)
        
        # add a new row for the new Vertex
        new_row = []
        for i in range (nVert):
            new_row.append(0)
        self.adjMat.append (new_row)

    # add weighted directed edge to the graph
    def add_directed_edge (self, start, finish, weight = 1):
        self.adjMat[start][finish] = weight
    
    # add weighted undirected edge to the graph
    def add_undirected_edge (self, start, finish, weight = 1):
        self.adjMat[start][finish] = weight
        self.adjMat[finish][start] = weight
    
    # return an unvisited vertex and adjacent to vertex v (index)
    def get_adj_unvisited_vertex (self, v):
        nVert = len(self.Vertices)
        for i in range (nVert):
            # check if there is an edge
            if (self.adjMat[v][i] > 0) and (not(self.Vertices[i]).was_visited()):
                return i
        return -1

    # do the dept first search in a graph
    # v is the index of the starting vertex
    def dfs (self, v):
        # create the Stack object
        theStack = Stack()

        # mark the vertex v as visited and push it on the stack
        (self.Vertices[v]).visited = True
        print(self.Vertices[v])
        theStack.push(v)

        # visit all vertices according to depth
        while (not theStack.is_empty()):
            # get an adjacent unvisited vertex
            u = self.get_adj_unvisited_vertex(theStack.peek())
            if (u == -1):
                u = theStack.pop()
            else:
                (self.Vertices[u]).visited = True
                print(self.Vertices[u])
                theStack.push(u)
        
        # the stack is empty, let us reset the flags
        nVert = len(self.Vertices)
        for i in range (nVert):
            self.Vertices[i].visited = False

# do a breadth first search in a graph starting at vertex v (index)
    def bfs (self, v):
        # create the queue
        theQueue = Queue()

        # Select a starting vertex. Mark it visited.
        self.Vertices[v].visited = True
        print(self.Vertices[v])
        theQueue.enqueue(v)
        
        # visit all vertices according to breath
        while not theQueue.is_empty():
            # get an adjacent unvisited vertex
            u = self.get_adj_unvisited_vertex(theQueue.peek())
            if u == -1:
                u = theQueue.dequeue()
            else:
                self.Vertices[u].visited  = True
                print(self.Vertices[u])
                theQueue.enqueue(u)

        # the stack is empty, let us rest the flags
        nVert = len (self.Vertices)
        for i in range (nVert):
            (self.Vertices[i]).visited = False

def main():
    # create the Graph object
    cities = Graph()

    # read the number of vertices
    line = (sys.stdin.readline()).strip()
    num_vertices = int(line)

    # add the vertices to the graph
    for i in range(num_vertices):
        city = (sys.stdin.readline()).strip()
        print(city)
        cities.add_vertex(city)

    # read the number of edges
    line = (sys.stdin.readline()).strip()
    num_edges = int(line)

    # read the edges and add them to the adjacency matrix
    for i in range(num_edges):
        line = (sys.stdin.readline()).strip()
        print(line)
        edge = line.split()
        start = int(edge[0])
        finish = int(edge[1])
        weight = int(edge[2])

        cities.add_directed_edge(start, finish, weight)

    # print the adjacency matrix
    print("\nAdjacency Matrix")
    for i in range (num_vertices):
        for j in range(num_vertices):
            print(cities.adjMat[i][j], end = " ")
        print()
    print()

    # read the starting vertex for dfs and bfs
    start_vertex = (sys.stdin.readline()).strip()
    print(start_vertex)

    # get the index of the starting vertex
    start_index = cities.get_index(start_vertex)
    print(start_vertex)

    # do the dept first search
    print("\nDepth First Search from " + start_vertex)
    cities.dfs(start_index)
    print()

    # do the breath first search
    print("\nBreath First Search from " + start_vertex)
    cities.bfs(start_index)
    print()

main()