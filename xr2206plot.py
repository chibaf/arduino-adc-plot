import serial, sys
import matplotlib.pyplot as plt

x=range(0, 100, 1)
data=[0]*100

ser=serial.Serial(sys.argv[1],sys.argv[2])
print("connected to: " + ser.portstr)
while True:
  line = ser.readline()
  line2=line.strip().decode('utf-8')
  data0=line2.split(", ")
  print(data0[1])
  data.pop(-1)
  data.insert(0,float(data0[1]))
  plt.clf()
  plt.ylim([-1.0,10.0])
  plt.plot(x,data)
  plt.pause(0.1)

ser.close()
