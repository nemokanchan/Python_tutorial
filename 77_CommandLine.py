#Command line utility are programs that can be run from terminal.
#curl:It is a command line utility that can be used by giving command.

import argparse
parser=argparse.ArgumentParser()

parser.add_argument("url", help="Url of the file to download")
parser.add_argument("arg2", help="Description of argument 2")
#Parse the argument
args=parser.parse_args()
#Use argument in the code
print(args.url)
print(args.arg2)
