
from signal import pause
from venv import create


for loop in range(10):
    file = create( 'message.txt' )
    pause()
    file = open('message.txt', 'w')
    file.write('/n Hello World!')
    file.close()

    

