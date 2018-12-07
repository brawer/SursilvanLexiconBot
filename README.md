# SursilvanLexiconBot

At some point, once the code in this repository is actually complete,
it will generate a machine-readable lexicon for the Sursilvan Romansh
language (IETF BCP47 code: `rm-sursilv`).  The plan is to build a
robot that adds Sursilvan word forms to [Lexicographical data in
Wikidata](https://www.wikidata.org/wiki/Wikidata_talk:Lexicographical_data).

For easier debugging, the output is printed as a [YAML
file](https://en.wikipedia.org/wiki/YAML), using [Universal
Features](http://universaldependencies.org/u/feat/) and [Universal
Part-of-Speech Tags](http://universaldependencies.org/u/pos/index.html).


## Usage

To generate the lexicon, run this command:

```sh
python3 build_lexicon.py
```


## License

The files in `data`, and also the generated output lexicon, are in the
Public Domain according to the [Creative Commons Zero v1.0 Universal
Public Domain Dedication](https://creativecommons.org/publicdomain/zero/1.0/).  The code for generating the lexicon is currently licensed under the
[MIT-0 license](https://spdx.org/licenses/MIT-0.html).
