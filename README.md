# pim_features_analysis

Python program to analyze structure feature identifiers from a Informatica Product 360 PIM system.

Takes a csv file as input. Must be utf-8 encoded and contain a column named "Identifier".

Identifies all the feature identifiers that contain invalid characters, i.e. that match the regex pattern: `[^a-zA-Z0-9_-]`.  

Saves the result in a new csv file with the same name as the input file with `_analyzed` suffix.

## Installation

Install in a Python virtual enviroment:

```console
python -m pip install "git+https://github.com/george-cm/pim_features_analysis#egg=pim_features_analysis"
```

## Usage

Use from the command line:

```console
pim_features_analysis -h
usage: pim_feature_analyis [-h] [--version] input_csv

Analysis of the PIM strucure features.

positional arguments:
  input_csv      Path to the input file.

options:
  -h, --help     show this help message and exit
  --version, -V  show program's version number and exit
```

## Example

The input file is named `structure_features.csv` with the features identifier in the "Identifier" column:

```console
pim_features_analysis "structure_features.csv"
```

The results are saved to a new file named `structure_features_analyzed.csv`.  
