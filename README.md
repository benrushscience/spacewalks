# Spacewalks

## Overview
Spacewalks is a Python analysis tool for researchesr to generate visualizations and stat summaries of NASA's extravehicular activitys (EVA) datasets

## Features

Key features of Spacewalks:
- Generates CSV table of summary statistics of Extravehicular Activity (EVA) Crew Sizes
- Generates a line plot to show the cumulative distribution of spaces walks over time

## Pre-requisities

Spacewalks was developed using Python 3.12

To install and run Spacewalks you will need have Python >=3.12
installed. You will also need the following libraries

- [NumPy](https://www.numpy.org/) >=2.0.0 - Spacewalk's test suite uses NumPy's statistical functions
- [Matplotlib](https://matplotlib.org/stable/index.html) >=3.0.0  - Spacewalks uses Matplotlib to make plots
- [pytest](https://docs.pytest.org/en/8.2.x/#) >=8.2.0  - Spacewalks uses pytest for testing
- [pandas](https://pandas.pydata.org/) >= 2.2.0 - Spacewalks uses pandas for data frame manipulation 

## Installation

To install, find the respository github.com/benrushscience/spacewalks and clone to your local repo. The repository is public and you will not have push permissions by default. We recommend using a virtual environment to maintain the exact versions of packages.

## Usage

The eva_data_analysis.py file contains several analysis functions. After importing packages and the eva-data.json, the function calculate_crew_size(crew) parses a string of crew member names and counts the number of names separated by a ";".

```
git clone https://github.com/benrushscience/spacewalks.git
cd spacewalks
```

Install required packages from requirements.txt

Import packages and data

```
def calculate_crew_size(crew):
    """
    Calculate the size of the crew for a single crew entry

    Args:
        crew (str): The text entry in the crew column containing a list of crew member names

    Returns:
        (int): The crew size
    """
    if crew.split() == []:
        return None
    else:
        return len(re.split(r';', crew))-1
```