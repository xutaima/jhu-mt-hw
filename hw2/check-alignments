#!/usr/bin/env python
import optparse
import sys

optparser = optparse.OptionParser()
optparser.add_option("-d", "--data", dest="train", default="data/hansards", help="Data filename prefix (default=data)")
optparser.add_option("-e", "--english", dest="english", default="e", help="Suffix of English filename (default=e)")
optparser.add_option("-f", "--french", dest="french", default="f", help="Suffix of French filename (default=f)")
(opts, args) = optparser.parse_args()
f_data = open("%s.%s" % (opts.train, opts.french))
e_data = open("%s.%s" % (opts.train, opts.english))
    
for (n, (f, e, a)) in enumerate(zip(f_data, e_data, sys.stdin)):
  size_f = len(f.strip().split())
  size_e = len(e.strip().split())
  try: 
    alignment = set([tuple(map(int, x.split("-"))) for x in a.strip().split()])
    for (i,j) in alignment:
      if (i>=size_f or j>size_e):
        sys.stderr.write("WARNING (%s): Sentence %d, point (%d,%d) is not a valid link\n" % (sys.argv[0],n,i,j))
      pass
  except (Exception):
    sys.stderr.write("ERROR (%s) line %d is not formatted correctly:\n  %s" % (sys.argv[0],n,a))
    sys.stderr.write("Lines can contain only tokens \"i-j\", where i and j are integer indexes into the French and English sentences, respectively.\n")
    sys.exit(1)
  sys.stdout.write(a)

warned = False
for a in (sys.stdin): 
  if not warned:
    sys.stderr.write("WARNING (%s): alignment file is longer than bitext\n" % sys.argv[0])
    warned = true
  sys.stdout.write(a)

try:
  if (f_data.next()):
    sys.stderr.write("WARNING (%s): bitext is longer than alignment\n" % sys.argv[0])
except (StopIteration):
  pass
  
