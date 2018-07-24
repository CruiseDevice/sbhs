import sys
import serial
import time
import os

ser = serial.Serial('/dev/ttyACM0')
def switchOnn(args):    
    try:
        for i in range(1,17):
            time.sleep(2)
            arg = str(i).zfill(2)
            print arg
            ser.write(b'F'+arg)
            
        # ser.close()
    except:
        print 'Error: Cannot connect to device ',args

    os.environ.setdefault('DJANGO_SETTINGS_MODULE','sbhs_server.settings')

    import django
    django.setup()

    
    from sbhs_server.tables.models import Board

    for i in range(1,17):
        b = Board.objects.get(id = i)
        b.power_status = 1
        b.save()

if __name__ == '__main__':
    switchOnn(sys.argv)
