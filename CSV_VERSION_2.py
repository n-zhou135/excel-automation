#many required imports
import tkinter as tk
from tkinter import filedialog
import os
from tkinter import messagebox

def Read_DynamicMod_Value(filePath): #this reads the values of the dynamic modulus values
    fileInfo = [] #initializing variables and setting file path for reading
    regroupDyn = ""
    readingFile = open(filePath, "r") 

    for line in readingFile: #reading the csv file line by line and storing it in a list
        fileInfo.append(line)

    dynamicMod = str(fileInfo[28]) #given that the dynamic mod values will always be on a specific line, this finds and reads the numbers only from that line
    splitDyn = dynamicMod.split(",")
    for value in range(1, len(splitDyn)):
        regroupDyn += str(splitDyn[value] + ", ")
    finalDyn = regroupDyn.replace("\n", "")
    
    readingFile.close()

    return finalDyn #returning the dynamic mod values (num only) from the line

def Add_All_DM_Strings(DMValues1, DMValues2, DMValues3): #this adds all the separate strings of dynamic mod values from the separate csv files into one final string
    superDM = DMValues1 + DMValues2 + DMValues3
    return superDM

def Read_PhaseAng_Value(filePath): #this reads the values of the phase angle values
    fileInfo = [] #initializing variables and setting file path for reading
    regroupPha = ""
    readingFile = open(filePath, "r")

    for line in readingFile: #reading the csv file line by line and storing in a list
        fileInfo.append(line)

    phaseVal = str(fileInfo[29]) #given that the dynamic mod values will always be on a specific line, this finds and reads the numbers only from that line
    splitPha = phaseVal.split(",")
    for thing in range(1, len(splitPha)):
        regroupPha += str(splitPha[thing] + ", ")
    finalPha = regroupPha.replace("\n", "")

    readingFile.close()

    return finalPha #returning the phase angle values (num only) from the line

def Add_All_PA_Strings(PAValues1, PAvalues2, PAValues3): #this adds all the separate strings of phase angle values from the separate csv files into one final string
    superPA = PAValues1 + PAvalues2 + PAValues3
    return superPA
    

def writingCSV(dirName, superDM, superPA): #this writes the final dynamic mod string and the final phase angle string into a final csv file

    writingFile = open(dirName + "/" + shortName + ".csv", "w") 
    writingFile.write(superDM + "\n")
    writingFile.write(superPA)

    writingFile.close()

root = tk.Tk()
root.withdraw()
dirName = filedialog.askdirectory(initialdir="/",title='Please select a directory') #choosing which files to read/getting the long file path
shortName = os.path.basename(dirName) #getting the shortened file path

DMValues1 = Read_DynamicMod_Value(dirName + "/4C/" + shortName + "_4C_Sum.csv") #reading separate dynamic mod values from different csv files
DMValues2 = Read_DynamicMod_Value(dirName + "/20C/" + shortName + "_20C_Sum.csv")
DMValues3 = Read_DynamicMod_Value(dirName + "/40C/" + shortName + "_40C_Sum.csv")

PAValues1 = Read_PhaseAng_Value(dirName + "/4C/" + shortName + "_4C_Sum.csv") #reading separate phase angle values from different csv files
PAValues2 = Read_PhaseAng_Value(dirName + "/20C/" + shortName + "_20C_Sum.csv")
PAValues3 = Read_PhaseAng_Value(dirName + "/40C/" + shortName + "_40C_Sum.csv") 

superDM = Add_All_DM_Strings(DMValues1, DMValues2, DMValues3) #creating final dynamic mod string
superPA = Add_All_PA_Strings(PAValues1, PAValues2, PAValues3) #creating final phase angle string

writingCSV(dirName, superDM, superPA) #writes the file

messagebox.showinfo("Message", "Done") #confirmation message