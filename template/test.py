import os
import argparse


parser = argparse.ArgumentParser(description="Test application")
parser.add_argument('filename', 
    type=str,
    help="Name of file with testinput to run",
    nargs="+")

args = parser.parse_args()



for filename in args.filename:
    try:
        print("Input for %s:" % filename)
        os.system("cat %s" % filename)
        print("Output for %s" % filename)
        os.system("cat %s | python run.py" % filename)
    except:
        print("Error with filename %s" %s)
