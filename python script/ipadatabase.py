# -*- coding: utf-8 -*-
""" 
======================================
Created on Thu Mar 19 10:55:17 2020

@author: Mathew Bidinlib
======================================

"""
#pip install mysql-connector-python

# Import and define Tk
import os
import csv
import tkinter as tk
import pandas as pd
from pandas import DataFrame
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from  PIL    import  ImageTk, Image
from  tkinter import scrolledtext
from  tkinter import Menu
from tkinter import messagebox as msg
from tkinter.filedialog import asksaveasfile 


import mysql.connector
import json
import argparse
import cgi, cgitb


win = tk.Tk()



s = ttk.Style()
s.configure('new.TFrame', background = '#AFEEEE')


# Create and define tabs
tabcontrol = ttk.Notebook(win)
home = ttk.Frame(tabcontrol, style ='new.TFrame')
tabcontrol.add(home, text = "Home")
sts_database = ttk.Frame(tabcontrol, style ='new.TFrame')
tabcontrol.add(sts_database, text = "STS Database")
sts_recruit = ttk.Frame(tabcontrol,style ='new.TFrame')
tabcontrol.add(sts_recruit, text = "STS Recruitment")
comm_database = ttk.Frame(tabcontrol, style ='new.TFrame')
tabcontrol.add(comm_database, text = "Community Database")
lts_database = ttk.Frame(tabcontrol, style ='new.TFrame')
tabcontrol.add(lts_database, text = "LTS Database")

new1 = ttk.Frame(tabcontrol)
tabcontrol.add(new1, text = "Position 1")
new2 = ttk.Frame(tabcontrol)
tabcontrol.add(new2, text = "Position 2")
new3 = ttk.Frame(tabcontrol)
tabcontrol.add(new3, text = "Position 3")
new4 = ttk.Frame(tabcontrol)
tabcontrol.add(new4, text = "Position 4")
tabcontrol.pack(expand = 2 , fill = "both")

#tabcontrol.tab(1, state = "hidden")
tabcontrol.tab(1, state="hidden")
tabcontrol.tab(2, state="hidden")
tabcontrol.tab(3, state="hidden")
tabcontrol.tab(4, state="hidden")
tabcontrol.tab(5, state="hidden")
tabcontrol.tab(6, state="hidden")
tabcontrol.tab(7, state="hidden")
tabcontrol.tab(8, state="hidden")
#tabcontrol.grid(row = 1, column =1,sticky = "w")


'''
Home Page Design

'''
# function to proceed to login
def _gotologin():
    welcome_frame.place_forget()
    login_frame.place(height=900, width=2000, x=450, y=109)

# function to navigate to getting started
def _gettingstarted():
    welcome_frame.place_forget()
    gettingstarted.place(height=1050, width=2000, x=1, y=1)
    
# function to get back to home
def _backtohome():
    gettingstarted.place_forget()
    welcome_frame.place(height=500, width=2000,x=1, y=150)
    
        
'''
# Welcome frame and button
'''
welcome_frame = ttk.Frame(home, style ='new.TFrame') # create frame for the first home page view
welcome_frame.place(height=500, width=2000,x=1, y=150)

Button(welcome_frame, text= "Proceed to Login", width = 20, bg ="orange", \
       height = 5,font=("Open Sans", 20), command = _gotologin) \
        .place(x= 690, y=1)
Button(welcome_frame, text= "Getting Started", width = 20, bg ="#BE0DF6", \
       height = 5,font=("Open Sans", 20), command = _gettingstarted) \
           .place(x= 340, y=1)
           
'''
# Getting Started frame
'''
gettingstarted = ttk.Frame(home, style ='new.TFrame') # create frame for the first home page view
# Gettin starter message
start_message = \
''' 
This is the Database system of Innovations for Poverty Action Ghana\n
Powered by the Research Quality Department(ghrqteam@poverty-action.org). \n
Continue to login using your username and password.\n
After loging in, use the various buttons to navigate to \n
the page or tab of your interest. Kindly note that your access \n
to a page or tabs depends on the permission you have\n

'''
head = Label(gettingstarted, text= start_message, fg = "#047B0A", bg = "#AFEEEE", \
     justify = "left",font=("Open Sans", 14, "italic", "bold")) \
      .place(x= 400, y=40)
Button(gettingstarted, text= "Back", width = 10, bg ="#ACAF04", \
       height = 2,font=("Open Sans", 20), command = _backtohome) \
           .place(x= 1000, y=350)


#Header
header = ttk.Frame(home, style ='new.TFrame')
#header.grid(row = 1, column = 3, columnspan = 7)
head = Label(header, text="IPA Ghana Database System",bg = "#AFEEEE", font=("Open Sans", 27)) \
     .grid(column =2, row =0, columnspan = 5)
header.place(height=50, width=500, x=500, y=5)



'''
=====================
    Login Frame
=====================
'''
# define function to get back to welcome screen
def _loginback():
    login_frame.place_forget()
    welcome_frame.place(height=500, width=2000,x=1, y=150)

username = StringVar()  # set username as string variable
password = StringVar() # set  password as string variable
login_frame = ttk.Frame(home, style ='new.TFrame')  ## this frame will show after clicking  the proceed button

Label(login_frame, text="Login",bg = "#AFEEEE",  font=("Open Sans", 18)).grid(column = 5, row =5, columnspan =2)
Label(login_frame, text="Username",bg = "#AFEEEE", font=("Open Sans", 15)).grid(column = 5, row =6)
Label(login_frame, text="Password",bg = "#AFEEEE", font=("Open Sans", 15)).grid(column = 5, row =7)
Entry(login_frame, width = 40, textvariable = username).grid(column = 6, row =6)
Entry(login_frame, width = 40, textvariable = password).grid(column = 6, row =7)
#Get back button
Button(login_frame, text= "Back", width = 10, bg ="#ACAF04", \
       height = 2,font=("Open Sans", 20), command = _loginback) \
           .place(x= 600, y=300)


# define accepted the login  details
def _login():
    
    user = username.get()
    pw = password.get()
    
        # Users who can access STS recuitment
    if user == "m" and pw == "g":
    
       login_frame.place_forget()          # Hide the Log in frame
       header.place_forget()               #Hide the header frame
       home_frame_head.place(height=70, width=1000,x=300, y=5) # shoe the home frame 
       home_frame.place(height=500, width=2000,x=1, y=150) # shoe the homw frame       
              
       #Other  Users
    elif user == "" and pw == "":
        
       login_frame.place_forget()          # Hide the Log in frame
       header.place_forget()               #Hide the header frame
       home_frame_head.place(height=70, width=1000,x=300, y=5) # shoe the home frame 
       home_frame.place(height=500, width=2000,x=1, y=150) # shoe the homw frame       
       recruit_button = Button(home_frame, text= "Research Quality Team",state = DISABLED, width = 25, bg ="#BE0DF6", \
                    height = 8,font=("Open Sans", 15, "bold"), command = _stsshortlist) \
                    .place(x= 340, y=1) # place the second button 300 spaces to your right

       
    else:
        msg.showinfo("invalid","Invalid username or passwoord. Please try again\
                     Kidly contact ghrqteam@poverty-action.org for help")

# create the login buton
Button(login_frame, text= "Submit",font=("Open Sans", 20), width = 15, bg ="light green", height = 2, \
       command = _login).grid(column = 6, row =8, columnspan =2)

'''
========================================
Create a home page and Hide it temporary
========================================
'''
# the header frame for the home page
home_frame_head = ttk.Frame(home, style ='new.TFrame')
# Brief aboout the page
brief = Label(home_frame_head, text= "Welcome to  the Database of Innovation for Poverty Action Ghana\n \
              Powered by the Research Quality Department",fg='white',bg = "green", \
               font=("Open Sans", 20, "bold")).grid(column = 1, row =1 )


'''
==========================
## Navigation between tabs
==========================
'''
    # function to control sts database
def _stsdatabase():
    tabcontrol.tab(1, state="normal") #activate the sts database tab
    tabcontrol.tk_focusNext           # switch to the sts database tab
    tabcontrol.tab(0, state="hidden") # hide the home tab
    
    # function to control comunity Database
def  _commdatabase():
    tabcontrol.tab(3, state="normal") # activate the communitytab
    tabcontrol.tk_focusNext           # switch to the comunity tab
    tabcontrol.tab(0, state="hidden") # hide the home tab
    
    # function to control sts_shortlisting    
def _stsshortlist():
    tabcontrol.tab(2, state="normal") # activate the shortlist tab
    tabcontrol.tk_focusNext           # switch to the shortlist tab
    tabcontrol.tab(0, state="hidden") # Hide the home tab


    # function to control ltsdatabase
def _ltsdatabase():
    tabcontrol.tab(4, state="normal") # activate the LTS database tab
    tabcontrol.tk_focusNext           # switch to the lts database tab
    tabcontrol.tab(0, state="hidden") # hide the home tab
   
    # function to controlback home
def _backtohome():
    tabcontrol.tab(0, state="normal") # Show the home tab
    tabcontrol.tab(1, state="hidden") # hide the sts database tab
    tabcontrol.tab(2, state="hidden") # hide the recruitment tab
    tabcontrol.tab(3, state="hidden") # hide the Comunity database tab
    tabcontrol.tab(4, state="hidden") # hide the LTS database tab
    tabcontrol.tab(5, state="hidden") # hide the position tab
    tabcontrol.tab(6, state="hidden") # hide the position tab
    tabcontrol.tab(7, state="hidden") # hide the position tab

def _homeback():
    # this line will reactivate recruit button before going back
    recruit_button = Button(home_frame, text= "STS Shortlisting", width = 25, bg ="#BE0DF6", \
                    height = 8,font=("Open Sans", 15, "bold"), command = _stsshortlist) \
                    .place(x= 340, y=1) # place the second button 300 spaces to your right
    
    home_frame.place_forget() # hide the home frame
    home_frame_head.place_forget() # hide the home head frame
    login_frame.place(height=900, width=2000, x=450, y=109) # activate the login frame
    header.place(height=50, width=500, x=480, y=5) # Activate the login header frame


''' 
==================================
Create Navigation tabs and buttons
==================================
'''

home_frame = ttk.Frame(home, style ='new.TFrame')

sts_button = Button(home_frame, text= "STS Database", width = 25, bg ="#1E90FF", \
                    height = 8,font=("Open Sans", 15, "bold"), command = _stsdatabase) \
                    .place(x=10, y=1) 
recruit_button = Button(home_frame, text= "Research Quality Team", width = 25, bg ="#BE0DF6", \
                    height = 8,font=("Open Sans", 15, "bold"), command = _stsshortlist) \
                    .place(x= 340, y=1) # place the second button 300 spaces to your right
comm_button = Button(home_frame, text= "Community Database", width = 25, bg ="orange", \
                     height = 8,font=("Open Sans", 15, "bold"), command = _commdatabase) \
                     .place(x= 670, y=1) # place the third button 600 spaces to your right
lts_button = Button(home_frame, text= "LTS Database", width = 25, bg ="#98EC04", \
                    height = 8,font=("Open Sans", 15,"bold"), command = _ltsdatabase) \
                    .place(x= 1000, y=1) # place the fourth button 900 spaces to your right


#Get back button
Button(home_frame, text= "Back", width = 10, bg ="#ACAF04", \
       height = 2,font=("Open Sans", 20), command = _homeback) \
           .place(x= 1050, y=250)

home_copywrite = ttk.Frame(home, style ='new.TFrame')
home_copywrite.place(x=1100, y=550)
# Brief aboout the page
brief = Label(home_copywrite, text= "© ipa-ghana 2020", bg= '#AFEEEE', \
               font=("Open Sans", 14)).grid(column = 1, row =1 )



''' 
==============================
### Design STS Database tab
==============================
'''

Button(sts_database, text= "Back", width = 10, bg ="#ACAF04", \
       height = 2,font=("Open Sans", 20), command = _backtohome) \
           .place(x= 800, y=400)



''' 
==============================
### Design STS Recruitment tab
==============================
'''
Button(sts_recruit, text= "Back", width = 10, bg ="#ACAF04", \
       height = 2,font=("Open Sans", 20), command = _backtohome) \
           .place(x= 800, y=400)



''' 
=====================================
### Design Community Database tab
=====================================
'''
import mysql.connector
from mysql.connector import (connection)
from mysql.connector import errorcode

# Define connection parameters
c_host     = 'bg4x5adl6spmuurgaqgp-mysql.services.clever-cloud.com'
c_database = 'bg4x5adl6spmuurgaqgp'
c_user     = 'uqovgyawkglrtuzv'
c_passwd   = 'VawVfxZ1lqU3jhy3IIRy'


# define function to connect to SQ
def _sqlconnect_comm():  
        #get input to connect to database
    '''
    c_host     = comm_host.get()
    c_database = comm_db_name.get()
    c_user     = comm_user.get()
    c_passwd   = comm_pwd.get()
    '''

    # Auto connection parameters
    
    try:
        commdb = mysql.connector.connect(
                host= c_host,
                user= c_user,
                passwd= c_passwd,
                database= c_database)
        mycursor = commdb.cursor()
        #msg.showinfo("Success", "Connection to " + database + " Databse successful")
            # Hide the connection frame and display the query frame
        comm_sql_connect.place_forget()
        comm_welcome_frame.place(height=500, width=2000,x=1, y=150)
        commdb.close()

        # Through Error Messages if connection fails
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            msg.showinfo("Connection Error", "Something Went wrong: invalid username or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            msg.showinfo("Connection Error", "Something Went wrong: Database does not exist")
        else:
            msg.showinfo("Connection Error", "Something Went wrong: {}".format(err) )


'''
=================================
  Page to connect to database 
=================================
'''
# Create a frame to hold connection wigets
comm_sql_connect = ttk.Frame(comm_database, style ='new.TFrame')
comm_sql_connect.place(height=500, width=700, x=450, y=109)

    # Create button to submit inputs
Button(comm_sql_connect, text= "Connect to Database",font=("Open Sans", 20), width = 20, bg ="light green", height = 2, \
       command = _sqlconnect_comm).grid(column = 6, row =11, columnspan =4, rowspan=3)

    # Back to Database home button
con_back = Button(comm_database, text= "Back", width = 10, bg ="#ACAF04", \
       height = 2,font=("Open Sans", 20), command = _backtohome) \
           .place(x= 800, y=450)

'''
===========================================
# Create a home page for comunity Database
===========================================
'''
# Define functions for navigation
def _comm_search():
    comm_sql_query.place(height=850, width=1000, x=450, y=109)
    comm_welcome_frame.place_forget()

def _comm_append():
    comm_welcome_frame.place_forget()
    comm_append_frame.place(height=500, width=2000,x=1, y=150)

# define a function to navigate back
def _comm_welc_back():
    comm_welcome_frame.place_forget() # Hide the welcome frame
    comm_sql_connect.place(height=600, width=600, x=450, y=109) # show the conection frame

# Create frame to display and allow navigation
comm_welcome_frame = ttk.Frame(comm_database, style ='new.TFrame')

Button(comm_welcome_frame, text= "Search Database", width = 20, bg ="orange", \
       height = 5,font=("Open Sans", 20), command = _comm_search) \
        .place(x= 340, y=1)
Button(comm_welcome_frame, text= "Append Database", width = 20, bg ="#BE0DF6", \
       height = 5,font=("Open Sans", 20), command = _comm_append) \
           .place(x= 690, y=1)

Button(comm_welcome_frame, text= "Back", width = 10, bg ="#ACAF04", \
       height = 2,font=("Open Sans", 20), command = _comm_welc_back) \
           .place(x= 1050, y=250)


'''
=====================
# Create append frame
=====================
'''
comm_append_frame = ttk.Frame(comm_database, style ='new.TFrame')

# Define function to navigate back
def  _comm_append_back():
    comm_append_frame.place_forget()
    comm_welcome_frame.place(height=500, width=2000,x=1, y=150)   
    # Back button
Button(comm_append_frame, text= "Back", width = 10, bg ="#ACAF04", \
       height = 2,font=("Open Sans", 20), command = _comm_append_back) \
           .place(x= 1050, y=250)


'''
====================
# Create query frame
====================
'''
# Define function to handle query
def _sqlquery_comm():
    comm_sql_query.place_forget() # hide query criteria
    
    # Execute Query 
    commdb = mysql.connector.connect(
        host= c_host,
        user= c_user,
        passwd= c_passwd,
        database= c_database)
    
    comm_cursor = commdb.cursor()
    comm_cursor = commdb.cursor()
    comm_cursor.execute("SELECT * FROM communities")
    myresult = comm_cursor.fetchall()

    # Extract column names
    comm_columns = comm_cursor.description
    comm_col_names = [i[0] for i in comm_columns]
    
    _sql_query_out = ttk.Frame(comm_database, style ='new.TFrame')
    _sql_query_out.place(x=1, y=1, width = 2000, height = 2000)


    # Create a treeview and set the column names
    comm_tree = ttk.Treeview(_sql_query_out, columns = comm_col_names, height = 20)
        # Show columns
    comm_tree['show'] = 'headings'
        #Loop through the column name and rename all columns
    for col in comm_col_names: 
        comm_tree.heading(col, text=col)

    cpt = 0 # Counter representing the ID of your code.
    for row in myresult:
        datt = row
         # Insert the rows 
        comm_tree.insert('', 'end', values=row)
        #comm_tree.insert('', 'end', text=str(cpt), values=(row[1], row[2], row[3],row[4]))
        cpt += 1 # increment the ID
    comm_tree.place(x= 1, y=50, width = 2000, height = 505)
    
    comm_scroll_h = ttk.Scrollbar(_sql_query_out, orient ="horizontal", command = comm_tree.xview)
    comm_scroll_h.place(x= 380, y=570, width = 600 )
    comm_tree.configure(xscrollcommand = comm_scroll_h)
    
    # get query results as a list and save if applicable
    comm_query_results = []
    for value in myresult:
        tmp = {}
        for (index,column) in enumerate(value):
            tmp[comm_columns[index][0]] = column
        comm_query_results.append(tmp)
    #print(result)
    #print(myresult)

    def save(): 
        files = [('CSV File', '*.csv'), 
                 ('All Files', '*.*')] 
        comm_file = asksaveasfile(mode = 'w', filetypes = files, defaultextension = '.csv') 
        #print(file)
        comm_df = pd.DataFrame(comm_query_results)
        comm_df.to_csv (comm_file, index = True, header=True)
        msg.showinfo("Export complete", "Query Export Complete \n Data saved in" + str(comm_file))
        
    #comm_query_results.to_csv(comm_file)
     
    Button(_sql_query_out, text= "Export Results", width = 14, bg ="orange", \
       height = 1,font=("Open Sans", 20), command = lambda : save()) \
           .place(x= 100, y=560)

    res_label =Label(_sql_query_out, text= "Query Results", font=("Open Sans", 22, "bold"),bg = "#AFEEEE")
    res_label.place(x= 200, y=1, width = 1000, height = 35)

    # Success Message
    msg.showinfo("Succesfull", "Query Successfull")

        # Function to return back to query criteria
    def comm_out_back():
        _sql_query_out.place_forget()
        comm_sql_query.place(height=850, width=1000, x=450, y=109)
    
    Button(_sql_query_out, text= "Back", width = 10, bg ="#ACAF04", \
       height = 1,font=("Open Sans", 20), command = comm_out_back) \
           .place(x= 1100, y=560)
 


# define the back navigatio fumction
def _comm_query_back():
    comm_sql_query.place_forget()
    comm_welcome_frame.place(height=500, width=2000,x=1, y=150)  

# Define variables
comm_name = StringVar()
comm_region = StringVar() 
comm_district = StringVar()
comm_project = StringVar() 
comm_pr_phase = StringVar()
comm_market = StringVar()
comm_conflict = StringVar()
comm_taboo = StringVar()
# Create a frame to hold connection wigets
comm_sql_query = ttk.Frame(comm_database, style ='new.TFrame')
# Header
Label(comm_sql_query, text="Enter Search Criteria",bg = "#AFEEEE",justify = CENTER, \
     font=("Open Sans", 18, "bold")).grid(column = 5, row =4, columnspan =3)
Label(comm_sql_query, text="Community Name",bg = "#AFEEEE", anchor=W,justify = LEFT, \
      font=("Open Sans", 15)).grid(sticky =W, column = 5, row =6)
Label(comm_sql_query, text="Region", anchor=W,justify = LEFT,bg = "#AFEEEE", \
      font=("Open Sans", 15)).grid(sticky = W, column = 5, row =7)
Label(comm_sql_query, text="District", anchor=W,justify = LEFT,bg = "#AFEEEE", \
      font=("Open Sans", 15)).grid(sticky= W,column = 5, row =8)
Label(comm_sql_query, text="Project", anchor=W,justify = LEFT,bg = "#AFEEEE", \
      font=("Open Sans", 15)).grid(sticky = W ,column = 5, row =9)
Label(comm_sql_query, text="Project Phase", anchor=W,justify = LEFT,bg = "#AFEEEE", \
      font=("Open Sans", 15)).grid(sticky = W ,column = 5, row =10)
Label(comm_sql_query, text="Market Day", anchor=W,justify = LEFT,bg = "#AFEEEE", \
      font=("Open Sans", 15)).grid(sticky = W ,column = 5, row =11)
Label(comm_sql_query, text="Taboo Day", anchor=W,justify = LEFT,bg = "#AFEEEE", \
      font=("Open Sans", 15)).grid(sticky = W ,column = 5, row =12)
Label(comm_sql_query, text="Conflict Status", anchor=W,justify = LEFT,bg = "#AFEEEE", \
      font=("Open Sans", 15)).grid(sticky = W ,column = 5, row =13)

# Name entry
Entry(comm_sql_query, width = 40, textvariable = comm_name).grid(column = 6, row =6, columnspan =2)

    # Defining dropdown options
comm_regions = ["Ashianti", "Brong Ahafo", "Central", "Eastern", "Greater Accra", \
                "Northern" ,"Volta", "Upper East", "Upper West", "Western"]
comm_projects = ["STARS", "SMEG", "QP4G", "FARMERLINE", "EP", \
                "TRaCTA" ,"TIF", "GEP", "GCCPS", "GYS", "Other(Specify)"]
comm_pr_phases = ["Pilot", "Baseline", "Endline", "Mobilization", "Round/Stage(specify)","Other(specify)"]
comm_conflict_status = ["Calm", "Mild conflict", "Severe Conflict", "War zone"]
comm_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

ttk.Combobox(comm_sql_query, width= 38, textvariable = comm_region , values = comm_regions) \
                        .grid(column = 6, row =7, columnspan =2)
ttk.Combobox(comm_sql_query, width= 38, textvariable = comm_district , values = comm_regions) \
                        .grid(column = 6, row =8, columnspan =2)
ttk.Combobox(comm_sql_query, width= 38, textvariable = comm_project , values = comm_projects) \
                        .grid(column = 6, row =9, columnspan =2)
ttk.Combobox(comm_sql_query, width= 38, textvariable = comm_pr_phase , values = comm_pr_phases) \
                        .grid(column = 6, row =10, columnspan =2)
ttk.Combobox(comm_sql_query, width= 38, textvariable = comm_conflict , values = comm_conflict_status) \
                        .grid(column = 6, row =11, columnspan =2)
ttk.Combobox(comm_sql_query, width= 38, textvariable = comm_taboo , values = comm_days) \
                        .grid(column = 6, row =12, columnspan =2)
ttk.Combobox(comm_sql_query, width= 38, textvariable = comm_market , values = comm_days) \
                        .grid(column = 6, row =13, columnspan =2)
    # Create search Buttoon
Button(comm_sql_query, text= "Search",font=("Open Sans", 20), width = 15, bg ="light green", height = 1, \
       command = _sqlquery_comm).grid(column = 6, row =14, columnspan =2)
    # Back button
Button(comm_sql_query, text= "Back",font=("Open Sans", 20), width = 10, bg ="#ACAF04", height = 2, \
       command =  _comm_query_back).grid(column = 10, row =20, columnspan =2)

''' #################################
### Design LTS Database tab
######################################
'''
Button(lts_database, text= "Back", width = 10, bg ="#ACAF04", \
       height = 2,font=("Open Sans", 20), command = _backtohome) \
           .place(x= 800, y=400)

# Master

# Header
head = Label(sts_recruit, text="IPA Ghana Recruitment", fg='white',bg = "green", font=("Open Sans", 22)) \
     .grid(column =0, row =0, columnspan =5)

'''
========================
     Project Details
========================
'''
    # Project details variabvles
pr_acronym   = StringVar() 
pr_code      = StringVar()
pr_grant     = StringVar()  
pr_office    = StringVar()
pr_phase     = StringVar() 
pr_subphase  = StringVar()

details_frame = ttk.Labelframe(sts_recruit, text = "Project Details")
details_frame.grid(column =0, row=1)

# Defining entry fields for Project details
Label(details_frame, text="Project Acronym", font=("Open Sans", 13)) \
     .grid(column = 1, row =2)
ttk.Entry(details_frame, width = 30, textvariable = pr_acronym).grid(column = 2, row =2)

Label(details_frame, text="Project Code", font=("Open Sans", 13)) \
     .grid(column = 1, row =3)
ttk.Entry(details_frame, width = 30, textvariable = pr_code).grid(column = 2, row =3)

Label(details_frame, text="Project Grant", font=("Open Sans", 13)) \
     .grid(column = 1, row =4)
ttk.Entry(details_frame, width = 30, textvariable = pr_grant).grid(column = 2, row =4)

Label(details_frame, text="Project Office", font=("Open Sans", 13)) \
     .grid(column = 1, row =5)  
offices = ["Accra", "Tamale"]
ttk.Combobox(details_frame, width= 27, values = offices, textvariable = pr_office) \
    .grid(column = 2, row =5)

Label(details_frame, text="Project Phase", font=("Open Sans", 13)) \
     .grid(column = 1, row =6)
phases = ["Pilot", "Census" "Baseline" , "Midline", "Endline", "Follow up", "Intervention Activities", " "]
ttk.Combobox(details_frame, width= 27,  values = phases, textvariable = pr_phase) \
                        .grid(column = 2, row =6)

Label(details_frame, text="Sub Phase(Opt)", font=("Open Sans", 13)) \
     .grid(column = 1, row =7)
ttk.Entry(details_frame, width = 30, textvariable = pr_subphase).grid(column = 2, row =7)


'''
=============================
Activity Details entry fields
=============================
'''
pr_submit          = StringVar() 
pr_training        = StringVar() 
pr_field_work      = StringVar()
pr_duration_number = StringVar() 
pr_duration_weeks  = StringVar() 

activity_frame = ttk.Labelframe(sts_recruit, text = "Activity Details")
activity_frame.grid(column =0, row =2)

Label(activity_frame, text="Submission Date", font=("Open Sans", 13)) \
     .grid(column = 1, row =10)
ttk.Entry(activity_frame, width = 30, textvariable = pr_submit).grid(column = 2, row =10)

Label(activity_frame, text="Date of Training", font=("Open Sans", 13)) \
     .grid(column = 1, row =11)
ttk.Entry(activity_frame, width = 30, textvariable = pr_training).grid(column = 2, row =11)

Label(activity_frame, text="Date of Field Work", font=("Open Sans", 13)) \
     .grid(column = 1, row = 12)
ttk.Entry(activity_frame, width = 30, textvariable = pr_field_work).grid(column = 2, row =12)

Label(activity_frame, text="Duration of Activities", font=("Open Sans", 13)) \
     .grid(column = 1, row =13)
duration_type = ["units", "Days", "Weeks" , "Months"]
duration_number = ["1", "2", "3", "4", "5","6" ,"7", "8", "9", "10", "11" , "12" ]
ttk.Combobox(activity_frame, width= 27, textvariable = pr_duration_number , values = duration_number) \
                        .grid(column = 2, row = 13)
ttk.Combobox(activity_frame, width= 27 , textvariable = pr_duration_weeks, values =duration_type) \
                        .grid(column = 2, row = 14)


'''
=============================
Project Staff entry fields
=============================
'''
    #Project staff variables
pr_fm        = StringVar()
pr_head      = StringVar()
pr_manager   = StringVar()
pr_sc        = StringVar()

staff_frame = ttk.Labelframe(sts_recruit, text = "Project Staff")
staff_frame.grid(column =1, row = 1)

Label(staff_frame, text="Field Manager", font=("Open Sans", 13)) \
     .grid(column = 3, row =2)
ttk.Entry(staff_frame, width = 30, textvariable = pr_fm).grid(column = 4, row =2)

Label(staff_frame, text="Project Head", font=("Open Sans", 13)) \
     .grid(column = 3, row =3)
ttk.Entry(staff_frame, width = 30, textvariable = pr_head).grid(column = 4, row =3)

Label(staff_frame, text="Project Manager", font=("Open Sans", 13)) \
     .grid(column = 3, row =4)
ttk.Entry(staff_frame, width = 30, textvariable = pr_manager).grid(column = 4, row =4)

Label(staff_frame, text="Survey Coordinator", font=("Open Sans", 13)) \
     .grid(column = 3, row =5)
ttk.Entry(staff_frame, width = 30, textvariable = pr_sc).grid(column = 4, row =5)



'''
=============================
Brief Description
=============================
'''
description = StringVar()

desc_frame = ttk.Labelframe(sts_recruit, text = "Description of Project")
desc_frame.grid(column =1, row = 2)
#frame1.configure(background = "light blue")

Label(desc_frame, text="Brief Description of Survey Activities", font=("Open Sans", 14)) \
     .grid(column = 3, row = 7)

description = scrolledtext.ScrolledText(desc_frame, width = 40, height = 15, wrap =tk.WORD) \
                .grid(column = 3, columnspan = 29, row = 9,rowspan = 14)




'''
Adding New Tab for each of the recruitment requests

'''
# Set quit to quit
def _quit():
    win.quit()
    win.destroy()
    exit()

menu_bar = Menu(win)
win.config(menu = menu_bar)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label ="Refresh")
file_menu.add_command(label ="New")
file_menu.add_command(label ="Quit", command = _quit)
menu_bar.add_cascade(label = "File", menu =file_menu)

# Help Menu
def _about():
    
    help = \
    '''     Version 1.0.0.1 
    
    This database system is a python GUI program that
    connects to the SQL the various databases IPA Ghana
    and provides a user friendly way of searching the 
    databasese, appending and conducting shortlisting 
    of short term staff.
    '''
    
    msg.showinfo("About IPAG MERS",help)
    print("That's the help button")

help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label ="About", command = _about)
menu_bar.add_cascade(label = "Help", menu =help_menu)


# adda submit button
def submit_details():  
    proj_acronym = pr_acronym.get()
    proj_code    = pr_code.get()
    proj_grant   = pr_grant.get()
    proj_office  = pr_office.get()
    proj_phase   = pr_phase.get()
    proj_subphase= pr_subphase.get()
    proj_fm      = pr_fm.get()
    proj_head    = pr_head.get()
    proj_manager = pr_manager.get()
    proj_sc      = pr_sc.get()
    proj_submit  = pr_submit.get()
    proj_training= pr_training.get() 
    proj_field_work = pr_field_work.get()
    proj_duration_number = pr_duration_number.get() 
    proj_duration_weeks  = pr_duration_weeks.get()
    
    print("Acro is "+ proj_acronym + "\nFM is " +proj_office  )   

#btn = ttk.Button(master, text="Add Tab", command = _addtab)
#btn.grid(column = 1, row = 15 , columnspan = 3 )

btn = ttk.Button(sts_recruit, text="Submit", command = submit_details)
btn.grid(column = 5, row = 15 , columnspan = 5 )




'''
######################
Request Tabs
######################
'''
#tabs = "123456"

#for rep in range(1,6):
#     print(rep)
     # Header


                                    
#ttk.Button(win, text = "Submit", command = quit).grid(column = 100, row =307)
win.title('IPA Ghana Database System')
win.configure(background = "light blue")
win.geometry("2000x700")
#win.resizable(False, False) # Prevent resizing 

win.mainloop()
