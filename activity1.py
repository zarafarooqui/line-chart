import matplotlib.pyplot as plt
x=[0,5,10,15,20,25,30]
y1=[0,5,10,15,20,25,30]
y2=[10,12,15,12,20,10,0]
plt.plot(x,y1,linestyle="dotted",marker="^",ms=12,mec="red",color="blue")
plt.plot(x,y2,linestyle="dashed",marker="D")
plt.title("velocity_Time graph")
plt.xlabel("Velocity")
plt.ylabel("Time")
plt.xlim(5,23)
plt.ylim(5,25)
plt.show()