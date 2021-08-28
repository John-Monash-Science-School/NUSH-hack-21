# NUSH-hack-21
NUSH Hack '21 entry for Collective Fullstack (JMSS team)


## How to use
* instructions go here
* Clone the GithHb repository with `git clone https://github.com/John-Monash-Science-School/NUSH-hack-21.git`
* Edit nonroutes.py and add your own access token for the mapbox api


## Running locally
* make sure python3 is installed
* if you haven't done it, create a virtualenv and activate it.
* run `pip install -r requirements.txt`
* run `python main.py`

## Where everything is
* `main.py` — the main flask file. 
* `templates/` — contains jinja html templates for rendering
* `static/` — contains all static files to be served by flask (in this case it's just tailwind)
* `components/` — contains all files referenced by preact that are dynamically loaded by flask.
* `deck/` — has our slide deck in mdx form.


## Tech stack:
* css library is a custom version of tailwind that uses css vars for colours. *please someone remind me to as our final commit remove all unused classes (otherwise the css will be a solid 1.3mb)*
* flask is the python server library.
* socket.io handles communications between live clients.
* preact does client-side reactive ui.
* mdx-deck does the slides in the deck folder.
* all icons used are done with iconify.
* Mapbox python module, that communicates with the official Mapbox API to provide accurate distances between two locations
