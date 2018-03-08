import random
class TestGenerator(object):
	"""Class when called will generate a list of array
	of desired data type and length."""
	n=0
	lower=0
	higher=0
	def __init__(self, n,lower,higher):
		super(TestGenerator, self).__init__()
		self.n = n
		self.lower=lower
		self.higher=higher

	def  classTest(self):
		print self.n
		print self.lower
		print self.higher

	def integerArray(self):
		intList=[]
		n = self.n
		lower = self.lower
		higher = self.higher
		for i in range(n):
			intList.append(random.randint(lower,higher))
		return intList

	def stringGenerator(self,len):
		stringList = []
		element=""
		reserve = 'abcdefghijklmnopqrstuvwxyz'
		n = self.n
		lower = self.lower
		higher = self.higher
		for i in range(n):
			length = random.randint(1,len)
			element=""
			for j in range(length):
				element = element + random.choice(reserve)
			stringList.append(element)
		return stringList

	def charGenerator(self):
		charList = []
		reserve = 'abcdefghijklmnopqrstuvwxyz'
		n = self.n
		lower = self.lower
		higher = self.higher
		for i in range(n):
			charList.append(random.choice(reserve))
		return charList
class SingleGenerator(object):
	"""This class generates the given number or character or string randomly"""
	lower=0
	higher =0
	
	def __init__(self,lower,higher):
		super(SingleGenerator, self).__init__()
		self.lower = lower
		self.higher = higher
	
	def integer(self):
		genint = random.randint(lower,higher)
		return genint

	def character(self):
		reserve = 'abcdefghijklmnopqrstuvwxyz'
		genchar = random.choice(reserve)
		return genchar
	
	def string(self):
		reserve = 'abcdefghijklmnopqrstuvwxyz'
		length = random.randint(lower,higher)
		element=""
		for i in range(length):
			element += random.choice(reserve)
		return element

	def specialchar(self,reserve):
		length = random.randint(lower,higher)
		element=""
		for i in range(length):
			element+=random.choice(reserve)
		return element

class GraphGenerator(object):
	"""This class will generate a random connected graph"""
	nodes=0
	edges=0
	def __init__(self, nodes,edges):
		super(GraphGenerator, self).__init__()
		self.nodes = nodes
		self.edges = edges

	def root (self,edgeSet,a):
		while edgeSet[a]!=a:
			a = edgeSet[a]
		return a

	def find(self,edgeSet,a,b):
		if self.root(edgeSet,a) == self.root(edgeSet,b):
			return True
		return False
	def union(self,edgeSet,a,b):
		if a<b:
			edgeSet[a]=edgeSet[b]
		else:
			edgeSet[b]=edgeSet[a]
	
	def graphGen(self):
		graphset = [i for i in range(nodes+1)]
		a = 1
		b = 2
		mapset = {}
		mapset[(1,2)]=1;
		#for i in range(edges):
	def treeGen(self):
		edgeSet = [i for i in range(self.nodes+1)]
		treeset = set()
		for i in range(self.edges):
			a = random.randint(1,self.nodes)
			b = random.randint(1,self.nodes)
			while a==b and self.find(edgeSet,a,b):
				b = random.randint(1,self.nodes)
			self.union(edgeSet,a,b)
			treeset.add((a,b))
		return treeset




random.seed()
n = 0     #number or the number of elements in the list required 
lower = 0  #lower bound on the element of the list
higher = 0 #upper bound on the element of the list

#obj = TestGenerator(10**5,)
#print obj.treeGen()
lis = ["1000000000 500000000 1000000000000000000\n"]*(10**5)
file = open('testfile.txt','w')
file.write("100000\n")
for i in lis:
	file.write(i)

