import serial
import time
import sys
import os

ser = serial.Serial('/dev/ttyACM0')
        
def switchOff(args):
    try:
        # it takes some time to initiate the port, add a sleep of 2 seconds.
        for i in range(1,17):
            time.sleep(1)  
            arg = str(i).zfill(2)
            # a = arg.split(' ')
            # print 'a=',a[]
            # return arg
            ser.write(b'N'+arg)
        # ser.close()
    except:
        print 'Error: Cannot connect to device ',args

    os.environ.setdefault('DJANGO_SETTINGS_MODULE','sbhs_server.settings')

    import django
    django.setup()

    
    from sbhs_server.tables.models import Board

    for i in range(1,17):
        b = Board.objects.get(id = i)
        b.power_status = 0
        b.save()

if __name__ == '__main__':
    switchOff(sys.argv)