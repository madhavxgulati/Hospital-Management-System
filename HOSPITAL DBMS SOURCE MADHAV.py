#importing mysql.connector
import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="abc123")

mycursor=mydb.cursor()
#creating database and related tables necessary

mycursor.execute("create database if not exists newlifehospital")
mycursor.execute("use newlifehospital")
mycursor.execute("create table if not exists doctor (Doctor_ID varchar(20) primary key, Doctors_First_Name varchar(20), Doctors_Last_Name varchar(20), Gender varchar(20), Age int, Specialization_Of_Doctor varchar(20), College varchar(20), marks int, Date_Of_Joining date, Success int, Fail int)")


mycursor.execute("create table if not exists patient(Patient_ID varchar(20) primary key, Patients_First_Name varchar(20), Patients_Last_Name varchar(20), Patient_Age int,DOB date,Doctor_ID varchar(20),Foreign key (Doctor_ID) references doctor(Doctor_ID)ON DELETE CASCADE ON UPDATE CASCADE,Gender varchar(20),Disease varchar(20), Phone varchar(20))")
mycursor.execute("Create table if not exists room(Room_No int primary key, Patient_ID varchar(20),Foreign key (Patient_ID) references patient (Patient_ID) ON DELETE CASCADE ON UPDATE CASCADE, Type_Of_Room varchar(20),Cost_Per_Day int)")
mycursor.execute("Create table if not exists in_patient(Patient_ID varchar(20),Foreign key (Patient_ID) references patient (Patient_ID) ON DELETE CASCADE ON UPDATE CASCADE, Date_Of_Adm date,Date_Of_Dis date,No_Of_Days_Adm int)")
mycursor.execute("create table if not exists bill(Bill_No varchar(20) primary key,Patient_ID varchar(20),Foreign key (Patient_ID) references patient (Patient_ID) ON DELETE CASCADE ON UPDATE CASCADE, Doctor_ID varchar(20),Foreign key (Doctor_ID) references doctor (Doctor_ID) ON DELETE CASCADE ON UPDATE CASCADE, No_Of_Days_Adm int, Total_Cost int,Cost_Per_Day int)")                     
mycursor.execute("create table if not exists out_patient(Patient_ID varchar(20),Foreign key (Patient_ID) references patient (Patient_ID) ON DELETE CASCADE ON UPDATE CASCADE,Patients_First_Name varchar(20), Surgery_No varchar(20) primary key, Bill_No varchar(20), Foreign key (Bill_No) references bill (Bill_No) ON DELETE CASCADE ON UPDATE CASCADE,Status_Of_Treatment varchar(20), Date_Of_Surgery date)")
mycursor.execute("create table if not exists userid(username varchar(20), password varchar(20))")
sqlbeforestart="select*from doctor"
mycursor.execute(sqlbeforestart)
myresultbefore=mycursor.fetchall()
if myresultbefore==[]:
    
    sqlstart="insert into doctor values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    valstart=("8KQW2E","Rohan","Jain","male","45","Cardiologist","AIIMS",92,"2010-11-19" , 123 , 48)
    mycursor.execute(sqlstart,valstart)
    mydb.commit()
#login page code
q=0
while(q==0):
    print("""
            ================================================================
             
                            WELCOME TO NEWLIFE HOSPITALS PVT. LTD. 

            ================================================================
    """)
    
    print("\n")

    print("\t\t\tLOGIN PAGE")
    print("\n1.SIGN UP IF YOU ARE NEW")
    print("\n2.LOGIN IF YOU ARE ALREADY REGISTERED")
    w=int(input("enter choice: "))
    if (w==1):
        username=input("ENTER USERNAME: (password should be atleast 6 characters long and containing atleast 1 numeric character)")
        if len(str(username))>=6 and username.isalnum()==True:
            sql="select * from userid where username = %s"
            val=username
            mycursor.execute(sql,(val,))
            myresult=mycursor.fetchall()
            if myresult==[]:
                print("username is available and registered. Please proceed to set password")
                password=input("ENTER PASSWORD: please select a strong password and dont share it with anyone")
                val1=(username,password)
                sql="insert into userid values(%s,%s)"
                mycursor.execute(sql,val1)
                mydb.commit()
                print("YOU HAVE BEEN REGISTERED. WELCOME.")
                
                
            else:
                print("username already registered. Please set a new username or login again if you are already registered")
                continue
        else:
            print("Username is not atleast 6 characters long. Please try again.")
            continue
            
            
        
    if (w==2):
        username1=input("ENTER USERNAME: ")
        password1=input("ENTER PASSWORD: ")
        if len(str(username1))>=6 and username1.isalnum()==True:
            print("Searching for your username...")
            sql="select password from userid where username= %s "
            val=username1
            mycursor.execute(sql,(val,))
            myresult=mycursor.fetchall()
            if myresult==[]:
                print("Username does not exist")
            elif myresult[0][0]==password1:
                print("Username and password match. Welcome")
                break
            else:
                print("Wrong password. try again")
        else:
            print("Please enter a valid username")
            continue


#MAIN MENU-------------
k=0
while(k==0):
    print(" ")
    print("MENU")
    print(" ")
    print("1.Patient Details")
    print("2.Calculate bill")
    print("3.Update or delete my records")
    print("4.Request my report")
    print("5.open doctors' details")
    print("6.Exit")
    print()

    ch=int(input("Enter choice: "))
    if (ch==6):
        print("""
            ================================================================
             
                            WELCOME TO NEWLIFE HOSPITALS PVT. LTD. 

            ================================================================
        """)
    
        print("\n")
        print("Thank you, for choosing our services. Come back soon and dont forget to leave us your valuable feedback")
        print("\n\n")
        k=1
    if (ch==1):
        print("\t\t\t WELCOME TO PATIENT DATABASE")
        try:
            firstname=str(input("Enter Patient's first name:"))
            lastname=str(input("enter patient's last name: "))
            patientage=int(input("enter patient's age: "))
            if firstname.isalpha()==True and lastname.isalpha()==True and type(patientage)==int:
                gender=str(input("Gender of Patient:"))
                if gender.lower()=='male' or gender.lower()=='female' or gender.lower()=='other':
                    print("Now, please state the reason of your discomfort or name of the disease you're suffering from:")
                else:
                    print("ENTER VALID GENDER")
                    print("choose any one gender (male/female/other)")
                    continue
        except:
            print("Name should not contain numbers and Age should not contain alphabets")
            continue
        genderf=gender.lower()
        disease=str((input("disease:")))
        print("Great! Now we will be assigning you your Patient ID and the ID of the doctor assigned to you")
        import string
        import random
        def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
            return ''.join(random.choice(chars) for _ in range(size))
        print("Your PatientID")
        patientid=id_generator()
        print(patientid)
        print("remember it")
        print("DoctorID")
        sql="select Doctor_ID from doctor"
        mycursor.execute(sql,)
        myresult=mycursor.fetchall()
        import random
        doctorid=random.choice(myresult)
        doctorid1 =  ''.join(doctorid)
        print(doctorid1)
        print("remember it")
        var=0
        while (var==0):
            ph=(input("Phone no.: "))
            pho=str(ph)
            if ('1','2','3','4','5','6','7','8','9','0' in pho) and len(pho)==10:
                break
            else:
                print("Invalid phone no.")
                print("Enter again")
                continue
        print(" patient's DOB")
        y=int(input("Enter year (YYYY): "))
        m=int(input("Enter month (MM): "))
        d=int(input("Enter date (DD): "))
        year=str(y)
        month=str(m)
        da=str(d)
        br='-'
        date=year+br+month+br+da
        if (d<=31) and (m<=12) and (m>0) and (d>0) and (y>0):
            if (m==4,6,9,11):
                if (d==31):
                    print("Invalid date")
                    print("Enter again")
                    continue
                else:
                    pass
            if (y%4==0) and (m==2):
                if (d==30,31):
                    print("Invalid date")
                    print("Enter again")
                    continue
                else:
                    pass
            if (y%4!=0) and (m==2):
                if (d==29) or (d==30) or (d==31):
                    print("Invalid date")
                    print("Enter again")
                    continue
                else:
                    pass
        else:
            print("invalid date")
            continue
        date1=date
        #inserting into patient table
        sql=("insert into patient values(%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        val=(patientid,firstname,lastname,patientage,date1,doctorid1,genderf,disease,ph)
        mycursor.execute(sql,val)
        mydb.commit()
        print("Now, please select which type of room you desire:")
        print("ROOMS")
        print("1. General ward")
        print("2. Semi private room")
        print("3. Private room")
        print("4. Suite")

        x=0
        roomchoice=int(input("enter your choice"))
        while (x==0):
                
            if roomchoice==1:
                typeofroom="General ward"
                costperday=12000
                x=1
            elif roomchoice==2:
                typeofroom="Semi private room"
                costperday=16000
                x=1
            elif roomchoice==3:
                typeofroom="Private room"
                costperday=18000
                x=1
            elif roomchoice==4:
                x=1
                typeofroom="Suite"
                costperday=21000
            else:
                print("invalid. try again")
                continue
        print("your room is",typeofroom,"and cost per day is", costperday)
        import string
        import random
        def id_generator2(size=3, chars=string.digits):
                return ''.join(random.choice(chars) for _ in range(size))
        
        roomno=id_generator2()
        print("your room number is",roomno)
        #INSERTING INTO TABLE ROOM
        sql="insert into room values(%s,%s,%s,%s)"
        val=(roomno,patientid,typeofroom,costperday)
        mycursor.execute(sql,val)
        mydb.commit()
        print("\n\nYour details have been inserted successfully")

        
    if (ch==2):
        #PAYMENT OF BILL
        j=str(input("enter your patientid: "))
        sql="select Patients_First_Name, Doctor_ID from patient where Patient_ID = %s"
        val=j
        sqlh="select*from bill where Patient_ID=%s"
        val=j
        mycursor.execute(sqlh,(val,))
        myresult6=mycursor.fetchall()
        #VALIDATION OF ALREADY PAYING THE BILL
        if myresult6!=[]:
            print("\nOUR RECORDS SHOW THAT YOU HAVE ALREADY PAID THE BILL, DIRECTING TO MAIN MENU..")
            pass
            continue
        else:
            
            mycursor.execute(sql,(val,))
            myresult=mycursor.fetchall()
            u=str(myresult[0][1])
            print("Is your first name", str(myresult[0][0]),"?")
            confirm=str(input("type Y for yes and N for no: "))
            if confirm.lower()=="n":
                print("We cant find your name")
                break
            else:
                print("when did you get admitted?")
                print("date of admission")
                y1=int(input("Enter year (YYYY): "))
                m1=int(input("Enter month (MM): "))
                d1=int(input("Enter date (DD): "))
                year1=str(y1)
                month1=str(m1)
                da1=str(d1)
                br='-'
                date1=year1+br+month1+br+da1
                if (d1<=31) and (m1<=12) and (m1>0) and (d1>0) and (y1>0):
                    if (m1==4,6,9,11):
                        if (d1==31):
                            print("Invalid date")
                            print("Enter again")
                            continue
                        
                    if (y1%4==0) and (m1==2):
                        if (d1==30,31):
                            print("Invalid date")
                            print("Enter again")
                            continue
                        
                    if (y1%4!=0) and (m1==2):
                        if (d1==29) or (d1==30) or (d1==31):
                            print("Invalid date")
                            print("Enter again")
                            continue
                    
                print("When are you getting discharged?")
                print("date of discharge")
                y2=int(input("Enter year (YYYY): "))
                m2=int(input("Enter month (MM): "))
                d2=int(input("Enter date (DD): "))
                year2=str(y2)
                month2=str(m2)
                da2=str(d2)
                br='-'
                date2=year2+br+month2+br+da2
                if (d2<=31) and (m2<=12) and (m2>0) and (d2>0) and (y2>0):
                    if (m2==4,6,9,11):
                        if (d2==31):
                            print("Invalid date")
                            print("Enter again")
                            continue
                        
                    if (y2%4==0) and (m2==2):
                        if (d2==30,31):
                            print("Invalid date")
                            print("Enter again")
                            continue
                        
                    if (y2%4!=0) and (m2==2):
                        if (d2==29) or (d2==30) or (d2==31):
                            print("Invalid date")
                            print("Enter again")
                            continue
                    print("Date of admission",date1)
                    print("Date of discharge",date2)
                    from datetime import date
                    f_date = date(y1, m1, d1)
                    l_date = date(y2, m2, d2)
                    delta = l_date - f_date
                    daysadm=(delta.days)
                    #VALIDATION OF DATE OF ADMISSION AND DISCHARGE
                    if daysadm<0:
                        print("INVALID DATE. TRY AGAIN")
                        continue
                    if date1==date2:
                        daysadm=1
                        print("Number of days of treatment", daysadm)
                    else:
                        
                        print("Number of days of treatment",daysadm)
                #INSERT INTO IN_PATIENT VALUES
                sql="insert into in_patient values (%s,%s,%s,%s)"
                val=(j,date1,date2,daysadm)
                mycursor.execute(sql,val)
                mydb.commit()
                sql="select Type_Of_Room, Cost_Per_Day from room where Patient_ID = %s"
                val=j
                mycursor.execute(sql,(val,))
                myresult1=mycursor.fetchall()
                print("Are the following details","\n Type of room: ",str(myresult1[0][0]),"\n Cost per Day: ",str(myresult1[0][1]),"\n correct? Do you wish to proceed")
                confirm=str(input("type Y for yes and N for no: "))
                if confirm.lower()=="n":
                    print("Something went wrong. try again")
                    break

                else:
                    type1=myresult1[0][0]
                    costperday=myresult1[0][1]
                    totalcost=costperday*daysadm
                    print("Total cost for your treatment",str(myresult[0][0]),"is",totalcost)
                    sql="select Disease from patient where Patient_ID = %s"
                    val=j
                    mycursor.execute(sql,(val,))
                    myresult2=mycursor.fetchall()
                    import string
                    import random
                    def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
                        return ''.join(random.choice(chars) for _ in range(size))
                    billno=id_generator()
                    #INSERTING INFO IN BILL
                    sql="insert into bill values (%s,%s,%s,%s,%s,%s)"
                    val=(billno,j,u,daysadm,totalcost,costperday)
                    mycursor.execute(sql,val)
                    mydb.commit()
                    print("\n\nYour details have been inserted successfully")
                    print("Your billno is",billno,"do you wish to see the bill now?")
                    confirm2=str(input("type Y for yes and N for no"))
                    filename= "%s.txt" % billno
                    file=open(filename,"w")
                    file.writelines(["\t\t\t HOSPITAL MANAGEMENT SYSTEM\n\nPatient's Name: ",str(myresult[0][0]),"\n","Patient ID: ",j,"\n","Disease: ",str(myresult2[0]),"\n"])
                    file.writelines(["Date Of Admission: ",date1,"\n","Date of Discharge: ",date2,"\n","Number of days of treatment: ",str(daysadm),"\n","Type of room: ",str(myresult1[0][0]),"\n"])
                    file.writelines(["Cost per day of room: ",str(myresult1[0][1]),"\n","\n","TOTAL COST: ",str(totalcost)])
                    file.close()
                    if confirm2.lower()=="y":
                        print("your bill will be generated shortly. Thank you")
                        file=open(filename,"r")
                        print(file.read())
                        print("file has been saved to your system with the name",filename)
                        print("\n YOUR ROOM IS NOW READY TO BE VACATED AND CLEANED FOR THE NEXT PATIENT.")
                        print("\n\n THANK YOU FOR CHOOSING OUR FACILITIES FOR YOUR TREATMENT. WE HOPE THAT OUR SERVICES PROVIDED TO YOU WERE SATISFACTORY")
                        print("\n Have a nice day, please dont forget to leave your feedback!")
                        sqlz="delete from room where Patient_ID=%s"
                        valz=j
                        mycursor.execute(sqlz,(valz,))
                        mydb.commit()
                    elif confirm2.lower()=="n":
                        print("bill is being downloaded")
                        print("download complete")
                        print("file has been saved to your system with the name",filename)
                        print("\n YOUR ROOM IS NOW READY TO BE VACATED AND CLEANED FOR THE NEXT PATIENT.")
                        print("\n\n THANK YOU FOR CHOOSING OUR FACILITIES FOR YOUR TREATMENT. WE HOPE THAT OUR SERVICES PROVIDED TO YOU WERE SATISFACTORY")
                        print("\n Have a nice day, please dont forget to leave your feedback!")
                        sqlz="delete from room where Patient_ID=%s"
                        valz=j
                        mycursor.execute(sqlz,(valz,))
                        mydb.commit()
                    else:
                        print("enter valid input")
                        break
    if (ch==5):
        print("\t\t\t WELCOME TO DOCTOR DATABASE")
        print("\n\n THESE DETAILS CAN ONLY BE PRIVY TO ADMIN STAFF OF THIS HOSPITAL")
        print("\n\n choose from the following: ")
        print("\n 1. Operation details")
        print("\n 2. Register as a doctor")
        print("\n 3. Back to Main Menu")
        o=int(input("Enter your choice :"))
        if (o==2):
            #REGISTERING AS A DOCTOR
            print("We will require some of your academic qualifications and personal details before assigning you this job, ")
            dfirstname=str(input("Enter candidate's first name:"))
            dlastname=str(input("enter candidate's last name: "))
            dage=int(input("enter candidate's age: "))
            dgender=str(input("Gender of candidate :"))
            college=str(input("enter the institute from where you achieved MBBS degree: "))
            marks=int(input("enter your marks scored in college: "))
            if dgender.lower()=='male' or dgender.lower()=='female' or dgender.lower()=='other':
                print("Now, please choose your area of expertise : ")
                print("1. Cardiologist")
                print("2. Dermatologist")
                print("3. Surgeon")
                print("4. Gynecologist")
                print("5. Orthodontist")
                print("6. Other")
                x=int(input("enter your choice: "))
                if x==1:
                    spec="Cardiologist"
                elif x==2:
                    spec="Dermatologist"
                elif x==3:
                    spec="Surgeon"
                elif x==4:
                    spec="Gynecologist"
                elif x==5:
                    spec="Orthodontist"
                elif x==6:
                    spec="other"
                else:
                    print("INVALID CHOICE")
                    break
                
            else:
                break
            doctordisease=print("Are you suffering from any major disease? (Y/N) ")
            v=str(input("choice: "))
            #EVALUATION OF INFO ENTERED
            print("Great! Now we will be evaluating your information and reviewing your application")
            if marks<=85 or dage>=55 or dage<=25 or v.lower()=='y':
                print("YOUR APPLICATION WAS REVIEWED. WE REGRET TO INFORM YOU THAT DUE TO SOME CONCERNS, YOU HAVE NOT BEEN ASSIGNED THE JOB.")
                print("This might be due to the follwing reasons: ")
                print("1. Your age should be between 25 and 55")
                print("2. You should not be having any major diseases")
                print("3. Your academic qualifications should be adequate (>85%)")
                continue     
            else:
                print("YOUR CANDIDANCY WAS CONSIDERED AND WE ARE GLAD TO INFORM YOU THAT YOU ARE GIVEN THE JOB. WELCOME ABOARD!")
                print("\n\n When would you like to start?")
                print("DATE OF JOINING")
                from datetime import date
                today= date.today()
                y3=int(input("Enter year (YYYY): "))
                m3=int(input("Enter month (MM): "))
                d3=int(input("Enter date (DD): "))
                try:
                    from datetime import date
                    global date3
                    date3 = date(y3,m3,d3)
                    print("Entered date of joining", date3)
                    from datetime import date
                    difference= date3-today
                    diff=difference.days
                    if diff<0 :
                        print("INVALID DATE. TRY AGAIN")
                        continue
                    else:
                        print("YOU CAN START WORKING FROM", date3,"!!")
                        print("\n\n NOW YOU WILL BE ASSIGNED YOUR UNIQUE DOCTOR ID. AVOID SHARING IT WITH ANYONE.")
                        import string
                        import random
                        def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
                            return ''.join(random.choice(chars) for _ in range(size))
                        doctorid=id_generator()
                        print(doctorid)
                        #INSERTING INTO DOCTOR
                        sql="insert into doctor values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                        val=(doctorid,dfirstname,dlastname,dgender,dage,spec,college,marks,date3,0,0)
                        mycursor.execute(sql,val)
                        mydb.commit()
                        print("YOUR DETAILS ARE RECORDED")

                except:
                    print("value error")
                    continue       
                
                
                
        if (o==1):
            print("\t\t\t OPERATION DETAILS")
            doctorid=str(input("Enter your doctorid: "))
            #ADDING OPERATION DETAILS
            sql="select Doctors_First_Name, Doctors_Last_Name from doctor where Doctor_ID = %s"
            val=doctorid
            mycursor.execute(sql,(val,))
            myresult=mycursor.fetchall()
            print("Welcome, ",myresult[0][0],myresult[0][1])
            print("\ninput the patient id of the patient under observation")
            patientid=str(input("Enter the patient id: "))
            sqlbef="select*from in_patient where Patient_ID=%s"
            valbef=patientid
            mycursor.execute(sqlbef,(valbef,))
            myresultbef=mycursor.fetchall()
            if myresultbef==[]:
                print("Please pay bill first as the system will need the date of admission and date of discharge")
                print("You will be directed to the main menu..")
                continue
            sql1="select Patients_First_Name, Patients_Last_Name,Disease,Gender, Patient_Age from patient where Patient_ID = %s"
            val1=patientid
            mycursor.execute(sql1,(val1,))
            myresult1=mycursor.fetchall()
            print("\n Patient's Name: ",myresult1[0][0],myresult1[0][1])
            print("\n Gender: ",myresult1[0][3],"\n Age: ",myresult1[0][4],"\n Patient's Disease: ",myresult1[0][2])
            conf=str(input("\n\n DO YOU CONFIRM THESE DETAILS AND WANT TO PROCEED? (Y/N): "))
            if conf.lower()=="n":
                print("You will be directed to the main menu..")
                continue
            elif conf.lower()=="y":
                import string
                import random
                def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
                    return ''.join(random.choice(chars) for _ in range(size))
                surgeryno=id_generator()
                print("surgery number is," ,surgeryno)
                print("Now, please enter the date of this operation")
                
                def surgery():
                            
                    ye=int(input("Enter the year of operation"))
                    mo=int(input("Enter the month of operation"))
                    da=int(input("Enter the date of operation"))
                    try:
                        from datetime import date
                        global dateofsurgery
                        dateofsurgery = date(ye,mo,da)
                        print("Entered date of surgery", dateofsurgery)
                        j=1
                    except:
                        print("value error")
                        surgery()

                    sql="select Date_Of_Adm, Date_Of_Dis from in_patient where Patient_ID=%s"
                    val=patientid
                    mycursor.execute(sql,(val,))
                    myresult8=mycursor.fetchall()
                
                    dateofadm=myresult8[0][0]
                    dateofdis=myresult8[0][1]
                    if dateofadm > dateofsurgery or dateofsurgery > dateofdis:
                        
                        print("Date of surgery is invalid. Date of surgery should be between date of admission and discharge of the patient")
                        print("date of admission", dateofadm)
                        print("date of discharge", dateofdis)
                        
                        surgery()
                    else:
                        j=1
                surgery()
                #CHOOSING STATUS OF PATIENT
                print("Now, please input the details of this operation")
                print("\n\n Select one of the options which best suited to the operation status")
                print("1. Operation successful, patient can be discharged at will")
                print("2. Operation successful, patient still needs to be under hospital care due to complications which may arise")
                print("3. Operation not successful, patient should be kept under special care.")
                print("4. Operation not successful, patient could not be saved.")
                stat=int(input("\n Enter most viable option: "))
                #VALIDATION OF NOT PAYING THE BILL
                sql3="select Bill_No from bill where Patient_ID=%s"
                mycursor.execute(sql3,(val1,))
                myresult3=mycursor.fetchall()
                if myresult3==[]:
                    print("please pay the bill first")
                    continue
                else:
                    billno=myresult3[0][0]
                patientfname=myresult1[0][0]
                if stat==1:
                    status="success, alive"
                    sql2="update doctor set Success=Success+1 where Doctor_ID=%s"
                    val2=doctorid
                    mycursor.execute(sql2,(val2,))
                    mydb.commit()
                    
                elif stat==2:
                    status="success, stable"
                    sql2="update doctor set Success=Success+1 where Doctor_ID=%s"
                    val2=doctorid
                    mycursor.execute(sql2,(val2,))
                    mydb.commit()
                elif stat==3:
                    status="fail, critical"
                    sql2="update doctor set Fail=Fail+1 where Doctor_ID=%s"
                    val2=doctorid
                    mycursor.execute(sql2,(val2,))
                    mydb.commit()
                elif stat==4:
                    status="fail, dead"
                    sql2="update doctor set Fail=Fail+1 where Doctor_ID=%s"
                    val2=doctorid
                    mycursor.execute(sql2,(val2,))
                    mydb.commit()
                else:
                    print("INVALID INPUT")
                sql4="insert into out_patient values(%s,%s,%s,%s,%s,%s)"
                values=(patientid,patientfname,surgeryno,billno,status,dateofsurgery)
                mycursor.execute(sql4,values)
                mydb.commit()
                print("\nOPERATION DETAILS INSERTED SUCCESSFULLY.")
                
            else:
                print("INVALID INPUT")
        if (o==3):
            print("Directing to main page")
            continue
    if (ch==3):
        print("\t\t UPDATION AND DELETION OF RECORDS")
        print("\n\n Are you a patient or a doctor?")
        print("1. DOCTOR")
        print("2. PATIENT")
        yus=int(input("enter your choice: "))
        if (yus==1):
            print("\n\nPlease enter your doctor id for authentication")
            auth=str(input("Doctor id: "))
            sql="select Doctors_First_Name, Doctors_Last_Name from doctor where Doctor_ID=%s"
            val=(auth)
            mycursor.execute(sql,(val,))
            myresult0=mycursor.fetchall()
            
            if myresult0==[]:
                print("Your details are not to be found in the database. Please try again")
                continue
            else:
                print("Welcome ", myresult0[0][0], myresult0[0][1], "!!")
                print("\n\nDo you wish to: \n 1. UPDATE RECORDS\n 2. DELETE RECORDS\n Please select 1 or 2")
                h=int(input())
                if (h==1):
                    print("\n\nHere are some of the details you can edit:")
                    print("1. Your specialisation")
                    print("2. Your age")
                    print("3. Date of a particular surgery")
                    print("4. Status of treatment of patient")
                    print("5. Back to previous page")
                    l=int(input())
                    if (l==1):
                        print("Now, please choose your new area of expertise : ")
                        print("1. Cardiologist")
                        print("2. Dermatologist")
                        print("3. Surgeon")
                        print("4. Gynecologist")
                        print("5. Orthodontist")
                        print("6. Other")
                        x=int(input("enter your choice: "))
                        if x==1:
                            spec="Cardiologist"
                        elif x==2:
                            spec="Dermatologist"
                        elif x==3:
                            spec="Surgeon"
                        elif x==4:
                            spec="Gynecologist"
                        elif x==5:
                            spec="Orthodontist"
                        elif x==6:
                            spec="other"
                        else:
                            print("INVALID CHOICE")
                            break
                        sql="update doctor set Specialization_Of_Doctor=%s where Doctor_ID=%s"
                        val=(spec,auth)
                        mycursor.execute(sql,val)
                        mydb.commit()
                        print("Your new specialization registered in the database is", spec)
                    elif (l==2):
                        newage=int(input("Please enter your age: "))
                        sql="update doctor set Age=%s where Doctor_ID=%s"
                        val=(newage,auth)
                        mycursor.execute(sql,val)
                        mydb.commit()
                        print("Your new age registered in the database is", newage)
                    elif (l==3):
                        surgeryno=str(input("Enter the surgery number provided during the surgery"))
                        sql="select Date_Of_Surgery, Patient_ID, Patients_First_Name from out_patient where exists(select Bill_No from out_patient where Surgery_No=%s)"
                        val=surgeryno
                        
                        mycursor.execute(sql,(val,))
                        myresult9=mycursor.fetchall()
                        if myresult9==[]:
                            print("value error")
                        else:
                            patientid=myresult9[0][1]
                            original=myresult9[0][0]
                            name=myresult9[0][2]
                            print("The previously entered date of surgery for patient", name, "was", original)
                            print("Please edit the date of surgery")
                            
                            def change():
                                ye=int(input("Enter the year of operation"))
                                mo=int(input("Enter the month of operation"))
                                da=int(input("Enter the date of operation"))
                                try:
                                    from datetime import date
                                    global dateofsurgery1
                                    dateofsurgery1 = date(ye,mo,da)
                                    print("Entered date of surgery", dateofsurgery1)
                                    
                                except:
                                    print("value error")
                                    change()

                                sql="select Date_Of_Adm, Date_Of_Dis from in_patient where Patient_ID=%s"
                                val=patientid
                                mycursor.execute(sql,(val,))
                                myresult10=mycursor.fetchall()
                            
                                dateofadm=myresult10[0][0]
                                dateofdis=myresult10[0][1]
                                if dateofadm > dateofsurgery1 or dateofsurgery1 > dateofdis:
                                
                                    print("Date of surgery is invalid. Date of surgery should be between date of admission and discharge of the patient")
                                    print("date of admission", dateofadm)
                                    print("date of discharge", dateofdis)
                                    
                                    change()
                                else:
                                    
                                    sql="update out_patient set Date_Of_Surgery=%s where Date_Of_Surgery=%s"
                                    val=(dateofsurgery1,original)
                                    mycursor.execute(sql,val)
                                    mydb.commit()
                                    print("Your new date of surgery registered in the database is", dateofsurgery1)
                            change()
                    elif (l==4):
                        def changestatus():
                        
                            surgeryno=str(input("Enter the surgery number provided during the surgery"))
                            sql="select Status_Of_Treatment, Patient_ID, Patients_First_Name from out_patient where exists(select Bill_No from out_patient where Surgery_No=%s)"
                            val=surgeryno
                            mycursor.execute(sql,(val,))
                            myresult11=mycursor.fetchall()
                            
                            if myresult11==[]:
                                print("The entered Surgery number was not found in the database. Try Again")
                                print("\n 1. TRY AGAIN")
                                print("\n 2. BACK TO MAIN MENU")
                                wee=int(input("\n"))
                                if (wee==1):
                                    changestatus()
                                elif (wee==2):
                                    return None
                                else:
                                    print("INVALID ENTRY")
                                    return None
                                
                            else:
                                patientid=myresult11[0][1]
                                original=myresult11[0][0]
                                name=myresult11[0][2]
                                sql15="select Doctor_ID from patient where Patient_ID=%s"
                                val15=patientid
                                mycursor.execute(sql,(val,))
                                myresult15=mycursor.fetchall()
                                doctorid=myresult15[0][0]
                                print("The previously entered status of treatment for patient", name, "was", original)
                                print("Please edit the status of treatment")
                                print("\n\n Select one of the options which best suited to the operation status")
                                print("1. Operation successful, patient can be discharged at will")
                                print("2. Operation successful, patient still needs to be under hospital care due to complications which may arise")
                                print("3. Operation not successful, patient should be kept under special care.")
                                print("4. Operation not successful, patient could not be saved.")
                                stat=int(input("\n Enter most viable option: "))
                                
                                if stat==1:
                                    status="success, alive"
                                    sql2="update doctor set Success=Success+1 where Doctor_ID=%s"
                                    val2=doctorid
                                    mycursor.execute(sql2,(val2,))
                                    mydb.commit()
                                    
                                elif stat==2:
                                    status="success, stable"
                                    sql2="update doctor set Success=Success+1 where Doctor_ID=%s"
                                    val2=doctorid
                                    mycursor.execute(sql2,(val2,))
                                    mydb.commit()
                                elif stat==3:
                                    status="fail, critical"
                                    sql2="update doctor set Fail=Fail+1 where Doctor_ID=%s"
                                    val2=doctorid
                                    mycursor.execute(sql2,(val2,))
                                    mydb.commit()
                                elif stat==4:
                                    status="fail, dead"
                                    sql2="update doctor set Fail=Fail+1 where Doctor_ID=%s"
                                    val2=doctorid
                                    mycursor.execute(sql2,(val2,))
                                    mydb.commit()
                                else:
                                    print("INVALID INPUT")
                                sql4="update out_patient set Status_Of_Treatment=%s where Status_Of_Treatment=%s and Patient_ID=%s"
                                
                                values=(status, original, patientid)
                                mycursor.execute(sql4,values)
                                mydb.commit()
                                print("\nOPERATION DETAILS UPDATED SUCCESSFULLY.")
                        changestatus()
                    elif (l==5):
                        print("\n\nDIRECTING BACK TO MAIN MENU..")
                        continue
                    else:
                        print("INVALID INPUT, TRY AGAIN")
                        continue
                                
                elif (h==2):
                    print("\n WARNING: DELETION OF DETAILS WILL RESULT IN REMOVAL OF ALL YOUR DETAILS FROM THE DATABASE. THIS ACTION CANNOT BE UNDONE. ")
                    print("\n ARE YOU SURE YOU WANT TO CONTINUE?")
                    print("1. I agree, remove my details from this institution")
                    print("2. No, back to main menu")
                    ch=int(input("enter your choice: "))
                    if (ch==1):
                        print("Deletion of details requested by user...")
                        print("Waiting for request to be accepted..")
                        print("The process of complete deletion of your details has started. This might take a minute")
                        print("...")
                        sql16="delete from doctor where Doctor_ID=%s"
                        val=auth
                        mycursor.execute(sql16,(auth,))
                        mydb.commit()
                        print("Details have been successfully deleted")
                        continue
                    elif (ch==2):
                        print("Directing you to main menu")
                        continue
                    else:
                        print("INVALID ENTRY")
                        continue
                else:
                    print("INVALID ENTRY")
                    continue
                        
                        
        elif (yus==2):
            print("Please enter your Patient ID for authentication")
            auth=str(input("Patient id: "))
            sql="select Patients_First_Name, Patients_Last_Name from patient where Patient_ID = %s"
            val=auth
            mycursor.execute(sql,(val,))
            myresult0=mycursor.fetchall()
            
            if myresult0==[]:
                print("Your details are not to be found in the database. Please try again")
                continue
            else:
                print("Welcome ", myresult0[0][0], myresult0[0][1], "!!")
                print("\n\nDo you wish to: \n 1. UPDATE RECORDS\n 2. DELETE RECORDS\n Please select 1 or 2 ")
                h=int(input())
                if (h==1):
                    print("here are some of the details you can edit: ")
                    print("1. Patient Age")
                    print("2. Disease the patient is suffering from")
                    print("3. contact details of the patient")
                    print("4. Request to change another room")
                    print("5. Back to main menu")
                    o=int(input("enter your choice: "))
                    if (o==1):
                        newage=int(input("Please enter your age: "))
                        sql="update patient set Patient_Age=%s where Patient_ID=%s"
                        val=(newage,auth)
                        mycursor.execute(sql,val)
                        mydb.commit()
                        print("Your new age registered in the database is", newage)
                    elif (o==2):
                        sql="select Disease from patient where Patient_ID=%s"
                        val=auth
                        mycursor.execute(sql,(val,))
                        myresult30=mycursor.fetchall()
                        originald=myresult30[0][0]
                        print("The original disease registered in the database is", originald)
                        newd=str(input("Enter your new disease : "))
                        sql00="update patient set Disease=%s where Patient_ID=%s"
                        vals=(newd,auth)
                        mycursor.execute(sql00,vals)
                        mydb.commit()
                        print("Details have been edited ")
                        print("\n YOUR DISEASE WAS CHANGED FROM", originald, "TO", newd)
                    elif (o==3):
                        sql191="select Phone from patient where Patient_ID=%s"
                        val=auth
                        mycursor.execute(sql191,(val,))
                        myresult191=mycursor.fetchall()
                        originalp=myresult191[0][0]
                        print("\n The original phone number entered was", originalp)
                        print("n Now, please enter the new phone number")
                        var=0
                        while (var==0):
                            ph=(input("Phone no.: "))
                            pho=str(ph)
                            if ('1','2','3','4','5','6','7','8','9','0' in pho) and len(pho)==10:
                                break
                            else:
                                print("Invalid phone no.")
                                print("Enter again")
                                continue
                        sql01="update patient set Phone=%s where Patient_ID=%s"
                        vals=(pho,auth)
                        mycursor.execute(sql01,vals)
                        mydb.commit()
                        print("Details have been edited ")
                        print("\n YOUR PHONE NUMBER WAS CHANGED FROM", originalp, "TO", pho)
                    elif (o==4):
                        sql90="select Room_no, Type_Of_Room, Cost_Per_Day from room where Patient_ID=%s"
                        vals=auth
                        mycursor.execute(sql90,(vals,))
                        myresult90=mycursor.fetchall()
                        if myresult90==[]:
                            print("You have already been discharged. There is no room allotted to you as per our records.")
                            continue
                        else:
                            
                            print("As per our records, your current room details are:")
                            print("\n ROOM NO: ", myresult90[0][0])
                            print("\n TYPE OF ROOM: ", myresult90[0][1])
                            print("\n COST PER DAY OF ROOM: ", myresult90[0][2])
                            print("\n Now, please select which type of room you desire:")
                            print("ROOMS")
                            print("1. General ward")
                            print("2. Semi private room")
                            print("3. Private room")
                            print("4. Suite")

                            x=0
                            roomchoice=int(input("enter your choice"))
                            while (x==0):
                                    
                                if roomchoice==1:
                                    typeofroom="General ward"
                                    costperday=12000
                                    x=1
                                elif roomchoice==2:
                                    typeofroom="Semi private room"
                                    costperday=16000
                                    x=1
                                elif roomchoice==3:
                                    typeofroom="Private room"
                                    costperday=18000
                                    x=1
                                elif roomchoice==4:
                                    x=1
                                    typeofroom="Suite"
                                    costperday=21000
                                else:
                                    print("invalid. try again")
                                    continue
                            print("your new selected room is",typeofroom,"and cost per day is", costperday)
                            import string
                            import random
                            def id_generator2(size=3, chars=string.digits):
                                    return ''.join(random.choice(chars) for _ in range(size))
                            
                            roomno=id_generator2()
                            print("your new room number is",roomno)
                            sql="update room set Room_no=%s, Patient_ID=%s, Type_Of_Room=%s,Cost_Per_Day=%s where Patient_ID=%s"
                            val=(roomno,auth,typeofroom,costperday,auth)
                            mycursor.execute(sql,val)
                            mydb.commit()
                            print("\n\nYour details have been updated successfully")
                    elif(o==5):
                        print("directing you to main menu...")
                        continue
                    else:
                        print("INVALID ENTRY")
                        continue
                elif (h==2):
                    print("\n WARNING: DELETION OF DETAILS WILL RESULT IN REMOVAL OF ALL YOUR DETAILS FROM THE DATABASE. THIS ACTION CANNOT BE UNDONE. ")
                    print("\n ARE YOU SURE YOU WANT TO CONTINUE?")
                    print("1. I agree, remove my details from this hospital")
                    print("2. No, back to main menu")
                    ch=int(input("enter your choice: "))
                    if (ch==1):
                        print("Deletion of details requested by user...")
                        print("Waiting for request to be accepted..")
                        print("The process of complete deletion of your details has started. This might take a minute")
                        print("...")
                        pass
                        sql16="delete from patient where Patient_ID=%s"
                        val=auth
                        mycursor.execute(sql16,(auth,))
                        mydb.commit()
                        print("Details have been successfully deleted")
                        continue
                    elif (ch==2):
                        print("Directing you to main menu")
                        continue
                    else:
                        print("INVALID ENTRY")
                        continue
                else:
                    print("INVALID ENTRY")
                    continue

        else:
            print("INVALID ENTRY")
            continue
                            
    if (ch==4):
        print("\t\t REPORT GENERATION")
        print("Here are the following data we can provide to a user about the hospital")
        print("\nABOUT THE PATIENT: ")
        print("\n1. All the information about a particular patient")
        print("2. Total no patients treated in the hospital")
        print("3. Total number of people having same disease/Injury")
        print("4. Name of those people who stayed for specific amount of days")
        print("5. Info of people who were admitted on a specific date")
        print("6. Info of people who were discharged on a specific date")
        print("7. Patients who had similar disease segregated on the basis of their gender")
        print("8. Info of those patients having similar disease in a particular age group")
        print("9. People who had similar disease and for how many days they were admitted")
        
        print("\n\nAbout the doctor:")
        print("\n10. Number of surgery done by a specific doctor")
        print("11. Name of those doctors having same field of expertise")
        print("12. Success rate of surgery and doctor having highest success rate")

        print("\n\nCash Flow and Misc: ")
        print("\n13. Total money generated on a specific day")
        print("14. Average Money generated per patient")
        print("15. Details of academic excellence of doctors (average marks scored)")

        print("\n\nRooms:")
        print("\n16. Total Numbers of rooms occupied and unoccupied in a day")
        print("\n\nWhich report do you desire to generate? ")
        print("1. ABOUT THE PATIENT")
        print("2. ABOUT THE DOCTOR")
        print("3. CASH FLOW")
        print("4. ROOMS")
        jk=int(input("Enter your choice (1/2/3/4): "))
        
        if (jk==1):
            jk1=int(input("Enter the particular report number from the aforementioned PATIENT reports: "))
            if (jk1==1):
                print("REPORT CHOSEN: 1. All the information about a particular patient")
                patientid=str(input("Enter the patientid of the particular patient: "))
                from tabulate import tabulate
                sql1="select*from patient where Patient_ID=%s "
                val1=patientid
                mycursor.execute(sql1,(val1,))
                myresult1=mycursor.fetchall()
                
                if myresult1==[]:
                    print("THE DETAILS ENTERED WERE NOT FOUND IN THE DATABASE. TRY AGAIN WITH VALID INPUTS")
                else:
                    print("\n\nGenerating your report...")
                    file=open("report","w")
                    file.write("This report contains all details of the patient entered at the time of admission")
                    file.write("\n\n")
                    file.write("""
                                            =================================================================================
             
                                                                   WELCOME TO NEWLIFE HOSPITALS PVT. LTD. 

                                            =================================================================================
                    """)
                    
                    file.write("\n")
                    file.write(tabulate(myresult1, headers=['Patient ID', 'Patients first Name','Patients Last Name', 'Patients Age','DOB','Doctor ID','Gender','Disease','Phone'], tablefmt='psql'))
                    file.close()
                    file=open("report","r")
                    print(file.read())
                    print("\n\nYour desired report is generated and SAVED")
            elif (jk1==2):
                print("REPORT CHOSEN: 2. Total no patients treated in the hospital")
                sql2a="select Patient_ID, Patients_First_Name, Patients_Last_Name from patient"
                mycursor.execute(sql2a)
                myresult2a=mycursor.fetchall()
                sql2b="select count(Patient_ID) from patient"
                mycursor.execute(sql2b)
                myresult2b=mycursor.fetchall()
                if myresult2a==[]:
                    print("There are no patients admitted in the hospital currently")
                else:
                    from tabulate import tabulate
                    file=open("report","w")
                    print("\n\nGenerating your report...")
                    file.write("This report contains the number of patients admitted in the hospital and their names")
                    file.write("\n\n")
                    file.write("""
                                            =================================================================================
             
                                                                   WELCOME TO NEWLIFE HOSPITALS PVT. LTD. 

                                            =================================================================================
                    """)
                    
                    file.write("\n")
                    file.write(tabulate(myresult2a, headers=['Patient ID','Patients first Name','Patients Last Name'], tablefmt='psql'))
                    file.write("\n")
                    file.write(tabulate(myresult2b, headers=['Number of Patients'], tablefmt='psql'))
                    file.close()
                    file=open("report","r")
                    print(file.read())
                    print("\n\nYour desired report is generated and SAVED")
            elif (jk1==3):
                print("REPORT CHOSEN: 3. Total number of people having same disease/Injury")
                sql3a="select count(Patient_ID), Disease from patient group by Disease"
                mycursor.execute(sql3a)
                myresult3a=mycursor.fetchall()
                if myresult3a==[]:
                    print("There are no patients admitted in the hospital currently")
                else:
                    from tabulate import tabulate
                    file=open("report","w")
                    print("\n\nGenerating your report...")
                    file.write("This report contains the number of patients admitted in the hospital, suffering from the same disease/injury")
                    file.write("\n\n")
                    file.write("""
                                            =================================================================================
             
                                                                   WELCOME TO NEWLIFE HOSPITALS PVT. LTD. 

                                            =================================================================================
                    """)
                    
                    file.write("\n")
                    file.write(tabulate(myresult3a, headers=['Patients having particular disease','Disease'], tablefmt='psql'))
                    file.close()
                    file=open("report","r")
                    print(file.read())
                    print("\n\nYour desired report is generated and SAVED")
            elif (jk1==4):
                print("REPORT CHOSEN: 4. Name of those people who stayed for specific amount of days")
                no=int(input("Enter a specific number of days of treatment"))
                if (no<=0):
                    print("The number of days should be greater than or equal to 1")
                else:
                    sql4="select Patients_First_Name, patient.Patient_ID from patient, in_patient where No_Of_Days_Adm=%s and patient.Patient_ID=in_patient.Patient_ID"
                    val4=no
                    mycursor.execute(sql4,(val4,))
                    myresult4=mycursor.fetchall()
                    if myresult4==[]:
                        print("There are NO details of patients admitted for", no, "days")
                        print("\n Try again")
                        continue
                    else:
                        from tabulate import tabulate
                        file=open("report","w")
                        
                        print("\n\nGenerating your report...")
                        file.write("This report contains the name and ID of patients admitted in the hospital for"+str(no)+"days")
                        file.write("\n\n")
                        file.write("""
                                                =================================================================================
                 
                                                                       WELCOME TO NEWLIFE HOSPITALS PVT. LTD. 

                                                =================================================================================
                        """)
                        
                        file.write("\n")
                        file.write(tabulate(myresult4, headers=['Patients First Name','Patient ID'], tablefmt='psql'))
                        file.close()
                        file=open("report","r")
                        print(file.read())
                        print("\n\nYour desired report is generated and SAVED.")
            elif (jk1==5):
                print("REPORT CHOSEN: 5. Info of people who were admitted on a specific date ")
                print("Date of admission")
                from datetime import date
                ye5=int(input("Enter the year of admission (YYYY): "))
                mo5=int(input("Enter the month of admission (MM): "))
                da5=int(input("Enter the date of admission (DD): "))
                try:
                    dateofadm5a=date(ye5,mo5,da5)
                    dateofadm5b=str(dateofadm5a)
                    val=dateofadm5b
                    sql5="select patient.Patient_ID,Patients_First_Name,Patients_Last_Name, Disease,Gender,Patient_Age from patient,in_patient where Date_Of_Adm=%s and in_patient.Patient_ID=patient.Patient_ID"
                    mycursor.execute(sql5,(val,))
                    myresult5=mycursor.fetchall()
                    if myresult5==[]:
                        print("No patient was admitted on", dateofadm5b)
                        continue
                    else:
                        from tabulate import tabulate
                        file=open("report","w")
                        print("\n\nGenerating your report...")
                        file.write("This report contains the details of patients admitted on"+str(dateofadm5b))
                        file.write("\n\n")
                        file.write("""
                                                =================================================================================
                 
                                                                       WELCOME TO NEWLIFE HOSPITALS PVT. LTD. 

                                                =================================================================================
                        """)
                        
                        file.write("\n")
                        file.write(tabulate(myresult5, headers=['Patient ID','Patients First Name','Patients Last Name','Disease','Gender','Age'], tablefmt='psql'))
                        file.close()
                        file=open("report","r")
                        print(file.read())
                        print("\n\nYour desired report is generated and SAVED")
                except:
                    print("value error")
                    continue
            elif (jk1==6):
                print("REPORT CHOSEN: 6. Info of people who were discharged on a specific date ")
                print("Date of discharge")
                from datetime import date
                ye6=int(input("Enter the year of discharge (YYYY): "))
                mo6=int(input("Enter the month of discharge (MM): "))
                da6=int(input("Enter the date of discharge (DD): "))
                try:
                    
                    dateofdis6a=date(ye6,mo6,da6)
                    dateofdis6b=str(dateofdis6a)
                    val=dateofdis6b
                    sql6="select patient.Patient_ID,Patients_First_Name,Patients_Last_Name, Disease,Gender,Patient_Age from patient,in_patient where Date_Of_Dis=%s and in_patient.Patient_ID=patient.Patient_ID"
                    mycursor.execute(sql6,(val,))
                    myresult6=mycursor.fetchall()
                    if myresult6==[]:
                        print("No patient was discharged on", dateofdis6b)
                        continue
                    else:
                        from tabulate import tabulate
                        file=open("report","w")
                        
                        file.write("\n\nGenerating your report...")
                        file.write("This report contains the details of patients discharged on"+str(dateofdis6b))
                        file.write("\n\n")
                        file.write("""
                                                =================================================================================
                 
                                                                       WELCOME TO NEWLIFE HOSPITALS PVT. LTD. 

                                                =================================================================================
                        """)
                        
                        file.write("\n")
                        file.write(tabulate(myresult6, headers=['Patient ID','Patients First Name','Patients Last Name','Disease','Gender','Age'], tablefmt='psql'))
                        file.close()
                        file=open("report","r")
                        print(file.read())
                        print("\n\nYour desired report is generated and SAVED")
                except:
                    print("value error")
                    continue
            elif (jk1==7):
                print("REPORT CHOSEN: 7. Patients who had similar disease segregated on the basis of their gender")
                sql7a="select distinct Disease from patient"
                mycursor.execute(sql7a)
                myresult7a=mycursor.fetchall()
                y=len(myresult7a)
                print("There are", y, "distinct diseases in our database")
                print("choose any one")
                list7=[]
                for i in range (0,y):
                    print(i+1,".",myresult7a[i][0])
                    list7.append(myresult7a[i][0])
                ch7=int(input("Enter disease number: "))
                if ch7>y:
                    print("INVALID CHOICE")
                    
                elif ch7<=0:
                    print("INVALID CHOICE")
                    
                else:
                    disease7=list7[ch7-1]
                    print("\nNow, the system will calculate data regarding this disease based on different genders")
                    sql7b="select count(Patient_ID) from patient where Disease=%s and Gender=%s"
                    val7b=(disease7,"female")
                    mycursor.execute(sql7b,val7b)
                    myresult7b=mycursor.fetchall()
                    
                    val7c=(disease7,"male")
                    mycursor.execute(sql7b,val7c)
                    myresult7c=mycursor.fetchall()

                    val7d=(disease7,"other")
                    mycursor.execute(sql7b,val7d)
                    myresult7d=mycursor.fetchall()

                    sql7e="select count(Patient_ID) from patient where Disease=%s"
                    val7e=disease7
                    mycursor.execute(sql7e,(val7e,))
                    myresult7e=mycursor.fetchall()
                    
                    

                    from tabulate import tabulate
                    print("CHOSEN DISEASE: ",disease7)
                    print("\n\nGenerating your report...")
                    print("This report contains the details of patients having disease", disease7)
                    print("\n\n")
                    print("""
                                            =================================================================================
             
                                                                   WELCOME TO NEWLIFE HOSPITALS PVT. LTD. 

                                            =================================================================================
                    """)
                    
                    print("\n")
                    print("Total number of patients having", disease7, "are", myresult7e[0][0])
                    print("\n")
                    print(tabulate(myresult7b, headers=['Number of female patients having the disease','Gender'], tablefmt='psql'))
                    print(tabulate(myresult7c, headers=['Number of male patients having the disease','Gender'], tablefmt='psql'))
                    print(tabulate(myresult7d, headers=['Number of other patients having the disease','Gender'], tablefmt='psql'))
                    print("\n")
                    print("Amongst all the patients infected with this disease: ")
                    print("\nMale people infected with", disease7,"are: ", ((myresult7b[0][0]/myresult7e[0][0])*100), "%")
                    print("\nFemale people infected with", disease7,"are: ", ((myresult7c[0][0]/myresult7e[0][0])*100), "%")
                    print("\nOther people infected with", disease7,"are: ", ((myresult7d[0][0]/myresult7e[0][0])*100), "%")
                    
                    print("\n\nYour desired report is generated and SAVED")
            elif (jk1==8):
                print("REPORT CHOSEN: 8. Info of those patients having similar disease in a particular age group")
                print("Define Age Group")
                start=int(input("Enter starting age of this particular age group: "))
                end=int(input("Enter ending age of this particular age group: "))
                if start>=0 and end >=0 and end>start:
                    
                    sql8a="select distinct(Disease) from patient where Patient_Age between %s and %s"
                    val8a=(start,end)
                    mycursor.execute(sql8a,val8a)
                    myresult8a=mycursor.fetchall()
                    y=len(myresult8a)
                    print("There are", y, "distinct disease(s) in our database")
                    list8a=[]
                    list8b=[]
                    for i in range (0,y):
                        print(i+1,".",myresult8a[i][0])
                        list8a.append(myresult8a[i][0])
                
                        sql8b="select count(Patient_ID),Disease from patient where Patient_Age between %s and %s and Disease=%s"
                        val8b=(start,end,list8a[i])
                        mycursor.execute(sql8b,val8b)
                        myresult8=mycursor.fetchall()
                        
                        list8b.append(myresult8)
                    
                    sql8c="select count(Patient_ID) from patient where Patient_Age between %s and %s"
                    val8c=(start,end)
                    mycursor.execute(sql8c,val8c)
                    myresult8c=mycursor.fetchall()
                    from tabulate import tabulate
                    print("\n\nGenerating your report...")
                    file=open("report","w")
                    file.write("This report contains the details of patients in age group"+str(start)+"-"+str(end))
                    file.write("\n\n")
                    file.write("""
                                            =================================================================================

                                                                   WELCOME TO NEWLIFE HOSPITALS PVT. LTD. 

                                            =================================================================================
                    """)
                    
                    file.write("\n")
                    file.write("Total number of patients in particular age group: "+str(myresult8c[0][0]))
                    file.write("\n")
                    y8b=len(list8b)
                    
                    for j in range(0,y8b):
                        file.write("\n\n")
                        file.write(tabulate(list8b[j], headers=['Number of patients having the disease','Disease'], tablefmt='psql'))
                        file.write("\n")
                        file.write("Percentage of people having this disease in the given age group is:"+str((list8b[j][0][0]/myresult8c[0][0])*100)+ "%") 
                    print("\n\nYour desired report is generated and SAVED")
                    file.close()
                    file=open("report","r")
                    print(file.read())
                        
                else:
                    print("INVALID INPUT")
            elif (jk1==9):
                print("REPORT CHOSEN: 9. People who had similar disease and for how many days they were admitted")
                sql9a="select distinct(Disease) from patient,in_patient where patient.Patient_ID=in_patient.Patient_ID"
                
                mycursor.execute(sql9a)
                myresult9a=mycursor.fetchall()
                
                y=len(myresult9a)
                print("There are", y, "distinct disease(s) contracted by the patients in our database currently")
                list9a=[]
                list9b=[]
                for i in range (0,y):
                    print(i+1,".",myresult9a[i][0])
                    list9a.append(myresult9a[i][0])
            
                    sql9b="select in_patient.Patient_ID, patient.Patients_First_Name, No_Of_Days_Adm, Disease from patient, in_patient where Disease=%s and patient.Patient_ID=in_patient.Patient_ID"
                    val9b=(list9a[i])
                    mycursor.execute(sql9b,(val9b,))
                    myresult9=mycursor.fetchall()
                    
                    list9b.append(myresult9)
                from tabulate import tabulate
                print("\n\nGenerating your report...")
                file=open("report","w")
                file.write("This report contains the details of patients in having same disease on the basis of number of days for which they were admitted")
                file.write("\nTo keep the results of this report fair and exact, the data mentioned below is SOLELY based on patients who have already been discharged till date")
                file.write("\n")
                file.write("""
                                        =================================================================================

                                                               WELCOME TO NEWLIFE HOSPITALS PVT. LTD. 

                                        =================================================================================
                """)
                
                file.write("\n")
                
                file.write("\n")
                y9b=len(list9b)
                
                for j in range(0,y9b):
                    file.write("\n\n")
                    file.write(tabulate(list9b[j], headers=['Patient ID','Patients Name','Number of days admitted','Disease'], tablefmt='psql'))
                    
                print("\n\nYour desired report is generated and SAVED")
                file.close()
                file=open("report","r")
                print(file.read())
            else:
                print("Invalid input")
        elif (jk==2):
            jk2=int(input("Enter the particular report number from the aforementioned reports: "))
            if (jk2==10):
                print("REPORT CHOSEN: 10. Number of surgery done by a specific doctor")
                doctorid=str(input("Enter the doctorid of the particular doctor: "))
                from tabulate import tabulate
                sql10="select Doctor_ID, Doctors_First_Name, Doctors_Last_Name, Specialization_Of_Doctor, sum(Success+Fail) from doctor where Doctor_ID=%s "
                val10=doctorid
                mycursor.execute(sql10,(val10,))
                myresult10=mycursor.fetchall()
                
                if myresult10==[]:
                    print("THE DETAILS ENTERED WERE NOT FOUND IN THE DATABASE. TRY AGAIN WITH VALID INPUTS")
                else:
                    print("\n\nGenerating your report...")
                    file=open("report","w")
                    file.write("This report contains details of the doctor inclusive of total number of sugeries performed by a particular doctor")
                    file.write("\n\n")
                    file.write("""
                                            =================================================================================
             
                                                                   WELCOME TO NEWLIFE HOSPITALS PVT. LTD. 

                                            =================================================================================
                    """)
                    
                    file.write("\n")
                    file.write(tabulate(myresult10, headers=['Doctor ID', 'Doctors first Name','Doctors Last Name','Specialization','Total number of surgeries done'], tablefmt='psql'))
                    print("\n\nYour desired report is generated and SAVED")
                    file.close()
                    file=open("report","r")
                    print(file.read())
            elif (jk2==11):
                print("REPORT CHOSEN: 11. Name of those doctors having same field of expertise")
                sql11a="select distinct(Specialization_Of_Doctor) from doctor"
                
                mycursor.execute(sql11a)
                myresult11a=mycursor.fetchall()
                
                y=len(myresult11a)
                print("There are", y, "distinct specialization(s) of doctors in our database currently")
                list11a=[]
                list11b=[]
                for i in range (0,y):
                    print(i+1,".",myresult11a[i][0])
                    list11a.append(myresult11a[i][0])
            
                    sql11b="select Doctors_First_Name, Doctors_Last_Name, Specialization_Of_Doctor from doctor where Specialization_Of_Doctor=%s"
                    val11b=(list11a[i])
                    mycursor.execute(sql11b,(val11b,))
                    myresult11=mycursor.fetchall()
                    
                    list11b.append(myresult11)
                from tabulate import tabulate
                file=open("report","w")
                print("\n\nGenerating your report...")
                file.write("This report contains the details of doctors having same field of expertise")
                
                file.write("""
                                        =================================================================================

                                                               WELCOME TO NEWLIFE HOSPITALS PVT. LTD. 

                                        =================================================================================
                """)
                
                file.write("\n")
                
                file.write("\n")
                y11b=len(list11b)
                
                for j in range(0,y11b):
                    
                    file.write("\n\n")
                    file.write("Specialization : "+str(list11b[j][0][2]))
                    file.write("\n")
                    file.write(tabulate(list11b[j], headers=['Doctors First Name', 'Doctors Last Name', 'Specialization Of Doctor'], tablefmt='psql'))
                    
                print("\n\nYour desired report is generated and SAVED")
                file.close()
                file=open("report","r")
                print(file.read())
            elif (jk2==12):
                file=open("report","w")
                file.write("REPORT CHOSEN: 12. Success rate of surgery and doctor having highest success rate")
                file.write("\n\nGenerating your report...")
                file.write("This report contains the details of doctors and the doctor having the highest success rate")
                
                file.write("""
                                        =================================================================================

                                                               WELCOME TO NEWLIFE HOSPITALS PVT. LTD. 

                                        =================================================================================
                """)
                
                file.write("\n")

                sql12a="select Doctor_ID, Doctors_First_Name, Doctors_Last_Name, Specialization_Of_Doctor, Success, Fail from doctor"
                mycursor.execute(sql12a)
                myresult12a=mycursor.fetchall()
                list12a=[]
                for i in range (0,len(myresult12a)):
                    try:
                        x=int((myresult12a[i][4]/(myresult12a[i][5]+myresult12a[i][4]))*100)
                    except:
                        x=0
                    list12a.insert(i,x)
                    file.write("Doctor ID: "+str(myresult12a[i][0]))
                    file.write("\nDoctors First Name: "+str(myresult12a[i][1]))
                    file.write("\nDoctors Last Name: "+str(myresult12a[i][2]))
                    file.write("\nField of expertise: "+str(myresult12a[i][3]))
                    file.write("\nNumber of successful operations: "+str(myresult12a[i][4]))
                    file.write("\nNumber of unsuccessful operations: "+str(myresult12a[i][5]))
                    file.write("\n\nSUCCESS RATE OF SURGERY DONE BY THIS PARTICULAR DOCTOR: "+str(x)+"%")
                    file.write("\n\n\n")
                
                posn=list12a.index(max(list12a))
                count=0
                for j in range (0,len(list12a)):
                    if (list12a[j]==list12a[posn]):
                        count+=1
                if count>=2:
                    file.write("Two doctors have the same success rate, hence the system has chosen the doctor who joined this hospital first out of the two")
                    file.write("\n\nHighest success rate of surgery done by a doctor is: "+str(max(list12a))+"%")
                    file.write("\n")
                    file.write("The doctor who has the highest success rate is "+str(myresult12a[posn][1])+" "+str(myresult12a[posn][2]))
                    file.close()
                    file=open("report","r")
                    print(file.read())
                else:
                    file.write("Highest success rate of surgery done by a doctor is: "+str(max(list12a))+"%")
                    file.write("\n")
                    file.write("The doctor who has the highest success rate is "+str(myresult12a[posn][1])+" "+str(myresult12a[posn][2]))
                    file=open("report","r")
                    print(file.read())
                    print("\n\nYour desired report is generated and SAVED")
            else:
                print("INVAID ENTRY")
                continue
        elif (jk==3):
            
            jk3=int(input("Enter the particular report number from the aforementioned reports: "))
            if (jk3==13):
                
                print("REPORT CHOSEN: 13. Total money generated on a specific day")
                from datetime import date
                ye13=int(input("Enter the year of discharge (YYYY): "))
                mo13=int(input("Enter the month of discharge (MM): "))
                da13=int(input("Enter the date of discharge (DD): "))
                try:
                    
                    dateofdis13a=date(ye13,mo13,da13)
                    dateofdis13b=str(dateofdis13a)
                    val=dateofdis13b
                    sql13="select bill.Patient_ID, Total_Cost, Date_Of_Dis from bill, in_patient where Date_Of_Dis=%s and in_patient.Patient_ID=bill.Patient_ID"
                    mycursor.execute(sql13,(val,))
                    myresult13=mycursor.fetchall()
                    sql13b="select sum(Total_Cost) from bill, in_patient where Date_Of_Dis=%s and in_patient.Patient_ID=bill.Patient_ID"
                    mycursor.execute(sql13b,(val,))
                    myresult13b=mycursor.fetchall()
                    if myresult13==[]:
                        print("No patient was discharged on", dateofdis13b)
                        print("Hence, no money was generated on that day")
                        continue
                    else:
                        from tabulate import tabulate
                        file=open("report","w")
                        print("\n\nGenerating your report...")
                        
                        file.write("This report contains the total amount of money generated on a specific date")
                        
                        file.write("""
                                                =================================================================================

                                                                       WELCOME TO NEWLIFE HOSPITALS PVT. LTD. 

                                                =================================================================================
                        """)
                        
                        file.write("\n")
                        file.write(tabulate(myresult13, headers=['Patient ID','Total Cost of this patient','Date of discharge'], tablefmt='psql'))
                        file.write("\n")
                        file.write(tabulate(myresult13b, headers=['Total money generated on this date'], tablefmt='psql'))
                        print("\n\nYour desired report is generated and SAVED")
                        file=open("report","r")
                        print(file.read())
                except:
                    print("value error")
                    continue
            elif (jk3==14):
                print("REPORT CHOSEN: 14. Average Money generated per patient")
                print("\nTo keep the results of this report fair and exact, the data mentioned below is SOLELY based on patients who have already been discharged till date")
                sql14a="select*from bill"
                mycursor.execute(sql14a)
                myresult14a=mycursor.fetchall()
                sql14b="select sum(Total_Cost) from bill"
                mycursor.execute(sql14b)
                myresult14b=mycursor.fetchall()
                sql14c="select count(Patient_ID) from bill"
                mycursor.execute(sql14c)
                myresult14c=mycursor.fetchall()
                sql14d="select avg(Total_Cost) from bill"
                mycursor.execute(sql14d)
                myresult14d=mycursor.fetchall()
                if myresult14a==[] or myresult14b==[] or myresult14c==[] or myresult14d==[]:
                    print("No patients have yet paid the bill, the report cannot be generated yet")
                    continue
                else:
                    from tabulate import tabulate
                    file=open("report","w")
                    print("\n\nGenerating your report...")
                    
                    file.write("This report contains the total amount of money generated on a specific date")
                    
                    file.write("""
                                            =================================================================================

                                                                   WELCOME TO NEWLIFE HOSPITALS PVT. LTD. 

                                            =================================================================================
                    """)
                    
                    file.write("\n")
                    file.write(tabulate(myresult14a, headers=['Bill no','Patient ID','Doctor ID','Number of days admitted','Total cost of patient','Cost per day'], tablefmt='psql'))
                    file.write("\n")
                    file.write(tabulate(myresult14b, headers=['Total money generated from these patients'], tablefmt='psql'))
                    file.write("\n")
                    file.write(tabulate(myresult14c, headers=['Total patients who have paid the bill'], tablefmt='psql'))
                    file.write("\n")
                    file.write(tabulate(myresult14d, headers=['AVERAGE COST GENERATED PER PATIENT'], tablefmt='psql'))
                    print("\n\nYour desired report is generated and SAVED")
                    file=open("report","r")
                    print(file.read())
            elif (jk3==15):
                print("REPORT CHOSEN: 15. Details of academic excellence of doctors (average marks scored)")
                sql15c="select Doctors_First_Name, Doctors_Last_Name, marks from doctor"
                mycursor.execute(sql15c)
                myresult15c=mycursor.fetchall()
                sql15d="select avg(marks) from doctor"
                mycursor.execute(sql15d)
                myresult15d=mycursor.fetchall()
                if myresult15d==[] or myresult15c==[]:
                    print("No doctors are registered in this database, the report cannot be generated yet")
                    continue
                else:
                    from tabulate import tabulate
                    file=open("report","w")
                    print("\n\nGenerating your report...")
                    
                    file.write("This report contains average marks of doctors")
                    
                    file.write("""
                                            =================================================================================

                                                                   WELCOME TO NEWLIFE HOSPITALS PVT. LTD. 

                                            =================================================================================
                    """)
                    
                    file.write("\n")
                    file.write(tabulate(myresult15c, headers=['Doctors First Name', 'Doctors Last Name', 'Marks scored'], tablefmt='psql'))
                    file.write("\n\n")
                    file.write(tabulate(myresult15d, headers=['AVERAGE MARKS SCORED BY DOCTORS'], tablefmt='psql'))
                    print("\n\nYour desired report is generated and saved and SAVED")
                    file=open("report","r")
                    print(file.read())
            else:
                print("INVALID INPUT")
                continue
        elif (jk==4):
            jk4=int(input("Enter the particular report number from the aforementioned reports: "))
            if (jk4==16):
                print("REPORT CHOSEN: 16. Total number of rooms occupied and unoccupied currently")
                sql16a="select * from room"
                mycursor.execute(sql16a)
                myresult16a=mycursor.fetchall()
                sql16b="select count(Room_No) from room"
                mycursor.execute(sql16b)
                myresult16b=mycursor.fetchall()
                if myresult16a==[] or myresult16b==[]:
                    print("No doctors are registered in this database, the report cannot be generated yet")
                    continue
                else:
                    from tabulate import tabulate
                    file=open("report","w")
                    print("\n\nGenerating your report file ...")
                    
                    file.write("This report contains average marks of doctors")
                    
                    file.write("""
                                            =================================================================================

                                                                   WELCOME TO NEWLIFE HOSPITALS PVT. LTD. 

                                            =================================================================================
                    """)
                    
                    file.write("\n")
                    file.write(tabulate(myresult16a, headers=['Room number','Patient ID', 'Type of room', 'Cost per day'], tablefmt='psql'))
                    file.write("\n")
                    file.write(tabulate(myresult16b, headers=['NUMBER OF ROOMS OCCUPIED AT THIS MOMENT'], tablefmt='psql'))
                    file.write("\n")
                    file.write("Total capacity of this hospital is: 999 beds")
                    file.write("\n")
                    file.write("Total number of unoccupied rooms are: " +str(999-myresult16b[0][0]))
                    print("\n\nYour desired report is generated and SAVED.")
                    file.close()
                    file=open("report","r")
                    print(file.read())
            else:
                print("INVALID INPUT")
                continue
        else:
            print("INVALID INPUT")
            continue
                
                
                
                
                
                
                
                
                
                
                
            
            
                
                

                
                    
                
                
                
                

                        
                        
                    
                    
                
                    
                        
                
                
                        
                
                
                
                
                
                    
                
                
                
                    

                
                
               
        
        
                        

                        
                        
                
                
            
            

            
            
            
            
        
    
            
                
                
                
                
             
            
        
            




            
      
            

    
    
        
        
        
 
         


  



    
    
    

