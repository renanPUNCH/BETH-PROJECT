class League:


	def __init__(self, id, slug, name, region, image, priority):

		self.id = id
		self.slug = slug
		self.name = name
		self.region = region
		self.image = image
		self.priority = priority

	
	def getLeagueId(self):

		return self.id
	
	def getLeagueName(self):

		return self.name

	def getLeagueImage(self):

		return self.image	
			 