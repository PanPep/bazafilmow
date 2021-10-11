import random
class Film:
    def __init__(self, title, production, category, views = 0):
        self.title = title
        self.production = production
        self.category = category
        self.views = views 

    def __str__(self):
        return f"{self.title}({self.production}) "


    
    def __repr__(self):
        return f"  Film(tytuł: {self.title}, produkcja: {self.production}, gatunek: {self.category}, wyświetlenia: {self.views}  "

    def play(self, value=1):
        self.views += value


class Serial(Film):
    def __init__(self, episode, season, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.episode = episode
        self.season = season

    def __str__(self):
        return f"{self.title} S{self.season}E{self.episode}"

    def __repr__(self):
        return f"  Serial(tytuł: {self.title}, produkcja: {self.production}, gatunek: {self.category}, wyświetlenia: {self.views}, sezon: {self.season}, odcinek: {self.episode}   "


forrestGump=Film(title='Forrest Gump', production='1994', category='Komedia/Dramat', views=2000)
interstellar=Film(title='Interstellar', production='2014', category='Sci-Fi',views=1230)
incepcja=Film(title='Incepcja', production='2010', category='Thriller/Sci-Fi', views=1100)
chappie=Film(title='Chappie', production='2015', category='Akcja/Sci-Fi', views=450)
zielonaMila=Film(title='Zielona Mila', production='2000', category='Dramat', views=3000)

breakingBad=Serial(title='Breaking Bad', production='2008', category='Dramat/Kryminał', views=1900,episode='10', season='02')
mrRobot=Serial(title='Mr.Robot', production='2015', category='Dramat/Thriller', views=1300, episode='08', season='01')
domzPapieru=Serial(title='Dom z papieru', production='2021', category='Akcja', views=200 , episode='05', season='05')


print('\n')

library=[forrestGump,interstellar,incepcja,chappie,zielonaMila,mrRobot,domzPapieru,breakingBad]
#print(library)
print("Biblioteka:")

for product in library:
    print(product)

def get_movies():
    for product in library:
        if type(product) == Film:
            print(product.title)
        
def get_series():
    for product in library:
        if type(product) == Serial:
            print(product.title)
        elif type(product)==Film:
            pass
        



def search():
    prod = input("Wpisz tytuł produkcji: ")
    for product in library:
        if prod.lower() in product.title.lower() : 
            print(product.title)
       


def top_titles():
    
    for product in library:
        by_views = sorted(library, key=lambda library: library.views)
    print(by_views[::-1])

        
print('\n')
print("Top tytuły:")    
top_titles()
print('\n')
def generate_views():
    prod = random.choice(library)
    prod.views + random.randint(1, 100)
    print(prod)

        
generate_views()
search()
print('\n')
print("Filmy:")
get_movies()
print('\n')
print("Seriale:")
get_series()