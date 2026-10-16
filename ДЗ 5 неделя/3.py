import pandas as pd
import os
x_path = os.path.join(os.path.dirname(__file__), "imdb_top_250.csv")
films = pd.read_csv(x_path)
film_genres_list = list(films['Genre'])

complex_genres = [] 
for film_genre in film_genres_list:
    genres = film_genre.split(' | ') 
    if len(genres) > 1: 
        for genre in genres:
            film_genres_list.append(genre) 
        complex_genres.append(film_genre) 

for genre in complex_genres:
    film_genres_list.remove(genre)
    
genres_set = set(film_genres_list)
print(genres_set)


from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        zhanr = str(feet.get())
        if zhanr in genres_set:
            mask = films['Genre'].str.contains(zhanr, case=False, na=False, regex=False)
            matching_films = films[mask]
            random_film = matching_films.sample(n=1).iloc[0]
            ans.set(f"{random_film['Title']} ({random_film.get('Year', '?')})")
    except ValueError:
        pass

root = Tk()
root.title("films")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=20, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

ans = StringVar()
ttk.Label(mainframe, textvariable=ans).grid(column=2, row=3, sticky=(W, E))
ttk.Button(mainframe, text="подобрать", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="Введите жанр:").grid(column=1, row=1, sticky=W)

feet_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()