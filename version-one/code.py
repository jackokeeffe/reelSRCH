import imdb
from GUI import sg, window, values

i = imdb.IMDb()

title = 0
plot = 0
year = 0
director = 0
cast = 0
runtime = 0
all_values = 0
finish = 1

def run_code():
    global letter, sg, event, name, movie, title, plot, year, director, cast, runtime
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'EXIT':
            break

        elif event == 'SEARCH':
            title = 0
            plot = 0
            year = 0
            director = 0
            cast = 0
            runtime = 0
            all_values = 0

            if values[0] == '':
                print('Please enter a valid title')
                run_code()
            else:
                print('Searching for: ' + str(values[0]))
                print('Please wait while your results load...')
                searchlist = i.search_movie(str(values[0]))
                id = searchlist[0].movieID
                movie = i.get_movie(id)
                print('-----------------------------')
                checkboxes1()

def checkboxes1():
    global event, movie, title, plot, year, director, cast, runtime, finish, value, all_values
    if values['-Title-'] is True and title == 0:
        title += 1
        print(movie['title'])
        checkboxes1()
    elif values['-Plot-'] is True and plot == 0:
        plot += 1
        split_string = str(movie['plot']).split(":", 1)[0]
        print(split_string[2:])
        checkboxes1()
    elif values['-Year-'] is True and year == 0:
        year += 1
        year = movie['year']
        print(year)
        checkboxes1()
    elif values['-Director-'] is True and director == 0:
        director += 1
        print(str(movie['director'])[32:-3])
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
        print(str(movie['runtime'])[2:-2] + ' minutes')
        checkboxes1()
    elif values['-All-'] is True and all_values == 0:
        all_values += 1
        values['-Title-'] = True
        values['-Plot-'] = True
        values['-Year-'] = True
        values['-Director-'] = True
        values['-Cast-'] = True
        values['-Runtime-'] = True
        checkboxes1()
    elif all_values == 0 and finish == 0:
        print('To view information please choose a checkbox:')
    elif event == 'WIN_CLOSED':
        exit()
    else:
        finish += 1
        print('****************** COMPLETE ******************')
        title = 0
        plot = 0
        year = 0
        director = 0
        cast = 0
        runtime = 0
        finish = 1
        return

if __name__ == '__main__':
    run_code()