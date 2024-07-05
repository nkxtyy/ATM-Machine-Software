import mysql.connector as conn
from random import randint
myconn=conn.connect(host='localhost',user='root',passwd='kriti',database='ATM')
if myconn.is_connected()==False:
    print('ERROR')
if myconn.is_connected()==True:
    print('...........CONNECTION SUCCESSFUL...........')

cursor=myconn.cursor()
cursor.execute('DROP TABLE IF EXISTS ATM')
cursor.execute('''CREATE TABLE ATM(ACCNO CHAR(8) NOT NULL PRIMARY KEY,
                        ACC_NM VARCHAR(30) NOT NULL,
                        CUSTOMERID CHAR(5),
                        PHONENO CHAR(10),
                        BALANCE INT,
                       PIN INT)''')
myconn.commit()



# New account
def new_acc():
    name=input('ENTER ACCOUNT HOLDER\'S NAME :  ')
    phno=int(input('ENTER ACCOUNT HOLDER\'S PHONE NUMBER :  '))
    pin=int(input('ENTER PIN(4-DIGIT) : '))
    bal=int(input('Enter opening balance: '))
    accno=str(randint(10000000,99999999))
    cusid='SA'+str(accno[-4:-1])
    
    sql='INSERT INTO ATM VALUES("{}","{}","{}","{}",{},{})'.format(accno,name,cusid,phno,bal,pin)
    cursor.execute(sql)
    myconn.commit()
    sql='SELECT * FROM ATM WHERE ACCNO={}'.format(accno,)
    try:
        cursor.execute(sql)
        record=cursor.fetchall()
        for r in record:
            for i in r:
                print(i)
    except:
        myconn.rollback()
        
#Existing account
def acc(ID,pin):
    sql='SELECT * FROM ATM WHERE CUSTOMERID="{}" AND PIN={}'.format(ID,pin)
    try:
        cursor.execute(sql)
        rec=cursor.fetchall()
        if rec==[]:
            print('...........WRONG DATA ENTERED...........')
    except:
        myconn.rollback()
    return rec[0]

def deposit():
    amt=int(input("Enter the money to be deposited:"))
    cusid=input("Enter customer id: ")
    print("================================================================================")

    sql='update atm set balance=balance + {} where CUSTOMERID="{}"'.format(amt,cusid)
    cursor.execute(sql)
    myconn.commit()
    print("sucessfully deposited")

    
    
    
    
    
                              
    
                                    
    
    
def withdraw():
    amt=int(input("Enter the money to withdraw:"))
    cusid=input("Enter customer id: ")
    print("================================================================================")
    
    ah="select  BALANCE from atm where CUSTOMERID={}".format(cusid)
    cursor.execute(ah)
    m=cursor.fetchone()
    if amt<m[0]:
        sr="update atm set balance=balance - {}  where CUSTOMERID={}".format(amt,cusid)
        ed="update atm set balance ={} where CUSTOMERID={}".format(amt,cusid)
        cursor.execute(ed)
        cursor.execute(sr)
        myconn.commit()
        print("Sucessfully updated")
        

    else:
        
        print("Your are having less than",amt)
        print("Please try again")
        print("=====================================================")
    
    
    
    
def balance():
    cusid=input("Enter customer id: ")
    ma='select balance from atm where CUSTOMERID="{}"'.format(cusid)
    cursor.execute(ma)
    k=cursor.fetchone()
    print("Balance in your account=",k)
    print("================================================================================")


def upin():
    pin=int(input("Enter the pin: "))
    cusid=input("Enter customer id: ")
    print("================================================================================")

    sql='update atm set pin={} where CUSTOMERID="{}"'.format(pin,cusid)
    cursor.execute(sql)
    myconn.commit()
    print("PIn updated")
 
    
def upn():
    phn=int(input("Enter the new phone number: "))
    cusid=input("Enter customer id: ")
    print("================================================================================")

    sql='update atm set phoneno={} where CUSTOMERID="{}"'.format(phn,cusid)
    cursor.execute(sql)
    myconn.commit()
    print("Phone number updated")

    
def delete():
    cusid=input("Enter customer id: ")
    print("================================================================================")

    sql='delete from atm where CUSTOMERID="{}"'.format(cusid)
    cursor.execute(sql)
    myconn.commit()
    print("Record deleted")
    


def menu():
    while True:
        print('...........MENU...........')
        print('1. DEPOSIT AMOUNT')
        print('2. WITHDRAW AMOUNT')
        print('3. CHECK BALANCE')
        print('4. UPDATE PIN')
        print('5. UPDATE PHONE NUMBER')
        print('6. DELETE ACCOUNT')
        print('7. EXIT')
        ch=int(input('ENTER YOUR CHOICE:  '))
        if ch==1:
            deposit()
        elif ch==2:
            withdraw()
        elif ch==3:
            balance()
        elif ch==4:
            upin()
        elif ch==5:
            upn()
        elif ch==6:
            delete()
        else:
            break


def main():
    while True:
        print('...........TO LOGIN...........')
        print('1. NEW ACCOUNT')
        print('2. EXISTING ACCOUNT')
        print('3. EXIT')
        ch=int(input('ENTER YOUR CHOICE:  '))
        if ch==1:
            new_acc()
        elif ch==2:
            ID=input('ENTER CUSTOMER ID :  ')
            pin=int(input('ENTER PIN :  '))
            data=acc(ID,pin)
            menu()
        else:
            break

main()
