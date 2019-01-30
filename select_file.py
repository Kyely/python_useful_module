import Tkinter
import tkFileDialog
import os
import csv

root = Tkinter.Tk()
root.withdraw()
CSV_filetypes = [('all files', '.*'), ('csv files', '.csv')]
CSV_file_path = tkFileDialog.askopenfilename(parent=root, initialdir=os.getcwd(), title="Please select a file:", filetypes=CSV_filetypes)
root.destroy()

csvFile = open(CSV_file_path, "r")
reader = csv.reader(csvFile)
for csv_line in reader:
    print csv_line
