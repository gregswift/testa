#!/usr/bin/python

class Testa(object):
  def __init__(self, msg="This is a test"):
    print msg

def run():
  from sys import argv
  Testa(" ".join(argv[1:]))

if __name__ == '__main__':
  run()