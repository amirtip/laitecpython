import os
f=open('p2.py','wt')
f.write('import random\nfor i in range(1001):\n\tx=random.randrange(1,1000)\n\tprint(f"{i}={x}")')
f.close()
import p2
