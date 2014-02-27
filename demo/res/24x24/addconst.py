#!/usr/bin/env python

import re
import os
import sys

def addconst():
  """
  add `const` to XPM files generated by `convert` command in linux 
  systems, to prevent overwhelming warnings like:
  \t`warning: deprecated conversion from string constant to char *`
  """
  files=filter(lambda x:x[len(x)-4:len(x)]=='.xpm',os.listdir(sys.argv[1]))
  for i,f in enumerate(files):
    with open(f,'rt') as fp:
      # print f
      a=re.sub('\nstatic char \*(.+)\[\]','\nstatic const char * \\1_xpm[]',fp.read())
      # sys.stderr.write(a.split('\n')[1]+'\n')
      fp.close()
      fp=open(f,'wt')
      fp.write(a)

if __name__=='__main__':
  addconst()
