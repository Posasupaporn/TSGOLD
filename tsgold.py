import sqlite3
import sys

conn = sqlite3.connect(r'D:\ไพทอนอาจารย์หลิน\project\try02.db')
cursor = conn.cursor()

def menu():
    print('='*45)
    print("💰TSGOLD ONLINE💰".center(42))
    print('='*45)
    print("Main Menu ","\n","🔐 1.Login ","\n","🟢 2.Register ""\n","🔴 3.Exit ")

def choosemenu():
    global number1
    number1 = input("\n"+"Select Menu : ") #ทำการinput menu จาก def menu()
    

def n_ame(): #ขั้นตอนการสมัคร
    global r_name
    r_name = input("Name : ")
    if r_name.isalpha() == True: #ใช้ isalpha เพื่อให้กรอกได้เฉพาะตัวอักษร
        r_name
        sur_name()
    if r_name.isalpha() == False:
        print("◆Number aren't allowed 0-9◆")
        n_ame()

def sur_name():
    global r_lname
    r_lname = input("Surname : ")
    if r_lname.isalpha() == True:
        r_lname
        password()
    if r_lname.isalpha() == False:
        print("◆Number aren't allowed 0-9◆")
        sur_name()

    
def password():
    global r_line,r_user,r_pass
    r_line = input("ID Line : ")
    r_user = input("Username : ")
    while True:
        r_pass = input("Password : ")
        if len(r_pass) < 8: #ต้องกรอกให้ครบ 8 ตัว
            print("Invalid Code ✖")
            print("!!Make sure your password is at lest 8 letters!!")
        else:
            register()
            break

def register(): #ทำการเลือกว่าจะเป็นผู้ซื้อหรือผู้ขาย
    print("\n")
    print("Select Prefer 1.Store🛒 2.Buyers🤵")
    number2 = input("Select Menu 👉 ")
    if number2 == '1':
        weight()
    elif number2 == '2':
        registerbuyer()
    else:
        print("🕬Number isn't valid🕬")
        print("\n")
            
def weight(): #เมื่อเลือกเป็นผู้ขาย
    global h_weights
    h_weights = input("Gold Bar Weight : ")
    if h_weights.isdigit() == True: #ใช้ isdigit เพื่อให้กรอกเป็นตัวเลขเท่านั้น
        h_weights
        number()
    if h_weights.isdigit() == False:
        print("◆Number aren't allowed 0-9◆")
        weight()

def number():
    global h_number
    h_number = input("The amount of gold bars to sell : ")
    if h_number.isdigit() == True:
        h_number
        price()
    if h_number.isdigit() == False:
        print("◆Number aren't allowed 0-9◆")
        number()

def price():
    global h_price
    h_price = input("Price : ")
    if h_price.isdigit() == True:
        h_price
        registerseller()
    if h_price.isdigit() == False:
        print("◆Number aren't allowed 0-9◆")
        price()

def registerseller(): #เมื่อทำการกรอกทุกอย่างเรียบร้อยจะนำข้อมูลไปเก็บที่ sellergoldb
    sql = """INSERT INTO sellergoldb (name, lname, line, username, pass, weight, number, price) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}');""".format(r_name, r_lname, r_line, r_user, r_pass, h_weights, h_number, h_price)
    cursor.execute(sql)
    conn.commit()
    print("Successfully registered ✔")
    print("\n")

def registerbuyer(): #สมัครเป็นผู้ซื้อ
    data1 = """INSERT INTO buyergoldb (name, lname, line, username, pass) VALUES ('{}','{}','{}','{}','{}');""".format(r_name, r_lname, r_line, r_user, r_pass)
    cursor.execute(data1)
    conn.commit()
    print("Successfully registered ✔")
    print("\n")


def login(): #ขั้นตอนล็อกอิน
    global r_user1,r_pass1
    typeb = input("Status 1.Store🛒 2.Buyers🤵 : ")
    if typeb == '1':
        r_user1 = input("Username : ")
        r_pass1 = input("Password : ")
        cursor.execute(' SELECT * FROM sellergoldb WHERE username = ? AND pass = ? ',(r_user1, r_pass1)) #ไปเรียกข้อมูลของผู้ขายจาก sellergoldb ที่กรอก username กับ password ถูกต้อง
        row = cursor.fetchall()
        if row: #เมื่อทำการเช็คแล้วโปรแกรมจะส่งไปให้ editseller ทำงานต่อ
            print('-'*150)
            print("ID            Name         Surname           ID Line           Username             Password        Weight           Stock           Price")
            print('-'*150)
            for x in row:
                print('{:<14}{:<14}{:<14}{:<14}{:^24}{:^16}{:^16}{:^16}{:^16}'.format(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8]))
            editseller()
        else:
            print("\n","✖ Username or Password Incorrect ✖")
            choose1 = input("Select 1.Login กด 2.Main Menu : ")
            if choose1 == '1':
                login()
            else:
                print("\n")
    elif typeb == '2': #ขั้นตอนเข้าสู่ระบบของผู้ซื้อ
        r_user1 = input("Username : ")
        r_pass1 = input("Password : ")
        cursor.execute(' SELECT * FROM buyergoldb WHERE username = ? AND pass = ? ',(r_user1, r_pass1))
        row = cursor.fetchall()
        if row:
            print("\n","Select 1.List Of All Store  2.Edit Personal Information")
            choose = input("Select Menu 👉 ")
            if choose == '1':
                all()
            else:
                print('-'*100)
                print("ID             Name        Surname           ID Line           Username             Password")
                print('-'*100)
                for x in row:
                    print('{:<14}{:<14}{:<14}{:<14}{:^24}{:^16}'.format(x[0],x[1],x[2],x[3],x[4],x[5]))
                editbuyer()
        else:
            print("\n","✖ Username or Password Incorrect ✖")
            choose1 = input("Selct 1.Login  2.Main Menu : ")
            if choose1 == '1':
                login()
            else:
                print("\n")
    else:
        print("🕬Number isn't valid🕬")
        login()
    

def all(): #เมื่อกดหมายเลขคำสั่ง List Of All Store จะนำเอารายการของผู้ขายมาแสดง
    print("\n","List Of All Gold Sellers 🛒".center(80))
    print('-'*80)
    print("ID            Username               Weight               Stock      Price")
    print('-'*80)
    cursor.execute(' SELECT id,username,weight,number,price FROM sellergoldb')
    row1 = cursor.fetchall()
    for x in row1:
        print('{:<14}{:<14}{:^24}{:^16}{:>6}'.format(x[0],x[1],x[2],x[3],x[4]))
    order()

def order(): #ขั้นตอนการสั่งซื้อ
    global c2,c3,c4,things,c5
    c2 = []
    c3 = []
    c4 = []
    c5 = []
    things = input("\nNumber of stores you want to buy : ")
    for x in range(1,int(things)+1):
        product_s = str(input("ID Seller %d : "%x))
        u = input("Amont to buy : ")
        c2.append(product_s)
        c3.append(u)
    for i in c2:
        cursor.execute(' SELECT id FROM sellergoldb WHERE id = ? ',i)
        row = cursor.fetchone()
        if row:
            row
        else:
            print("\n","✖ ID Seller incorrect ✖") #ตรวจสอบไอดีร้านที่ลูกค้ากรอกว่ามีในระบบหรือไม่
            print("Please try again","\n")
            all()
    for i in c2:
        cursor.execute(' SELECT number FROM sellergoldb WHERE id = ? ',i)
        result = cursor.fetchall()
        for x in result:
            c5.append(x[0])
    for num1, num2 in zip(c5, c3):
        v = int(num1) - int(num2)
        if v > 0:
            v
        elif v == 0:
            v
        else:
            print("\n","✖ Amont to by incorrect ✖") #ตรวจสอบว่าจำนวนทองคำที่ลูกค้ากรอกลงไม่เกินจำนวนที่ร้านค้ามี
            print("Please try again","\n")
            all()
    print("\n","Items your picked 🛒".center(80))
    print('-'*85)
    print("username                            Weight                                Price")
    print('-'*85)
    for i in c2:
        cursor.execute(' SELECT username,weight,price FROM sellergoldb WHERE id = ? ',i)
        result = cursor.fetchall()
        for x in result:
            print('{:<14}{:^50}{:>15}'.format(x[0],x[1],x[2]))
            c4.append(x[2])
    total()

def total(): #ขั้นตอนการรวมเงิน
    global sum1
    pp = []
    for num1, num2 in zip(c3, c4):
        pp.append(int(num1) * int(num2))
    sum1 = 0
    for num3 in pp:
        sum1 = int(sum1) + int(num3)
    sum2 = 0
    for num4 in c3:
        sum2 = int(sum2) + int(num4)
    print("Total orders",sum2,"Stick Total Money",sum1,"Bath")
    confirm()
    
def confirm(): #ขั้นตอนกดยืนยันการสั่งซื้อ
    print("\n")
    conf = input("Confirm Orders(y/n) :")
    if conf == 'y':
        print("Fill in the address📍")
        address1 = input("Address : ")
        data4 = """INSERT INTO databuyer1 (username,totalprice,address) VALUES ('{}','{}','{}');""".format(r_user1, sum1, address1)
        cursor.execute(data4)
        conn.commit()
        for num1,num2 in zip(c2,c3):
            data2 = """INSERT INTO databuyer (username,idseller,number) VALUES ('{}','{}','{}');""".format(r_user1, num1, num2)
            cursor.execute(data2)
            conn.commit()
        deletestock()
        print("Finished the Orders ✔")
        print("\n")
        last()
    else:
        last()

def deletestock(): #ลบสต็อกเมื่อผู้ซื้อทำการยืนยันคำสั่งซื้อ
    p = []
    for num1, num2 in zip(c5, c3):
        p.append(int(num1) - int(num2))
    for x in range(1,int(things)+1):
        x
        for num,num3 in zip(p,c2):
            cursor.execute(""" UPDATE sellergoldb SET number = ? WHERE id = ? """,(num,num3))
            conn.commit()

def last(): #เมื่อทำการยืนยันหรือไม่ยืนยันคำสั่งซื้อจะเข้าสู่เมนูทางเลือก
    while True:
        print("\n","Select 1.List Of All Gold Sellers 2.Edit Personal Information  3.Exited the program")
        choose = input("Select Menu 👉 ")
        if choose == '1':
            print("\n")
            all()
        elif choose == '2':
            print("\n")
            editbuyer()
        elif choose == '3':
            print("\n")
            print("Exited the program successfully")
            print("Thank You! ☺")
            sys.exit()

def editseller(): #ขั้นตอนการแก้ไขข้อมูลของผู้ขาย
    print("\n","Edit Lists 🔁","\n","1.Name              5.password","\n","2.Surname           6.Glod Bar Weight","\n","3.id line           7.Amont of Glod Bar","\n","4.username          8.Price")
    edit1 = input("Select Edit Lists 👉 ")
    try:
        if edit1 == '1':
            name = input('Name : ')
            cursor.execute(""" UPDATE sellergoldb SET name = ? WHERE username = ? """,(name,r_user1))
            conn.commit()
            List1()
        elif edit1 == '2':
            surname = input('Surname : ')
            cursor.execute(""" UPDATE sellergoldb SET lname = ? WHERE username = ? """,(surname,r_user1))
            conn.commit()
            List1()
        elif edit1 == '3':
            line = input('ID Line : ')
            cursor.execute(""" UPDATE sellergoldb SET line = ? WHERE username = ? """,(line,r_user1))
            conn.commit()
            List1()
        elif edit1 == '4':
            username1 = input('Username : ')
            cursor.execute(""" UPDATE sellergoldb SET username = ? WHERE username = ? """,(username1,r_user1))
            conn.commit()
            List1()
        elif edit1 == '5':
            password = input('Password : ')
            cursor.execute(""" UPDATE sellergoldb SET pass = ? WHERE username = ? """,(password,r_user1))
            conn.commit()
            List1()
        elif edit1 == '6':
            weight = input('Glod Bar Weight : ')
            cursor.execute(""" UPDATE sellergoldb SET weight = ? WHERE username = ? """,(weight,r_user1))
            conn.commit()
            List1()
        elif edit1 == '7':
            num1 = input('Amont of Glod Bar : ')
            cursor.execute(""" UPDATE sellergoldb SET number = ? WHERE username = ? """,(num1,r_user1))
            conn.commit()
            List1()
        elif edit1 == '8':
            price = input('Price : ')
            cursor.execute(""" UPDATE sellergoldb SET price = ? WHERE username = ? """,(price,r_user1))
            conn.commit()
            List1()
        else:
            print("!!Number isn't valid!!") #เมื่อกรอกหมายเลขนอกเหนือจากคำสั่งกำหนด
            print("►Please enter number again◄")
            editseller()
    except sqlite3.Error as e :
        print (e)

def List1() : #แสดงตารางอัพเดตข้อมูลผู้ขาย
    print('-'*150)
    print("ID            Name         Surname           ID Line           Username             Password        Weight           Stock           Price")
    print('-'*150)
    cursor.execute(' SELECT * FROM sellergoldb WHERE username = ? AND pass = ? ',(r_user1, r_pass1))
    row1 = cursor.fetchall()
    for x in row1:
        print('{:<14}{:<14}{:<14}{:<14}{:^24}{:^16}{:^16}{:^16}{:^16}'.format(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8]))
    print("\n","Successfully registered ✔")
    print("\n","Select 1.Edit Personal Information Again  2.Main Menu")
    choose = input("Select Menu 👉 ")
    if choose == '1':
        print("\n")
        editseller()
    else:
        print("\n")

def editbuyer(): #แก้ไขข้อมูลผู้ซื้อ
    print("\n","Edit Lists 🔁","\n","1.Name              4.username","\n","2.Surname           5.password","\n","3.id line")
    edit1 = input("Select Edit Lists 👉 ")
    try:
        if edit1 == '1':
            name = input('Name : ')
            cursor.execute(""" UPDATE buyergoldb SET name = ? WHERE username = ? """,(name,r_user1))
            conn.commit()
            Lists() 
        elif edit1 == '2':
            surname = input('Surname : ')
            cursor.execute(""" UPDATE buyergoldb SET lname = ? WHERE username = ? """,(surname,r_user1))
            conn.commit()
            Lists() 
        elif edit1 == '3':
            line = input('ID Line : ')
            cursor.execute(""" UPDATE buyergoldb SET line = ? WHERE username = ? """,(line,r_user1))
            conn.commit()
            Lists() 
        elif edit1 == '4':
            username1 = input('Username : ')
            cursor.execute(""" UPDATE buyergoldb SET username = ? WHERE username = ? """,(username1,r_user1))
            conn.commit()
            Lists() 
        elif edit1 == '5':
            password = input('Password : ')
            cursor.execute(""" UPDATE buyergoldb SET pass = ? WHERE username = ? """,(password,r_user1))
            conn.commit()
            Lists() 
        else:
            print("!!Number isn't valid!!")
            print("►Please enter number again◄")
            editbuyer ()
    except sqlite3.Error as e :
        print (e)

def Lists () : #แสดงตารางอัพเดตข้อมูลผู้ซื้อ
    print('-'*100)
    print("ID             name        Surname           ID Line            Username            Password")
    print('-'*100)
    cursor.execute(' SELECT * FROM buyergoldb WHERE username = ? AND pass = ? ',(r_user1, r_pass1))
    row1 = cursor.fetchall()
    for x in row1:
        print('{:<14}{:<14}{:<14}{:<14}{:^24}{:^16}'.format(x[0],x[1],x[2],x[3],x[4],x[5]))
    print("\n","Successfully registered ✔")
    last()

while True:
    menu()
    choosemenu() 
    if number1 == '1': 
        login()
    elif number1 == '2':
        n_ame()
    else:
        exit1 = input("Want to exit the program (y/n) : ")
        if exit1 == 'n':
            print("\n")
        else:
            print("Exited the program successfully")
            print("Thank You! ☺")
            break