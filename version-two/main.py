from tkinter import *
import imdb

i = imdb.IMDb()

title_count = 0
plot_count = 0
year_count = 0
director_count = 0
cast_count = 0
runtime_count = 0
all_count = 0
finish_count = 1

def var_states():
	global all_box, title_box, plot_box, year_box, director_box, cast_box, runtime_box
	all_box = var1.get()
	title_box = var2.get()
	plot_box = var3.get()
	year_box = var4.get()
	director_box = var5.get()
	cast_box = var6.get()
	runtime_box = var7.get()
	search()

def search():
	global movie, id, searchlist
	output_box.delete("1.0", "end")
	searchlist = i.search_movie(e1.get())
	id = searchlist[0].movieID
	movie = i.get_movie(id)
	results()

def results():
	global title_box, plot_box, year_box, director_box, cast_box, \
		runtime_box, all_count, title_count, plot_count, year_count, \
		director_count, cast_count, runtime_count
	if all_box == 1 and all_count == 0:
		all_count += 1
		title_box = 1
		plot_box = 1
		year_box = 1
		director_box = 1
		cast_box = 1
		runtime_box = 1
		results()
	elif title_box == 1 and title_count == 0:
		title_count += 1
		output_box.insert(END, str(movie['title']) + '\n')
		results()
	elif plot_box == 1 and plot_count == 0:
		plot_count += 1
		split_string = str(movie['plot']).split(":", 1)[0]
		output_box.insert(END, split_string[2:] + '\n')
		results()
	elif year_box == 1 and year_count == 0:
		year_count += 1
		output_box.insert(END, str(movie['year']) + '\n')
		results()
	elif director_box == 1 and director_count == 0:
		director_count += 1
		output_box.insert(END, str(movie['director'])[32:-3] + '\n')
		results()
	elif cast_box == 1 and cast_count == 0:
		cast_count += 1
		cast1 = movie['cast'][0]
		cast2 = movie['cast'][1]
		cast3 = movie['cast'][2]
		output_box.insert(END, str('{}, {} and {}'.format(cast1, cast2, cast3)) + '\n')
		results()
	elif runtime_box ==1 and runtime_count == 0:
		runtime_count += 1
		output_box.insert(END, str(movie['runtime'])[2:-2] + ' minutes' + '\n')
		results()
	else:
		all_count = 0
		title_count = 0
		plot_count = 0
		year_count = 0
		director_count = 0
		cast_count = 0
		runtime_count = 0
		return

title = 'reelSRCH'
root = Tk()
root.title('reelSRCH')
root.resizable(False, False)
root.config(bg='light blue')

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()

main_frame = Frame(root, padx=50, pady=5,bg='light blue')
main_frame.pack()
#l1 = Label(main_frame,text='Please enter the name of a movie below', bg='light blue')
#l1.pack()
Label(main_frame, text='Movie Title: ', bg='light blue').pack(side=LEFT)
e1 = Entry(main_frame, fg='black', bg='gray94', highlightthickness=0, borderwidth=2, relief="groove")
e1.pack(side=LEFT)

frame = Frame(root, padx=50, pady=5,bg='light blue')
frame.pack()
c1 = Checkbutton(frame, text="All", bg='light blue',variable=var1)
c1.pack(side=LEFT)
c2 = Checkbutton(frame, text="Title", bg='light blue',variable=var2)
c2.pack(side=LEFT)
c3 = Checkbutton(frame, text="Plot", bg='light blue',variable=var3)
c3.pack(side=LEFT)

c4 = Checkbutton(frame, text="Year", bg='light blue',variable=var4)
c4.pack(side=LEFT)
c5 = Checkbutton(frame, text="Director", bg='light blue',variable=var5)
c5.pack(side=LEFT)
c6 = Checkbutton(frame, text="Cast", bg='light blue',variable=var6)
c6.pack(side=LEFT)
c7 = Checkbutton(frame, text="Runtime", bg='light blue',variable=var7)
c7.pack(side=LEFT)

output_frame = Frame(root, padx=50, pady=5, bg='light blue') #highlightbackground='grey', highlightthickness=1
output_frame.pack()
output_frame.config(width=200)

output_box = Text(output_frame, width=60,height=10, highlightthickness=0,bg='gray94', borderwidth=2, relief="groove")
output_box.pack()
#Label(output_frame, bg='light blue', text='', width=1).pack()

button_frame = Frame(root,padx=50, pady=5,bg='light blue')
button_frame.pack()
b1 = Button(button_frame, text='Search', highlightthickness=0, command=var_states, bg='light blue') #print_output
b1.pack(side=LEFT, padx=10)
b2 = Button(button_frame, text='Exit', highlightthickness=0, command=root.destroy, bg='light blue')
b2.pack(side=LEFT)
root.mainloop()
