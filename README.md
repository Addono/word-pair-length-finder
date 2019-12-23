# Word Pair Length Finder

## Table of Contents
+ [About](#about)
+ [Getting Started](#getting_started)
+ [Usage](#usage)

## About<a name = "about"></a>
A small script to find word pairs when you know the length of these words. Originally written for finding book titles for a Chistmas puzzle. 

## Getting Started<a name = "getting_started"></a>
These instructions will get you a copy of the project up and running on your local machine.

[![asciicast](https://asciinema.org/a/gvBbu4VUGI9uLQxTko5JU4RWu.svg)](https://asciinema.org/a/gvBbu4VUGI9uLQxTko5JU4RWu)

### Prerequisites

For this project, you will need Python 3 and (optionally) `virtualenv`.
```
brew install python3 pyenv-virtualenv
```

### Installing
Create a virtual environment.
```bash
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage<a name = "usage"></a>

Enter the virtual environment, if not already.
```bash
source venv/bin/activate
```

To run the script:
```bash
python search.py
```

This project comes with a dataset containing all Dutch book titles according to [book.be](https://book.be) released in 2019. You can replace the `data.csv` file with any dataset you like. The script will use the first column as its input.