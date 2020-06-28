class Sorter():

	""" Sorter class is a collection of the most popular 
        sorting algorithms that you should know

	"""
	def __init__(self, array):
		self.array = array

	def insertionSort(self):
		"""Function to sort an array using insertion sort
		algorithm.
		
		Args: 
			None
		
		Returns: 
			list: sorted array 

		"""
		for i in range(1, len(self.array)):
			value = self.array[i]
			j = i

			while j > 0 and self.array[j - 1] > value:
				self.array[j] = self.array[j - 1]
				j = j - 1

			self.array[j] = value

		return self.array
