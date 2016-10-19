import omdb
import sys

class serie:
    def __init__(self, stash):
        self.poster = stash.get('poster', "")
        self.type = stash.get('type', "")
        self.writer = stash.get('writer', "")
        self.runtime = stash.get('runtime', "")
        self.awards = stash.get('awards', "")
        self.response = stash.get('response', "")
        self.released = stash.get('released', "")
        self.metascore = stash.get('metascore', "")
        self.year = stash.get('year', "")
        self.title = stash.get('title', "")
        self.actors = stash.get('actors', "")
        self.imdb_rating = stash.get('imdb_rating', "")
        self.language = stash.get('language', "")
        self.director = stash.get('director', "")
        self.rated = stash.get('rated', "")
        self.imdb_id = stash.get('imdb_id', "")
        self.genre = stash.get('genre', "")
        self.imdb_votes = stash.get('imdb_votes', "")
        self.country = stash.get('country', "")
        self.plot = stash.get('plot', "")

series = []
seriesList = sys.argv[1]
genreWanted = sys.argv[2]

def addSerieToList(title):
    newSerie = serie(omdb.title(title))
    series.append(newSerie)

def addSeriesToList(titles):
    for title in titles:
        newSerie = serie(omdb.title(title))
        if newSerie != {}:
            series.append(newSerie)

def generateHtmlFromSeries(series):
    html = ""
    for i in series:
        if checkGenre(genreWanted, i) or genreWanted == "":
          html += generateHtml(i)
    return(html)

def checkGenre(wanted, serie):
    #Comedy, Drama, Sci-Fi, Adventure, Fantasy, Romance
    genre = serie.genre.split(", ")
    if wanted in genre:
        return(True)
    else:
        return(False)

def generateHtml(serie):
    endline = "\r\n"
    imdbLink = "http://www.imdb.com/title/" + serie.imdb_id
    string = ""
    string += "<h1>" + serie.title + " (" + serie.year.replace("–", "-") + ")</h1>" + endline
    string += "<a target=\"_blank\" href=\"" + imdbLink + "\"><img src=\"" + serie.poster + "\" width=\"200\"></a>" + endline
    string += "<h3>" + serie.genre + "</h3>" + endline
    string += "<h3>" + serie.imdb_rating + "</h3>" + endline
    string += "<pre>" + serie.plot + "</pre>" + endline
    return(string)

def saveHtmlToDisk(html):
    filename = "test.html"
    with open(filename, 'w') as out:
    	out.write(html	)

if __name__ == "__main__":
    addSeriesToList(seriesList.split(","))
    html = generateHtmlFromSeries(series)
    saveHtmlToDisk(html)
