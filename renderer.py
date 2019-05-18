import os
import glob

BASEDIR = 'books'

def getfiles(book_title, chapnum):
    DIR = os.path.join(BASEDIR, book_title)
    GLOB = glob.glob(os.path.join(DIR, "Chap_{}_par_*.txt.html".format(chapnum)))
    npaths = len(GLOB)
    files =  (os.path.join(DIR, "Chap_{}_par_{}.txt.html".format(chapnum, n)) for n in range(1, npaths+1))
    return [path for path in files if os.path.exists(path)]

def concat(filelist):
    strings = []
    print(len(filelist), 'FILES')
    for path in filelist:
        with open(path) as f:
            strings.append(f.read())
    return "\n".join(strings)