"""
@pb-jchin says:

Here is a snippet of the python script I use to split a fasta file by the movie names. Please read it and test it to see if it fits your user's case.

# https://github.com/PacificBiosciences/FALCON/issues/82
"""
import sys
state = 1
files = {}
seq = ""
read_name = ""
with open(sys.argv[1]) as f:
    for l in f:
        l = l.strip()
        if l[0] == ">":
            if len(seq) > 0 and len(read_name) != "":
                mn = read_name.split("/")[0]
                if mn not in files:
                    f = open(read_name.split("/")[0]+".subreads.fasta","a")
                    files[mn] = f
                print >> files[mn], ">"+read_name
                seq = "".join(seq)
                for s in xrange(0, len(seq), 60):
                    print >> files[mn], seq[s:s+60]

            read_name = l[1:]
            state = 1
            seq = []
            continue
        else:
            seq.append(l)

if len(seq) > 0 and len(read_name) != "":
    mn = read_name.split("/")[0]
    if mn not in files:
        f = open(read_name.split("/")[0]+".subreads.fasta","a")
        files[mn] = f
    print >> files[mn], ">"+read_name
    for s in xrange(0, len(seq), 60):
        print >> files[mn], seq[s:s+60]

for mn in files:
    files[mn].close()

