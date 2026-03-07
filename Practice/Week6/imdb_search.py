class IMDBTracker:
    def __init__(self):
        self.db = {}
        with open('imdb.txt', 'r') as file:
            for movie in file:
                movie = movie.split('/')
                movie_title = movie[0]
                for i in range(1, len(movie)):
                    movie[i] = movie[i].replace(',', '')
                self.db[movie[0]] = movie[1:]

    def list_performers(self, movie):
        list_of_performers = self.db.get(movie)
        print(list_of_performers)
    
    def list_performers_ordered(self, movie):
        list_of_performers = self.db.get(movie)
        if list_of_performers is None:
            return None
        list_of_performers = sorted(list_of_performers, key=lambda x: x[0])
        return list_of_performers
    def check_actor(self, movie, actor):
        if self.db.get(movie) is None:
            return None
        performers = self.db.get(movie)
        return actor in performers
    def number_of_performances(self, actor):
        count = 0
        for movie, performers in self.db.items():
            if actor in performers:
                count +=1
        return count
 
    def actor_performances(self, actor):
        performances = []
        for movie, performers in self.db.items():
            if actor in performers:
                performances.append(movie)
        return performances


tracker = IMDBTracker()
print(tracker.number_of_performances("Reeves Keanu"))
print(tracker.actor_performances("Reeves Keanu"))   
            

