import imdb
from GUI import window, values

ia = imdb.IMDb()

title = 0
plot = 0
year = 0
director = 0
cast = 0
runtime = 0
finish = 1

def run_code():
    global name, movie_title, movie, title, plot, year, director, cast, runtime
    while True:
        event, value = window.read()
        if event == 'SEARCH':
            print(values[0])
            name = str(values[0])

            print('Please wait while your results load...')
            search = ia.search_movie(values[0])

            id = search[0].movieID

            code = id

            movie = ia.get_movie(code)

            movie_title = movie['title']

            print('-----------------------------')
            checkboxes1()

        elif event == 'EXIT':
            break

all = title + plot + year + director + cast + runtime

def checkboxes1():
    global movie_title, movie, title, plot, year, director, cast, runtime, finish, value
    if values['-Title-'] is True and title == 0:
        title +=1
        print(movie_title)
        checkboxes1()
    elif values['-Plot-'] is True and plot == 0:
        plot += 1
        text = str(movie['plot'])
        split_string = text.split(":", 1)
        substring = split_string[0]
        print(substring[2:])
        checkboxes1()
    elif values['-Year-'] is True and year == 0:
        year += 1
        year = movie['year']
        print(year)
        checkboxes1()
    elif values['-Director-'] is True and director == 0:
        director += 1
        director = str(movie['director'])[32:-3]
        print(director)
        checkboxes1()
    elif values['-Cast-'] is True and cast == 0:
        cast += 1
        cast1 = movie['cast'][0]
        cast2 = movie['cast'][1]
        cast3 = movie['cast'][2]
        print('{}, {} and {}'.format(cast1, cast2, cast3))
        checkboxes1()
    elif values['-Runtime-'] is True and runtime == 0:
        runtime += 1
        runtime = str(movie['runtime'])[2:-2] + ' minutes'
        print(runtime)
        checkboxes1()
    elif all == 0 and finish == 0:
        print('To view information please choose a checkbox:')
    else:
        finish += 1
        print('****************** COMPLETE ******************')
        title = 0
        plot = 0
        year = 0
        director = 0
        cast = 0
        runtime = 0
        finish = 0
        values[0] = ''
        run_code()

run_code()