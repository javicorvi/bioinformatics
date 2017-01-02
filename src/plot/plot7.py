import numpy as np
import pylab as pl

for i in xrange(1, 5):
    pl.subplot(220+i)
    pl.pie([i,2], labels=["a","b"], autopct='%1.1f%%')

fig = pl.gcf()
axe = fig.add_axes([0.4,0.4,0.2,0.2])

pie = pl.pie([1,1], labels=["a","b"])
l = pl.legend(title="sample", loc="center")
for group in pie:
    for x in group:
        x.set_visible(False)

pl.show()