class Vertex:

	def __init__(self, id):
		self.id = id
		self.connected = [ ]
		self.visited = False
		self.color = None

class MyGraph:

	def __init__(self, filename):
		file = open(filename, "r")
		lines = [line.strip('\n') for line in file]
		file.close()
		self.numVertices = int(lines[0])
		verticesList = [ Vertex(i) for i in range(1, (self.numVertices+1))]
		self.numEdges = lines[1]
		for i in range(2,len(lines)):
			vertices = lines[i].split()
			vertex1 = int(vertices[0])
			vertex2 = int(vertices[1])
			verticesList[vertex1 -1].connected.append(vertex2)
			verticesList[vertex2 -1].connected.append(vertex1)
		self.verticesList = verticesList
				
	def conn_components(self):
		graphs =[ ]
		for i in self.verticesList:
			newgraph = [ ]
			if i.visited == False:
				newgraph.append(i.id)
				i.visited=True
				self.connected_to(i,newgraph)
				newgraph = sorted(newgraph)
				graphs.append(newgraph)
		return graphs
				
	def connected_to(self, vertex, newgraph):
		for i in vertex.connected:
			if self.verticesList[i-1].visited == False:
				newgraph.append(i)
				self.verticesList[i-1].visited = True
				self.connected_to(self.verticesList[i-1],newgraph)

	def bicolor(self):
		for i in self.verticesList:
			if i.color == None:
				i.color = 'red'
				for j in i.connected:
					self.verticesList[j-1].color = 'black'
					colorable = self.check_color(self.verticesList[j-1])
					if colorable == False:
						return False
		return True
	
	def check_color(self,vertex):
		for i in vertex.connected:
			if self.verticesList[i-1].color == None:
				if vertex.color == 'black':
					self.verticesList[i-1].color = 'red'
				else:
					self.verticesList[i-1].color = 'black'
				if self.check_color(self.verticesList[i-1]) == False:
					return False
			elif self.verticesList[i-1].color == vertex.color:
				return False
		return True
