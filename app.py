from flask import Flask, render_template, request, jsonify
import json
import re

app = Flask(__name__)

DATA_FILE_PATH = "lyrics_data/lyrics.json"

try:
    with open(DATA_FILE_PATH, "r", encoding="utf-8") as f:
        LYRICS_DATA = json.load(f)
except FileNotFoundError:
    print(f"ERROR: Data file not found at {DATA_FILE_PATH}.")
    print("Ensure you have run 'git submodule update --init' and the path is correct.")
    LYRICS_DATA = []


def perform_search(query):
    """
    Searches the flat list of lyric dictionaries, returning results
    including the previous and next lines based on keys: 'prev', 'lyric', 'next'.
    """
    if not query:
        return []

    # Regex pattern for case-insensitive, whole-word search with plurals
    escaped_query = re.escape(query)
    pattern = re.compile(
        r"\b" + escaped_query + r"(?:s\b|es\b|\'s\b|s\'\b)?", re.IGNORECASE
    )

    results = []

    # Iterate through the flat list of lyric blocks
    for line_data in LYRICS_DATA:
        current_lyric = line_data.get("lyric", "")

        # Check for a match in the 'lyric' key
        if pattern.search(current_lyric):
            # Extract contextual lines and metadata using your exact JSON keys
            results.append(
                {
                    "album": line_data.get("album", "N/A"),
                    "artist": line_data.get("artist", "N/A"),
                    "year": line_data.get("year", "N/A"),
                    "song": line_data.get("song", "N/A"),
                    "prev_line": line_data.get("prev", ""),
                    "matched_line": current_lyric,
                    "next_line": line_data.get("next", ""),
                }
            )

    return results


@app.route("/")
def index():
    """Route for the main search page (renders the Jinja template)."""
    return render_template("index.html")


@app.route("/search", methods=["GET"])
def search_api():
    """API route for fetching search results."""
    query = request.args.get("q", "")
    results = perform_search(query)
    return jsonify(results)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
