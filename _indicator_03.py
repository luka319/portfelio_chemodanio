
import sys, time

for i in range(5, 101, 5):

    d = '▒' * ( i//4) 

    sys.stdout.write('\r ...%s %s %%' % (d,i) )
    
    sys.stdout.flush()
    time.sleep(1)

print('\n the End')
