# Collatz conjecture
# Dtermining the correlation between an integer
# and the number of steps it takes to reach the
# Collatz loop for the integer in a given range
# Muhtar Hanif Alhassan 24/06/2022
import matplotlib.pyplot as plt

entint = int(input('Enter highest number: '))
maxint = entint + 1

for myint in range(1, maxint, 1):
    nsteps = 0
    gint = myint
    while gint > 1:
        if gint % 2 == 0:
            nxint = int(gint / 2)
            nsteps += 1
        else:
            nxint = gint * 3 + 1
            nsteps += 1
        gint = nxint
    print(myint, "====", nsteps)
    plt.plot(myint, nsteps, color='green', linestyle='solid', linewidth=1,
             marker='o', markerfacecolor='red', markersize=2)
plt.xlabel('starting number')
plt.ylabel('number of steps')
message = f"Collotz Conjecture steps for integers between 1 and {entint}"
plt.title(message)
plt.show()
