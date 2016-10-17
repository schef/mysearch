import omdb

class serie:
    def __init__(self, stash):
        self.poster = stash['poster']
        self.type = stash['type']
        self.writer = stash['writer']
        self.runtime = stash['runtime']
        self.awards = stash['awards']
        self.response = stash['response']
        self.released = stash['released']
        self.metascore = stash['metascore']
        self.year = stash['year']
        self.title = stash['title']
        self.actors = stash['actors']
        self.imdb_rating = stash['imdb_rating']
        self.language = stash['language']
        self.director = stash['director']
        self.rated = stash['rated']
        self.imdb_id = stash['imdb_id']
        self.genre = stash['genre']
        self.imdb_votes = stash['imdb_votes']
        self.country = stash['country']
        self.plot = stash['plot']

series = []

def addSerieToList(title):
    newSerie = serie(omdb.title(title))
    series.append(newSerie)

def addSeriesToList(titles):
    for title in titles:
        newSerie = serie(omdb.title(title))
        series.append(newSerie)

def generateHtmlFromSeries(series):
    html = ""
    for i in series:
      html += generateHtml(i)
    return(html)

def generateHtml(serie):
    endline = "\r\n"
    string = ""
    string += "<h1>" + serie.title + "</h1>" + endline
    string += "<img src=\"" + serie.poster + "\" width=\"200\">" + endline
    string += "<h3>" + serie.genre + "</h3>" + endline
    string += "<pre>" + serie.plot + "</pre>" + endline
    return(string)

def saveHtmlToDisk(html):
    filename = "test.html"
    with open(filename, 'w') as out:
    	out.write(html	)
