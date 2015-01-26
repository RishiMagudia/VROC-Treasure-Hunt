import heapq
import pygame


class node(object):
    def __init__(self, x, y, traversable):
        """
        Initialize new node
        """
        self.traversable = traversable
        self.x = x
        self.y = y
        self.parent = None
        self.g = 0
        self.h = 0
        self.f = 0

class AStar(object):
    def __init__(self):
        self.opened = []
        heapq.heapify(self.opened)
        self.closed = set()
        self.nodes = []
        self.grid_height = 18 
        self.grid_width = 32
        self.path = []

    def init_grid(self,startx,starty,endx,endy,land):

        self.opened = []
        heapq.heapify(self.opened)
        self.closed = set()
        self.nodes = []
        self.path = []

        walls = land
        for x in range(self.grid_width):
            for y in range(self.grid_height):
                if (x, y) in walls:
                    traversable = False
                else:
                    traversable = True
                self.nodes.append(node(x, y, traversable))
                
        self.start = self.get_node(startx,starty)
        self.end = self.get_node(endx,endy)

    def getPath(self):
        return self.path


    def get_heuristic(self, node):
        """
        distance between
        this node and the ending node multiply by 10.
        """
        return 10 * (abs(node.x - self.end.x) + abs(node.y - self.end.y))

    def get_node(self, x, y):
        """
        Returns a node from the nodes list
        """
        return self.nodes[x * self.grid_height + y]

    def get_adjacent_nodes(self, node):
        """
        Returns adjacent nodes to a node. Clockwise starting
        from the one on the right.
        """
        nodes = []
        if node.x < self.grid_width-1:
            nodes.append(self.get_node(node.x+1, node.y))
        if node.y > 0:
            nodes.append(self.get_node(node.x, node.y-1))
        if node.x > 0:
            nodes.append(self.get_node(node.x-1, node.y))
        if node.y < self.grid_height-1:
            nodes.append(self.get_node(node.x, node.y+1))
        return nodes

    def display_path(self):
        node = self.end
        while node.parent is not self.start:
            node = node.parent
            self.traverse_path(node.x,node.y)


    def traverse_path(self,x,y):
        self.path.append(x)
        self.path.append(y)
        #print x,y

    def update_node(self, adj, node):
        """
        Update adjacent node
        """
        adj.g = node.g + 10
        adj.h = self.get_heuristic(adj)
        adj.parent = node
        adj.f = adj.h + adj.g

    def algorithm(self):
        # add starting node to open heap queue
        heapq.heappush(self.opened, (self.start.f, self.start))
        while len(self.opened):
            # pop node from heap queue
            f, node = heapq.heappop(self.opened)
            # add node to closed list so we don't algorithm it twice
            self.closed.add(node)
            # if ending node, display found path
            if node is self.end:
                self.display_path()
                break
            # get adjacent nodes for node
            adj_nodes = self.get_adjacent_nodes(node)
            for adj_node in adj_nodes:
                if adj_node.traversable and adj_node not in self.closed:
                    if (adj_node.f, adj_node) in self.opened:
                        # if adj node in open list, check if current path is
                        # better than the one previously found
                        # for this adj node.
                        if adj_node.g > node.g + 10:
                            self.update_node(adj_node, node)
                    else:
                        self.update_node(adj_node, node)
                        # add adj node to open list
                        heapq.heappush(self.opened, (adj_node.f, adj_node))
