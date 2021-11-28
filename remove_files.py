import os
from os import listdir
from os.path import isfile, join#list of csvs
only_csv = [f for f in listdir("Documents/tmp") if isfile(join("Documents/tmp", f))]
[os.remove("Documents/tmp/{}".format(e)) for e in only_csv]
print(only_csv," removed Documents/tmp folder clean")
