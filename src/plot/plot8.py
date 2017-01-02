

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
import itertools



runs=['5000','10000','15000','20000']
X = [1,2,3,4,5]
beta=[0.05,0.15,0.40,0.60,0.80]


for r in runs:
    for b in beta:
        data = []
        for n in X:
            source = open('outputruns2000.dat', 'r')
            for line in source:
                if (('beta'+b in line) & ('nsus'+n in line) & ('runs'+r+'.' in line)):
                    str,value=line.split(",")
                    data[n]=value
            source.close()        


Ys = np.array([
      [0.64,0.65,0.90,0.8,0.74],
      [0.62,0.65,0.3,0.2,0.34],
      [0.68,0.63,0.5,0.6,0.43],
      [0.32,0.67,0.45,0.89,0.79],
      [0.61,0.62,0.56,0.81,0.71]])


f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2 , sharex='col', sharey='row')
#ax6.set_visible(False) 

#nCols = len(X)  
#nRows = Ys.shape[0]
##En vez de rainbow darle yo los colores
colors = cm.rainbow(np.linspace(0, 1, len(Ys)))

#cs = [colors[i//len(X)] for i in range(len(Ys)*len(X))] 
#cs2 = ['red','green','blue','yellow','grey']
#Xs=X*nRows 
#red_patch = mpatches.Patch(color='red', label='The red data')
#plt.legend(handles=[red_patch])
#colors = cm.rainbow(np.linspace(0, 1, len(Ys)))
colors = itertools.cycle(["red", "blue", "green", "yellow", "lime"])
beta=['0.05','0.15','0.40','0.60','0.80']

subplt = [ax1,ax2,ax3,ax4]
r=0
for splt in subplt:
    i=0
    for y, c in zip(Ys, colors):
        splt.scatter(X, y, color=c)   
        splt.plot(X, y,color=c, label=beta[i])
        splt.set_title('Runs ' + runs[r])
        i=i+1
    r=r+1  
axis=[0, 6, 0, 1]
plt.axis(axis)

# Now add the legend with some customizations.
plt.legend(loc='upper right', shadow=True)


   
   
#fig.savefig('samplefigure', bbox_extra_artists=(lgd,), bbox_inches='tight')

f.text(0.5, 0.04, 'NSUS', ha='center')
f.text(0.04, 0.5, 'AUC', va='center', rotation='vertical')


plt.show()   




