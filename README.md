# Get News
### Dirty-simple news checking Python script (Portuguese language results)

<hr>

Intended use later as a component on another larger project, 
the full automation of a YouTube channel.

Will use Pegassus for Summary in a later iteration.

<hr>

All in Portuguese language: (Intended YT channel default language)
<br>
   ➡️Get daily news on a subject from google news,
   <br>
   ➡️download and parse the page associated with news,
   <br>
   ➡️create AI summary of the contents,
   <br>
   ➡️blind-choose between summary and original based on size and *really* dumb logic,
   <br>
   ➡️print output to console and to file.
   
<hr>

Open a command prompt and `cd` to a new directory of your choosing:

(optional; recommended) Create a virtual environment with:
```
python -m venv "venv"
venv\Scripts\activate
```

To install do:
```
git clone https://github.com/vluz/GetNews.git
cd GetNews
pip install -r requirements.txt
```

On first run it may download several models.
<br>
It will take quite some time, both on reqs above and on first run.
<br>
Please allow it time to finish.
<br>
All runs after the first are then faster to load.

To run do:<br>
`python getnews.py` 


Note: Do not use this for production, it's untested and a ugly hack

TODO: Switch over to Pegassus summaries like this: https://github.com/vluz/Summary
