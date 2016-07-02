import argparse
import json
import sys

from contexttimer import Timer

from pandas_driver import PandasDriver
from sqlite_driver import SqliteDriver

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Pandas operations')
  parser.add_argument('file', help='location of csv data file')
  parser.add_argument('command', help='either pandas or sqlite')
  args = parser.parse_args()

  results = { 'command': args.command, 'file': args.file }

  if args.command == "pandas":
    driver = PandasDriver(args.file)
  elif args.command == "sqlite":
    driver = SqliteDriver(args.file, "data/test.db")
  else:
    raise ValueError("bad value for command")

  with Timer() as timer:
    driver.load()
  results['load'] = timer.elapsed

  with Timer() as timer:
    driver.groupby()
  results['groupby'] = timer.elapsed

  json.dump(results, sys.stdout)
  print