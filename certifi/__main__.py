import argparse

from certifi import contents, where

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--contents", action="store_true")
parser.add_argument("-c", "--contracts", action="store_true")
args = parser.parse_args()

if args.contents:
    print(contents())
if args.contracts:
    print(contracts())
else:
    print(where())
