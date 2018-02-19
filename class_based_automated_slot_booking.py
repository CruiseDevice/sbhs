import random
import MySQLdb
import datetime
from time import gmtime, strftime

from sbhs_server import credentials as credentials

class Automated_Slot_Booking:

    
    def __init__(self):
    
      
        self.db = MySQLdb.connect(host = credentials.DB_HOST,
                             user=credentials.DB_USER,
                             passwd=credentials.DB_PASS,
                             db=credentials.DB_NAME)
        print 'Database opened successfully'

        self.cu1= self.db.cursor()
        self.cursor5 = self.db.cursor()
        self.cu2 = self.db.cursor()

        self.nowDate=datetime.datetime.now().date()
        self.nowTime=str(datetime.datetime.now().time())
        self.SplittedTime=self.nowTime.split(":")
        self.NowdaTe=str(self.nowDate)
        self.NowdaTe=self.NowdaTe.strip()   ## To remove extra spaces strip is used##

        self.CurrentAccountIdList=[]
        self.BookedSlotId=[]
        self.RequiredMidList = []

        self.SuperUserMidList = []
        # self.SuperUserMidList = [Mid for Mid in range(1,41)]


    def SuperUserList(self):
        querry = 'SELECT * FROM tables_account'      
        self.cu1.execute(querry)
        for user in self.cu1:
            u = user[5]
            i = user[0]
            if i < 41:
                suser = 'suser'+str(i)
                if u == suser:
                    self.SuperUserMidList.append(int(i))

    # print SuperUserMidList

    def CurrentBookedAccount(self):
        
        querry = 'SELECT * FROM tables_booking'
        self.cu1.execute(querry)
        # return cu1
        for DateTimeInBooking in self.cu1:
            nn = str(DateTimeInBooking[2])
            daTe = nn[0:11]
            tiMe = nn[11:13]
            daTe = daTe.strip()

            if daTe == self.NowdaTe and int(self.SplittedTime[0]) + 1 == int(DateTimeInBooking[6]):
                self.CurrentAccountIdList.append(int(DateTimeInBooking[5]))
                self.BookedSlotId.append(int(DateTimeInBooking[0]))

        print 'BookedSlotId', self.BookedSlotId
        print 'CurrentAccountIdList', self.CurrentAccountIdList
    
    def BookedMidList(self):
        # self.SelectFromTablesAccount(self.cu2)
        querry = 'SELECT * FROM tables_account'
        self.cu2.execute(querry) 

        for AccoutIdFromTablesAccnt in self.cu2:
            # var = AccoutIdFromTablesAccnt[0]

            for Id in range(len(self.CurrentAccountIdList)):
                if (self.CurrentAccountIdList[Id]) == (AccoutIdFromTablesAccnt[0]):
                    self.RequiredMidList.append(int(AccoutIdFromTablesAccnt[0]))
        
        print 'RequiredMidList ',self.RequiredMidList


    def BookSlot(self):
        MidsTobeBooked = [mId for mId in self.SuperUserMidList if mId not in self.RequiredMidList]
        print 'MidsTobeBooked', MidsTobeBooked
        for BookMid in range(0,len(MidsTobeBooked)):
            ToInsert = [int((MidsTobeBooked[BookMid])), int(self.SplittedTime[0])+1, (datetime.datetime.now()),(datetime.datetime.now()),(self.nowDate)]
            # try:
            self.cursor5.execute("INSERT INTO tables_booking(account_id,slot_id,created_at,updated_at,booking_date) VALUES(%s,%s,%s,%s,%s)",ToInsert)
            # except:
                # pass
            self.db.commit()

    def CloseDb(self):
        self.cu1.close()
        self.cu2.close()
        self.cursor5.close()
        self.db.close()
        print 'Database closed successfully'
