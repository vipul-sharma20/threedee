"""
threedee

Usage:
  threedee github-skyline --width=<width> --stl-path=<path> --username=<username> --start=<start-year> --end=<end-year>

Options:
    --width=<width>      Number of years of contibution (number of skylines) in one row. Example: If there are 10 years of GitHub skyline, --width=2 will create 5 rows each with 2 years combined along the X axis
  --stl-path=<stl-path>  Path to directory with STLs stored. File names should be of the format "<github-username>-<year>.stl"
  --username=<username>  GitHub username
  --start=<start-year>   Start year (inclusive)
  --end=<end-year>       End year (inclusive)
"""

from docopt import docopt

from threedee import __version__
from threedee.github import combine_skyline


def main():
    args = docopt(__doc__, version=__version__)

    if args["github-skyline"]:
        combine_skyline(**args)

