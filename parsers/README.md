# XML Parsers

Parsing this much xml requires a bit of complexity.

## Downloading the files

[download_scripts](download_scripts) has the scripts to download all of the `7z` files.

## Spark parser

[spark_parser.ipynb](spark_parser.ipynb) contains a spark implementation of an xml parser. This was infeasible, because i could not allocate enough resources to spark - and there was more overhead than necessary.

## ET_parser

[ET_parser.py](ET_parser.py) uses the native python xml parser library to parse. It is meant to be run through [runparser.sh](runparser.sh) with `sbatch`

## utility scripts

[delete_extra.sh](utility_scripts/delete_extra.sh) just contains a simple utility script to delete duplications of files

the [fix_verify](utility_scripts/fix_verify) directory contains some permutations of the fixing and verification script to verify validity of `csv` files and reparse failures. Mostly, it is meant to reparse failures.

# Results

With an average size of  ~70GB per file dump, and with ~800 files, ~56000GB (56TB) of xml was parsed into ~150GB of csv files.
