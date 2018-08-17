import requests as r
from chalice import Chalice
from io import StringIO
from contextlib import redirect_stdout

app = Chalice(app_name='swapi')

api_url = 'https://swapi.co/api/'


# Default landing page
@app.route('/')
def index():
    return 'Sorry, nothing to see here\n\nTry adding /ship-pilots or /films to your url and see what happens.'


# route to get a list of ships and corresponding pilots
@app.route('/ship-pilots')
def get_ships_pilots():
    response = r.get(api_url + 'starships/')
    results = response.json()['results']
    # Capturing Standard Output as a string
    s = StringIO()
    with redirect_stdout(s):
        print("Star Wars Ships and Pilots from SWAPI")
        for ship in results:
            ship_name = ship['name']
            ship_pilots = ship['pilots']
            if ship_pilots == []:
                pilot_info = "  Unknown\n"
            else:
                pilot_info = get_pilot_info(ship_pilots)
            print(f'--------------------\nShip: {ship_name}\n Pilot(s):')
            print(pilot_info)

    fleet_data = s.getvalue()

    return fleet_data


def get_pilot_info(ship_pilots):
    results = ''  # Create empty string
    # Iterate through all pilots and identify species
    for pilot in ship_pilots:
        pilot_info = r.get(pilot).json()
        pilot_name = pilot_info['name']
        pilot_species = r.get(pilot_info['species'][0]).json()['name']
        results += f'  - Name: {pilot_name}\n    - Species: {pilot_species}\n'
    return results


# route to get list of Star Wars films.
@app.route('/films')
def get_films():
    response = r.get(api_url + 'films/')
    results = response.json()['results']
    s = StringIO()
    with redirect_stdout(s):
        print("----- List of Star Wars films -----")
        for movie in results:
            movie_title = movie['title']
            episode = movie['episode_id']
            print(f'Title: {movie_title}\n - Episode: {episode}')
    movie_data = s.getvalue()
    return movie_data
