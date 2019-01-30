import Tkinter
import tkFileDialog
import os

root = Tkinter.Tk()
root.withdraw()
CSV_filetypes = [('all files', '.*'), ('csv files', '.csv')]
CSV_file_path = tkFileDialog.askopenfilename(parent=root, initialdir=os.getcwd(),
                                             title="Please select a file:", filetypes=CSV_filetypes)
root.destroy()
print CSV_file_path
