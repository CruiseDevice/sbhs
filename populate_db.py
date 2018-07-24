import MySQLdb
import os,sys
import datetime
import sqlite3
from time import gmtime, strftime

from django.db import connection

from sbhs_server import credentials as credentials

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                        'sbhs_server.settings')


import django
django.setup()

from sbhs_server.tables.models import Board
from django.contrib.auth.hashers import make_password

connection_vendor = str(connection.vendor)

if connection_vendor == 'mysql':
    db = MySQLdb.connect(host=credentials.DB_HOST,
        user=credentials.DB_USER,
        passwd=credentials.DB_PASS,
        db=credentials.DB_NAME)
else:
    db = sqlite3.connect("sbhs.sqlite3")


print db
print 'database opened successfully'
# cursor = db.cursor()

## Datetime used when script runs
nowDate=datetime.datetime.now().date()
nowTime=str(datetime.datetime.now().time())
SplittedTime=nowTime.split(":")
NowdaTe=str(nowDate)
NowdaTe=NowdaTe.strip()

print 'Nowdate ', NowdaTe
print 'SplittedTime ', SplittedTime
print 'nowTime ', nowTime[:8]

def create_board(number_of_board_and_users):
    cursor1 = db.cursor()
    for i in range(1,int(number_of_board_and_users)+1):
        mid = i
        online = 1
        created_at = datetime.datetime.now()
        updated_at = datetime.datetime.now()
        temp_offline = 0
        power_status = 0
        ToInsert = [int(mid),int(online),created_at,updated_at,temp_offline,power_status]
        if connection_vendor == 'mysql':
            cursor1.execute("INSERT into tables_board(mid,online,created_at,updated_at,temp_offline,power_status) VALUES(%s,%s,%s,%s,%s,%s)",ToInsert)
        else:
            cursor1.execute("INSERT into tables_board(mid,online,created_at,updated_at,temp_offline,power_status) VALUES(?,?,?,?,?,?)",ToInsert)
        db.commit()
        # cursor1.close()


def create_account(number_of_board_and_users):
    cursor2 = db.cursor()
    for i in range(1,int(number_of_board_and_users)+1):
        name = 'Super User '+str(i)
        email= 'suser'+str(i)+'@gmail.com'
        username='suser'+str(i)
        password = 'suser'+str(i)+'4229'
        pwd = make_password(password)
        is_active = 1
        is_admin = 0
        # board = Board.objects.get(mid=i)
        # temp = i
        # if temp > 30:
        #     temp = 1
        board = i
        created_at = datetime.datetime.now()
        updated_at = datetime.datetime.now()
        ToInsert = [pwd,name,username,email,is_active,is_admin,created_at,updated_at,board]
        if connection_vendor == 'mysql':
            cursor2.execute("INSERT into tables_account(password,name,username,email,is_active,is_admin,created_at,updated_at,board_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",ToInsert)
        else:
            cursor2.execute(
                "INSERT into tables_account(password,name,username,email,is_active,is_admin,created_at,updated_at,board_id) VALUES(?,?,?,?,?,?,?,?,?)",
                ToInsert)
        db.commit()
        # cursor2.close()

def create_slot(number_of_slot):
    cursor3 = db.cursor()
    for i in range(int(number_of_slot)):
        start_hour = i
        start_minute=0
        end_hour = i
        end_minute = 55
        create_at = datetime.datetime.now()
        updated_at = datetime.datetime.now()
        ToInsert = [start_hour,start_minute, end_hour,end_minute,create_at,updated_at]
        if connection_vendor == 'mysql':
            cursor3.execute("INSERT into tables_slot(start_hour,start_minute,end_hour,end_minute,created_at,updated_at)VALUES(%s,%s,%s,%s,%s,%s)",ToInsert)
        else:
            cursor3.execute(
                "INSERT into tables_slot(start_hour,start_minute,end_hour,end_minute,created_at,updated_at)VALUES(?,?,?,?,?,?)",
                ToInsert)
        db.commit()
        # cursor3.close()

number_of_board_and_users = raw_input('Enter Number of board and raw users you want.')
# number_of_slot = raw_input('Enter how many slots to create.')
create_slot(24)
create_board(number_of_board_and_users)
create_account(number_of_board_and_users)

# cursor1.close()
# cursor2.close()
db.close()
print 'database closed successfully'

