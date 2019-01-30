import csv
import Tkinter
import tkFileDialog
import os

root = Tkinter.Tk()
root.withdraw()
CSV_filetypes = [('all files', '.*'), ('csv files', '.csv')]
CSV_file_path = tkFileDialog.askopenfilename(parent=root, initialdir=os.getcwd(),
                                             title="Please select a file:", filetypes=CSV_filetypes)
root.destroy()

csvFile = open(CSV_file_path, "r")
reader = csv.reader(csvFile)
for csv_line in reader:
    print csv_line
csvFile.seek(os.SEEK_SET,0)
for csv_line in reader:
    print csv_line
csvFile.close()

with open(CSV_file_path, "r") as csvFile:
    reader = csv.reader(csvFile)
    for csv_line in reader:
        print csv_line
    csvFile.seek(os.SEEK_SET,0)
    for csv_line in reader:
        print csv_line
