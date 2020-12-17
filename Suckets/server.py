import socket
import datetime 
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import csv

s = socket.socket()         
 
s.bind(('0.0.0.0', 8090 ))
s.listen(0)                 
print("hello from server")
ekg_content = list()

time = list()
czas_pobrania = 5
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []

def animate(i, xs, ys):

    # Read temperature (Celsius) from TMP102

    # Add x and y to lists
    # xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    # ys.append(temp_c)

    # Limit x and y lists to 20 items
    xs = xs[-200:]
    ys = ys[-200:]

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys)

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    # plt.title('TMP102 Temperature over Time')
    # plt.ylabel('Temperature (deg C)')

while len(ekg_content)<2000:
 
    client, addr = s.accept()
 
    while True:
        content = client.recv(8)
       
        if len(content) ==0:
           break
 
        else:
            print(content)
            ekg_content.append(float(content.decode()))
            time.append(czas_pobrania * len(ekg_content))
            
    client.close()   
    # ani = animation.FuncAnimation(fig, animate, fargs=(ekg_content), interval=200)
    # plt.show()        
    

print("got signal")

plt.plot(time, ekg_content)
plt.show()
 
with open('test3.csv', 'w+', newline='') as f:
    # data = list(csv.writer(f))
    writer = csv.writer(f)
    writer.writerow(time)
    writer.writerow(ekg_content)
    # for x in ekg_content:
    #     writer.writerow(x)
   
