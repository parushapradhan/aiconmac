import Tkinter as tk
import pickle
import ttk as ttk
import os
import sys

z=file('Database.dat','ab')
z.close()


class CompanyPeople(object):          

    def PersonDetails_AddCNG(self, CompanyName, PersonName, Personid , CompanyArea='NOT GIVEN',
                             CompanyPhone='NOT GIVEN', CompanyAddress='NOT GIVEN',
                             PersonPhone='NOT GIVEN',
                             PersonDes='NOT GIVEN'):

        self.CompanyName =  CompanyName.title()
        self.CompanyArea = CompanyArea.title()
        self.CompanyPhone = CompanyPhone.title()
        self.CompanyAddress = CompanyAddress.title()
        self.PersonName = PersonName.title()
        self.Personid = Personid.title()
        self.PersonPhone = PersonPhone.title()
        self.PersonDes = PersonDes.title()
 
        
        
        
        
        


class master(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.title('Database')

        container = tk.Frame(bg='white')
        container.pack(side="top", fill="both" , expand = True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)

        self.frames = {}

        for F in (MainPage,Add_New,Show_All,CompanySearchPage,PersonSearchPage):
            frame = F(container ,self)
            self.frames[F]=frame
            frame.grid(row=0,column=0,sticky="nsew")

        self.Show_frame(MainPage)

    def Show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

    def dict_Add(self):

        DataBase = file('Database.dat', 'rb')

        Data_dict = {}

        try:
            while True:
                obj = pickle.load(DataBase)

                if obj.CompanyName not in Data_dict:

                    Company_dict = {}
                    Person_dict  = {}
                    PersonDetails_dict = {}

                    Company_dict['companyarea'] = obj.CompanyArea
                    Company_dict['companyphone'] = obj.CompanyPhone
                    Company_dict['companyaddress'] = obj.CompanyAddress

                    PersonDetails_dict['personid'] = obj.Personid
                    PersonDetails_dict['personphone'] = obj.PersonPhone
                    PersonDetails_dict['persondes'] = obj.PersonDes

                    Person_dict[obj.PersonName]  = PersonDetails_dict

                    Company_dict['people'] = Person_dict

                    Data_dict[obj.CompanyName] = Company_dict


                elif obj.CompanyName in Data_dict:

                    PersonDetails_dict = {}

                    Company_dict = Data_dict.get(obj.CompanyName)
                    Person_dict = Company_dict.get('people')

                    PersonDetails_dict['personid'] = obj.Personid
                    PersonDetails_dict['personphone'] = obj.PersonPhone
                    PersonDetails_dict['persondes'] = obj.PersonDes

                    Person_dict[obj.PersonName]  = PersonDetails_dict

                    Company_dict['people'] = Person_dict

                    Data_dict[obj.CompanyName] = Company_dict

        except EOFError:
            pass

        DataBase.close()

        return Data_dict
                   

        




class MainPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg='white')

        Title = tk.Label(self, text='AICONMAC',bg='orange',fg='purple',font=('cooper',16)).pack(fill='x')

        F1=tk.Frame(self,bg='white')

        AddNew     = ttk.Button(F1, text='Add new contact', command=lambda: controller.Show_frame(Add_New))
        SearchData = ttk.Button(F1, text='Search for company details', command=lambda: controller.Show_frame(CompanySearchPage))
        Search     = ttk.Button(F1, text='Search for person details', command=lambda: controller.Show_frame(PersonSearchPage))
        ShowAll    = ttk.Button(F1, text='Show all the data', command=lambda: controller.Show_frame(Show_All))

        F1.pack()

        AddNew.grid(row=0, padx=2, columnspan=3)
        SearchData.grid(row=1, column=1, padx=2)
        Search.grid(row=1,column=2, padx=2)
        ShowAll.grid(row=2,columnspan=3, pady=4)
        

class Add_New(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        Title = tk.Label(self, text="Add new contact data").grid(row=0)

        Company=tk.Frame(self)

        CompanyName_label = tk.Label(Company, text='Company Name:')
        CompanyName_entry = tk.Entry(Company)

        Company.grid(row=1)
        Company.tkraise()


        CompanyName_label.grid(row=0, column=0)
        CompanyName_entry.grid(row=0, column=1)

        CompanyName = CompanyName_entry.get()


  

        Submit_Company = ttk.Button(Company, text='SUBMIT',
                                   command=lambda: self.CompanyName_Data(CompanyName_entry, self, Company, controller))
        Submit_Company.grid(row=1, columnspan=2)


        Back = ttk.Button(self, text="BACK", command= lambda: controller.Show_frame(MainPage))
        Back.grid(row=2, sticky='se')
        


    def restart(self):
        python = sys.executable
        os.execl(python, python, * sys.argv)


    def frameSwitcher(self, framenew, frameold):
        framenew.tkraise()
        framenew.grid(row=1, sticky='nsew', rowspan=2)


    def lastfunc(self, Parentframe, PersonDetails, CompanyName, PersonName, Personid , CompanyArea,
                 CompanyPhone, CompanyAddress, PersonPhone, PersonDes, controller, CompanyArea_entry,
                 CompanyAddress_entry, CompanyPhone_entry, PersonName_entry, PersonDes_entry, Personid_entry,
                 PersonPhone_entry, CompanyName_entry):

        self.frameSwitcher( Parentframe, PersonDetails)

        self.Data_Add(CompanyName, PersonName, Personid , CompanyArea,
                 CompanyPhone, CompanyAddress, PersonPhone, PersonDes, controller, CompanyArea_entry,
                 CompanyAddress_entry, CompanyPhone_entry, PersonName_entry, PersonDes_entry, Personid_entry,PersonPhone_entry, CompanyName_entry)



    def Data_Add(self, CompanyName, PersonName, Personid , CompanyArea,
                 CompanyPhone, CompanyAddress, PersonPhone, PersonDes, controller, CompanyArea_entry,
                 CompanyAddress_entry, CompanyPhone_entry, PersonName_entry, PersonDes_entry, Personid_entry,
                 PersonPhone_entry, CompanyName_entry):

        DataBase = open('Database.dat', 'ab')

        Data = CompanyPeople()
        Data.PersonDetails_AddCNG(CompanyName, PersonName, Personid , CompanyArea,
                                  CompanyPhone, CompanyAddress, PersonPhone, PersonDes)

        pickle.dump(Data, DataBase)

        

        controller.Show_frame(MainPage)

        CompanyArea_entry.delete(0, 'end')
        CompanyAddress_entry.delete(0, 'end')
        CompanyPhone_entry.delete(0, 'end')
        CompanyPhone_entry.delete(0, 'end')
        PersonName_entry.delete(0, 'end')
        PersonDes_entry.delete(0, 'end')
        Personid_entry.delete(0, 'end')
        PersonPhone_entry.delete(0, 'end')
        CompanyName_entry.delete(0, 'end')

        self.restart()







        



    def CompanyName_Data(self, CompanyName_entry, parent, Parentframe, controller):

        CompanyName_=CompanyName_entry.get()
        CompanyName_ = CompanyName_.title()


        #Company details frame
        CompanyDetails = tk.Frame(parent)

        CompanyArea_label = tk.Label(CompanyDetails, text='Company Area:')
        CompanyAddress_label = tk.Label(CompanyDetails, text='Company Address:')
        CompanyPhone_label = tk.Label(CompanyDetails, text='Company Phone no:')

        CompanyArea_entry = tk.Entry(CompanyDetails)
        CompanyAddress_entry = tk.Entry(CompanyDetails)
        CompanyPhone_entry = tk.Entry(CompanyDetails)

        CompanyArea_label.grid(row=0)
        CompanyAddress_label.grid(row=1)
        CompanyPhone_label.grid(row=2)

        CompanyArea_entry.grid(row=0, column=1)
        CompanyAddress_entry.grid(row=1, column=1)
        CompanyPhone_entry.grid(row=2, column=1)

        SubmitButton_1 = ttk.Button(CompanyDetails, text='SUBMIT',
                                   command=lambda: self.frameSwitcher(PersonDetails, CompanyDetails))
        SubmitButton_1.grid(row=3, columnspan=2)
        
        
        #Person details frame
        PersonDetails = tk.Frame(parent)

        PersonName_label = tk.Label(PersonDetails, text='Name:')
        PersonDes_label = tk.Label(PersonDetails, text='Designation:')
        Personid_label = tk.Label(PersonDetails, text='Email id')
        PersonPhone_label = tk.Label(PersonDetails, text='Phone number:')

        PersonName_entry = tk.Entry(PersonDetails)
        PersonDes_entry = tk.Entry(PersonDetails)
        Personid_entry = tk.Entry(PersonDetails)
        PersonPhone_entry = tk.Entry(PersonDetails)

        PersonName_label.grid(row=0)
        PersonDes_label.grid(row=1)
        Personid_label.grid(row=2)
        PersonPhone_label.grid(row=3)

        PersonName_entry.grid(row=0, column=1)
        PersonDes_entry.grid(row=1, column=1)
        Personid_entry.grid(row=2, column=1)
        PersonPhone_entry.grid(row=3, column=1)


        DataBase=open('Database.dat', 'rb')

        flag1=0
        object2= None
        try:
            
            while True:
                object1 = pickle.load(DataBase)
                
                print object1
                if CompanyName_ != object1.CompanyName:
                    flag1=0
                    object2=object1

                if CompanyName_ == object1.CompanyName:
                    flag1 = 1
                    object2=object1
                    
                    break
                
        except EOFError:
            pass

        DataBase.close()

        if object2 is None:

            object2 = CompanyPeople()
            object2.PersonDetails_AddCNG('', '', '')


            
        
        
        if flag1==0:
            self.frameSwitcher(CompanyDetails, Parentframe)

        if flag1==1:
            self.frameSwitcher(PersonDetails, Parentframe)

            

        SubmitButton_2 = ttk.Button(PersonDetails, text='SUBMIT', command=lambda: self.valueadd(CompanyName_, Parentframe, PersonDetails,
                                                                                               controller, CompanyArea_entry,
                                                                                               CompanyAddress_entry, CompanyPhone_entry,
                                                                                               PersonName_entry, PersonDes_entry,
                                                                                               Personid_entry, PersonPhone_entry,
                                                                                               CompanyName_entry, flag1, object2))
        SubmitButton_2.grid(row=4, columnspan=2)

        


    
        

    def valueadd(self,CompanyName_, Parentframe, PersonDetails, controller, CompanyArea_entry,
                 CompanyAddress_entry, CompanyPhone_entry, PersonName_entry, PersonDes_entry, Personid_entry,
                 PersonPhone_entry, CompanyName_entry, flag1, object1):
        if flag1==0:
            

            Company_Name=CompanyName_.title()
            Company_Area=CompanyArea_entry.get()
            Company_Phone=CompanyPhone_entry.get()
            Company_Address=CompanyAddress_entry.get()

            Person_Name=PersonName_entry.get()
            Person_id=Personid_entry.get()
            Person_Phone=PersonPhone_entry.get()
            Person_Des=PersonDes_entry.get()            


        if flag1==1:            

            Company_Name=object1.CompanyName
            Company_Area=object1.CompanyArea
            Company_Phone=object1.CompanyPhone
            Company_Address=object1.CompanyAddress

            Person_Name=PersonName_entry.get()
            Person_id=Personid_entry.get()
            Person_Phone=PersonPhone_entry.get()
            Person_Des=PersonDes_entry.get()

        self.lastfunc(Parentframe, PersonDetails,
                      Company_Name, Person_Name, Person_id , Company_Area,
                      Company_Phone, Company_Address, Person_Phone, Person_Des,
                      controller, CompanyArea_entry, CompanyAddress_entry, CompanyPhone_entry,
                      PersonName_entry, PersonDes_entry, Personid_entry,
                      PersonPhone_entry, CompanyName_entry)





        



    


class Show_All(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        Refresh = ttk.Button(self, text='Refresh')
        self.configure(bg='white')

        Data_dict = controller.dict_Add()


        canvas = tk.Canvas(self, height=200, width=1000, highlightthickness=0)
        canvas.configure(bg='white')

        canvas.grid(row=1, sticky='nsew')

        row = -1

        columnlargest=1

        Data_dict_keys = Data_dict.keys()
        Data_dict_keys.sort()


        

        for i in Data_dict_keys:

            frameComp = tk.Frame(canvas)
            frameComp.configure(bg='white')


            CompanyName = Data_dict[i]

            row=row+1
            

            CompanyArea = CompanyName['companyarea']
            CompanyAddress = CompanyName['companyaddress']
            People_dict = CompanyName['people']
            
            CompanyName_label_1 = tk.Label(frameComp, text='Company Name :')
            CompanyArea_label_1 = tk.Label(frameComp, text='Company Area :')
            CompanyAddress_label_1 = tk.Label(frameComp, text='Company Address :')
            
            CompanyName_label_2 = tk.Text(frameComp, height=1, width=len(i))
            CompanyArea_label_2 = tk.Text(frameComp, height=1, width=len(CompanyArea))
            CompanyAddress_label_2 = tk.Text(frameComp, height=1, width=len(CompanyAddress))

            CompanyName_label_2.insert(1.0, i)
            CompanyArea_label_2.insert(1.0, CompanyArea)
            CompanyAddress_label_2.insert(1.0, CompanyArea)

            CompanyName_label_2.configure(relief='flat')
            CompanyArea_label_2.configure(relief='flat')
            CompanyAddress_label_2.configure(relief='flat')

            CompanyName_label_1.grid(row=0, sticky='e')
            CompanyArea_label_1.grid(row=1, sticky='e')
            CompanyAddress_label_1.grid(row=2, sticky='e')
            CompanyName_label_2.grid(row=0, column=1, sticky='w')
            CompanyArea_label_2.grid(row=1, column=1, sticky='w')
            CompanyAddress_label_2.grid(row=2, column=1, sticky='w')

            frameComp.grid(row=row, pady=10)
            

            row=row+1
            personcolumn=0

            People_dict_keys = People_dict.keys()
            People_dict_keys.sort()

            

            for k in People_dict_keys:

                personframe = tk.Frame(canvas)
                personframe.configure(bg='white')


                PersonDetails = People_dict[k]

                PersonName = k
                PersonDes = PersonDetails['persondes']
                PersonID = PersonDetails['personid']
                PersonPhone = PersonDetails['personphone']

                PersonName_label_1 = tk.Label(personframe, text='Person Name :')
                PersonDes_label_1 = tk.Label(personframe, text='Person Designation :')
                PersonID_label_1 = tk.Label(personframe, text='Person ID :')
                PersonPhone_label_1 = tk.Label(personframe, text='Person Phone number :')

                PersonName_label_2 = tk.Text(personframe, height=1, width=len(PersonName))
                PersonDes_label_2 = tk.Text(personframe, height=1, width=len(PersonDes))
                PersonID_label_2 = tk.Text(personframe, height=1, width=len(PersonID))
                PersonPhone_label_2 = tk.Text(personframe, height=1, width=len(PersonPhone))

                PersonName_label_2.insert(1.0, PersonName)               
                PersonDes_label_2.insert(1.0, PersonDes)
                PersonID_label_2.insert(1.0, PersonID)
                PersonPhone_label_2.insert(1.0, PersonPhone)
                
                PersonName_label_2.configure(relief='flat')
                PersonDes_label_2.configure(relief='flat')
                PersonID_label_2.configure(relief='flat')
                PersonPhone_label_2.configure(relief='flat')

                PersonName_label_1.grid(row=0, sticky='e')
                PersonDes_label_1.grid(row=1, sticky='e')
                PersonID_label_1.grid(row=2, sticky='e')
                PersonPhone_label_1.grid(row=3, sticky='e')
                PersonName_label_2.grid(row=0, column=1, sticky='w')
                PersonDes_label_2.grid(row=1, column=1, sticky='w')
                PersonID_label_2.grid(row=2, column=1, sticky='w')
                PersonPhone_label_2.grid(row=3, column=1, sticky='w')

                personframe.grid(row=row, column=personcolumn, pady=10)
                personcolumn+=1

                if personcolumn > columnlargest:
                    columnlargest = personcolumn




        Done = ttk.Button(self, text='Done', command=lambda: controller.Show_frame(MainPage))
        Done.grid(row=2, columnspan=columnlargest)


class CompanySearchPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        CompanyName_frame = tk.Frame(self)

        CompanyName_label = tk.Label(CompanyName_frame, text='Company Name :')
        CompanyName_entry = tk.Entry(CompanyName_frame)
        Submit = ttk.Button(CompanyName_frame, text='submit', command=lambda: self.Data(CompanyName_entry, controller, self, CompanyName_frame))

        CompanyName_label.grid(row=0)
        CompanyName_entry.grid(row=0, column=1)
        Submit.grid(row=1, columnspan=2)

        Done = ttk.Button(self, text='Done', command=lambda: controller.Show_frame(MainPage))
        Done.grid(row=2, columnspan=4, sticky='se')
                           
        

        CompanyName_frame.grid(row=1, sticky='nsew')


    def Data(self, CompanyName_entry, controller, parent, CompanyName_frame):

        Data_dict=controller.dict_Add()

        CompanyName_data = CompanyName_entry.get().title()

        frame = tk.Frame(parent)

        row = 1

        if CompanyName_data not in Data_dict:

            answer = tk.Label(frame, text='Company Not in DataBase')

            answer.grid(row=0)

        elif CompanyName_data in Data_dict:

            CompanyName = Data_dict[CompanyName_data]

            CompanyArea = CompanyName['companyarea']
            CompanyAddress = CompanyName['companyaddress']
            People_dict = CompanyName['people']
            
            CompanyName_label_1 = tk.Label(frame, text='Company Name :')
            CompanyArea_label_1 = tk.Label(frame, text='Company Area :')
            CompanyAddress_label_1 = tk.Label(frame, text='Company Address :')
            
            CompanyName_label_2 = tk.Text(frame, height=1, width=len(CompanyName_data))
            CompanyArea_label_2 = tk.Text(frame, height=1, width=len(CompanyArea))
            CompanyAddress_label_2 = tk.Text(frame, height=1, width=len(CompanyAddress))

            CompanyName_label_2.insert(1.0, CompanyName_data)
            CompanyArea_label_2.insert(1.0, CompanyArea)
            CompanyAddress_label_2.insert(1.0, CompanyArea)

            CompanyName_label_2.configure(relief='flat')
            CompanyArea_label_2.configure(relief='flat')
            CompanyAddress_label_2.configure(relief='flat')

            CompanyName_label_1.grid(row=0, sticky='e')
            CompanyArea_label_1.grid(row=1, sticky='e')
            CompanyAddress_label_1.grid(row=2, sticky='e')
            CompanyName_label_2.grid(row=0, column=1, sticky='w')
            CompanyArea_label_2.grid(row=1, column=1, sticky='w')
            CompanyAddress_label_2.grid(row=2, column=1, sticky='w')

            frame.grid(row=row)
            

            
            personcolumn=0

            People_dict_keys = People_dict.keys()
            People_dict_keys.sort()

            

            for k in People_dict_keys:

                personframe = tk.Frame(frame)


                PersonDetails = People_dict[k]

                PersonName = k
                PersonDes = PersonDetails['persondes']
                PersonID = PersonDetails['personid']
                PersonPhone = PersonDetails['personphone']

                PersonName_label_1 = tk.Label(personframe, text='Person Name :')
                PersonDes_label_1 = tk.Label(personframe, text='Person Designation :')
                PersonID_label_1 = tk.Label(personframe, text='Person ID :')
                PersonPhone_label_1 = tk.Label(personframe, text='Person Phone number :')

                PersonName_label_2 = tk.Text(personframe, height=1, width=len(PersonName))
                PersonDes_label_2 = tk.Text(personframe, height=1, width=len(PersonDes))
                PersonID_label_2 = tk.Text(personframe, height=1, width=len(PersonID))
                PersonPhone_label_2 = tk.Text(personframe, height=1, width=len(PersonPhone))

                PersonName_label_2.insert(1.0, PersonName)               
                PersonDes_label_2.insert(1.0, PersonDes)
                PersonID_label_2.insert(1.0, PersonID)
                PersonPhone_label_2.insert(1.0, PersonPhone)
                
                PersonName_label_2.configure(relief='flat')
                PersonDes_label_2.configure(relief='flat')
                PersonID_label_2.configure(relief='flat')
                PersonPhone_label_2.configure(relief='flat')

                PersonName_label_1.grid(row=0, sticky='e')
                PersonDes_label_1.grid(row=1, sticky='e')
                PersonID_label_1.grid(row=2, sticky='e')
                PersonPhone_label_1.grid(row=3, sticky='e')
                PersonName_label_2.grid(row=0, column=1, sticky='w')
                PersonDes_label_2.grid(row=1, column=1, sticky='w')
                PersonID_label_2.grid(row=2, column=1, sticky='w')
                PersonPhone_label_2.grid(row=3, column=1, sticky='w')

                personframe.grid(row=3, column=personcolumn, pady=10)
                personcolumn+=1
        frame.grid(row=1, sticky='nsew')
        frame.tkraise()

        back = ttk.Button(frame, text='BACK', command=lambda: self.CompanyName_frame_raise(CompanyName_frame, CompanyName_entry))
        back.grid(row=4)

    def CompanyName_frame_raise(self, CompanyName_frame, CompanyName_entry):
        CompanyName_frame.tkraise()
        CompanyName_entry.delete(0, 'end')

class PersonSearchPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        Personframe = tk.Frame(self)

        PersonName_label = tk.Label(Personframe, text='Person Name :')
        PersonName_entry = tk.Entry(Personframe)
        Submit = ttk.Button(Personframe, text='SUBMIT', command=lambda: self.Datab(PersonName_entry, controller, Personframe, self))

        
        PersonName_label.grid(row=0)
        PersonName_entry.grid(row=0, column =1)
        Submit.grid(row=1, columnspan =2)
        Done = ttk.Button(self, text='Done', command=lambda: controller.Show_frame(MainPage))
        Done.grid(row=2, columnspan=4, sticky='se')
        Personframe.grid(row=1, sticky='nsew')

    def Datab (self, PersonName_entry, controller, Personframe, parent):

        Data_dict = controller.dict_Add()
        PersonName_Data = PersonName_entry.get()

        Data_dict_keys = Data_dict.keys()
        Data_dict_keys.sort()

        flag=0

        datascreen = tk.Frame(parent)


        

        for i in Data_dict_keys:

            print 'hi'

            frameComp = tk.Frame(datascreen)


            CompanyName = Data_dict[i]
            

            CompanyArea = CompanyName['companyarea']
            CompanyAddress = CompanyName['companyaddress']
            People_dict = CompanyName['people']
            
            CompanyName_label_1 = tk.Label(frameComp, text='Company Name :')
            CompanyArea_label_1 = tk.Label(frameComp, text='Company Area :')
            CompanyAddress_label_1 = tk.Label(frameComp, text='Company Address :')
            
            CompanyName_label_2 = tk.Text(frameComp, height=1, width=len(i))
            CompanyArea_label_2 = tk.Text(frameComp, height=1, width=len(CompanyArea))
            CompanyAddress_label_2 = tk.Text(frameComp, height=1, width=len(CompanyAddress))

            CompanyName_label_2.insert(1.0, i)
            CompanyArea_label_2.insert(1.0, CompanyArea)
            CompanyAddress_label_2.insert(1.0, CompanyArea)

            CompanyName_label_2.configure(relief='flat')
            CompanyArea_label_2.configure(relief='flat')
            CompanyAddress_label_2.configure(relief='flat')

            

            
            

            
            personcolumn=0

            People_dict_keys = People_dict.keys()
            People_dict_keys.sort()
            

            

            if PersonName_Data in People_dict_keys :

                personframe = tk.Frame(datascreen)


                PersonDetails = People_dict[PersonName_Data]

                PersonName = PersonName_Data
                PersonDes = PersonDetails['persondes']
                PersonID = PersonDetails['personid']
                PersonPhone = PersonDetails['personphone']

                PersonName_label_1 = tk.Label(personframe, text='Person Name :')
                PersonDes_label_1 = tk.Label(personframe, text='Person Designation :')
                PersonID_label_1 = tk.Label(personframe, text='Person ID :')
                PersonPhone_label_1 = tk.Label(personframe, text='Person Phone number :')

                PersonName_label_2 = tk.Text(personframe, height=1, width=len(PersonName))
                PersonDes_label_2 = tk.Text(personframe, height=1, width=len(PersonDes))
                PersonID_label_2 = tk.Text(personframe, height=1, width=len(PersonID))
                PersonPhone_label_2 = tk.Text(personframe, height=1, width=len(PersonPhone))

                PersonName_label_2.insert(1.0, PersonName)               
                PersonDes_label_2.insert(1.0, PersonDes)
                PersonID_label_2.insert(1.0, PersonID)
                PersonPhone_label_2.insert(1.0, PersonPhone)
                
                PersonName_label_2.configure(relief='flat')
                PersonDes_label_2.configure(relief='flat')
                PersonID_label_2.configure(relief='flat')
                PersonPhone_label_2.configure(relief='flat')

                PersonName_label_1.grid(row=0, sticky='e')
                PersonDes_label_1.grid(row=1, sticky='e')
                PersonID_label_1.grid(row=2, sticky='e')
                PersonPhone_label_1.grid(row=3, sticky='e')
                PersonName_label_2.grid(row=0, column=1, sticky='w')
                PersonDes_label_2.grid(row=1, column=1, sticky='w')
                PersonID_label_2.grid(row=2, column=1, sticky='w')
                PersonPhone_label_2.grid(row=3, column=1, sticky='w')

                CompanyName_label_1.grid(row=0, sticky='e')
                CompanyArea_label_1.grid(row=1, sticky='e')
                CompanyAddress_label_1.grid(row=2, sticky='e')
                CompanyName_label_2.grid(row=0, column=1, sticky='w')
                CompanyArea_label_2.grid(row=1, column=1, sticky='w')
                CompanyAddress_label_2.grid(row=2, column=1, sticky='w')

                frameComp.grid(row=0, pady=10)

                personframe.grid(row=1, column=personcolumn, pady=10)
                flag=1

        if flag==0:
            label = tk.Label(datascreen, text='Person not in database')
            label.grid(row=0)

        datascreen.grid(row=1, sticky='nsew')

        back = ttk.Button(datascreen, text='BACK', command=lambda: self.PersonName_frame_raise(Personframe, PersonName_entry))
        back.grid(row=4)

    def PersonName_frame_raise(self, Personframe, PersonName_entry):
        Personframe.tkraise()
        PersonName_entry.delete(0, 'end') 
                

                

                

                
                
app=master()
app.mainloop()


        
            



        
