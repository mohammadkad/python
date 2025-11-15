<!-- 1404-08-24 -->

## TOON (Token-Oriented Object Notation)

### install directly from GitHub:
pip install git+https://github.com/toon-format/toon-python.git

- from toon_format import encode, decode
- encode([{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}])

### CLI usage:
- toon -h
- toon input.json -o output.toon      # Encode
- toon data.toon -o output.json       # Decode
