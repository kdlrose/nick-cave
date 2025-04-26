# Nick Cave lyric search

Inspired by [shaynak/taylor-swift](https://github.com/shaynak/taylor-swift) with my hand-copied [kdlrose/nick-cave-lyrics](https://github.com/kdlrose/nick-cave-lyrics) dataset.

## Log

### 2024-09-10

- Added *Wild God*.

### 2024-08-27

#### Changes

- Added year to results.
- Moved app styles from `index.sass`.

### 2024-08-26

#### Tasks

- Make curly quotes/apostrophes interchangeable with `''`. Craziest culprit is
    "rock'n'roller" on "Babe, I'm On Fire" versus "king of rock'n'roll" on "The
    Spinning Song"
- Filter by artist if not album between TBP, TBS, Grinderman, Cave/Ellis
- Get rid of partial words, e.g. "hair" returns "chair," but I would still want
    the begining of the word to work? "gun" shouldn't return "begun," et cetera.
- Make results modal for instances of album-less releases like "Release the Bats."

## Resources

- [How to Implement Search in React JS with JSON](https://codedec.com/tutorials/how-to-implement-search-in-react-js-with-json/)
- [Deploying a React App* To GitHub Pages](https://github.com/gitname/react-gh-pages)
