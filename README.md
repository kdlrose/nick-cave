# nick cave lyric search

a simple python-based web app that allows users to search the complete lyrics of Nick Cave across various projects: The Birthday Party, The Bad Seeds, Grinderman, Nick Cave & Warren Ellis.

a prior React version of this application was inspired by [shaynak/taylor-swift](https://github.com/shaynak/taylor-swift) which scraped lyrics from Genius, but [the Nick Cave dataset](https://github.com/sailorfe/nick-cave-lyrics) is hand-compiled.

## live application

the app is deployed on Render: [Nick Cave Lyric Search](https://nick-cave.onrender.com)

## local installation

```bash
git clone https://github.com/sailorfe/nick-cave.git
cd nick-cave
git submodule update --init
uv run app.py   # live development server
```

## data format

this application expects lyric data in a flat list of JSON object, with critical keys for contextual rendering:

```json
[
    {
        "song":"Black Hair",
        "album":"The Boatman's Call",
        "prev":"Last night my kisses",
        "lyric":"Were banked in black hair",
        "next":"And in my bed, my lover,",
        "artist":"Nick Cave & The Bad Seeds",
        "year":"1997",
        ...
    }
]
```

## license

this project is licensed under the MIT license.
