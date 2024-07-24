import serial, sys
import matplotlib.pyplot as plt

x=range(0, 100, 1)
data=[0]*100
ser = serial.Serial(sys.argv[1],sys.argv[2])
while True:
  try:
    line = ser.readline()
    try: 
      line2=line.strip().decode('utf-8')
      if line2=='':
        line2=0.0
      else:
         line2=float(line2)
      print(line2)
    except UnicodeDecodeError:
      line2=0.0
    data.pop(-1)
    data.insert(0,line2)
    plt.clf()
    plt.ylim([-1.0,5000.0])
    plt.plot(x,data)
    plt.pause(0.1)
  except KeyboardInterrupt:
    print ('exiting')
    break
exit()
