from matplotlib import pyplot as plt
from matplotlib.patches import Circle, Rectangle, RegularPolygon
from itertools import product
import numpy as np

f,ax=plt.subplots(figsize=(9.1,11.2));plt.tight_layout()

colors=["dodgerblue","aqua","white","gold","darkorange","red"]
c1,c2,c3,c4,c5,c6=colors
r1,r2,r3,r4,r5,r6=[0.07*(i+1) for i in range(6)]

for i in range(6):
	r=Rectangle((0.7+1.3*i,0),1.3,0.5,edgecolor="black",facecolor=colors[i])
	ax.axvline(0.7+1.3*i,color="grey",linestyle=":")
	c=Circle((0,1.35+1.7*i),radius=0.07*(i+1),edgecolor="black",facecolor="white")
	ax.axhline(0.5+1.7*i,color="grey",linestyle=":")
	ax.add_patch(r)
	ax.add_patch(c)

ax.set_xlim(-.5,8.6)
ax.set_ylim(-0.1,11.1)
ax.set_axis_off()
plt.savefig("CMD.pdf",density=300)
plt.clf()

f,ax=plt.subplots(figsize=(9.1,11.2));plt.tight_layout()
ax.set_xlim(-.5,8.6)
ax.set_ylim(-0.1,11.1)
ax.set_axis_off()
xgrid=np.arange(.1,8.6,1.3)
ygrid=np.arange(.5,11.1,1.7)
pos=list(product(xgrid,ygrid))
props=[[c1,r6],[c1,r5],[c1,r2],[c2,r5],[c2,r4],[c2,r1],[c3,r5],[c3,r4],[c3,r3],[c4,r4],[c4,r3],[c4,r2],[c5,r5],[c5,r4],[c5,r2],[c5,r1],[c6,r6],[c6,r5],[c6,r1]]
for i,p in enumerate(pos):
	ax.add_patch(Circle(p,radius=props[i%len(props)][1],edgecolor="black",facecolor=props[i%len(props)][0]))
#Circle((0,1.35+1.7*i),radius=0.07*(i+1),edgecolor="black",facecolor="white")
plt.savefig("stars.pdf",density=300)
plt.clf()

f,ax=plt.subplots(figsize=(9.1,11.2));plt.tight_layout()
ax.set_xlim(-.5,8.6)
ax.set_ylim(-0.1,11.1)
ax.set_axis_off()
xgrid=np.arange(.1,8.6,1.3)
ygrid=np.arange(.5,11.1,1.6)
pos=list(product(xgrid,ygrid))
sunprops=[[c4,r3],[c5,r4],[c6,r5],[c6,r6],[c1,r2],[c2,r1]]
for i,p in enumerate(pos):
	ax.add_patch(RegularPolygon(xy=p,numVertices=5,radius=sunprops[i%len(sunprops)][1],edgecolor="black",facecolor=sunprops[i%len(sunprops)][0]))
	#ax.annotate(ur"$\u1f576$",xy=p)
plt.savefig("sun.pdf",density=300)
plt.clf()
