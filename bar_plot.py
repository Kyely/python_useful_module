#https://matplotlib.org/api/_as_gen/matplotlib.pyplot.html
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch
import csv
import Tkinter
import tkFileDialog
import os

root = Tkinter.Tk()
root.withdraw()
CSV_filetypes = [('all files', '.*'), ('csv files', '.csv')]
CSV_file_path_200K = tkFileDialog.askopenfilename(parent=root, initialdir=os.getcwd(),
                                             title="Please select a 200K fifo occupancy file:", filetypes=CSV_filetypes)
CSV_file_path_400K = tkFileDialog.askopenfilename(parent=root, initialdir=os.getcwd(),
                                             title="Please select a 400K fifo occupancy file:", filetypes=CSV_filetypes)
root.destroy()

fifo_occupancy_200K = []
fifo_number_200K = []
fifo_percentage_200K = []
with open(CSV_file_path_200K, "r") as csvFile_200K:
    reader_200K = csv.reader(csvFile_200K)
    for csv_line_200K in reader_200K:
        # print csv_line
        fifo_occupancy_200K.append(int(csv_line_200K[0]))
        fifo_number_200K.append(int(float(csv_line_200K[1])))
        fifo_percentage_200K.append(float(csv_line_200K[2]))

fifo_occupancy_400K = []
fifo_number_400K = []
fifo_percentage_400K = []
with open(CSV_file_path_400K, "r") as csvFile_400K:
    reader_400K = csv.reader(csvFile_400K)
    for csv_line_400K in reader_400K:
        # print csv_line
        fifo_occupancy_400K.append(int(csv_line_400K[0]))
        fifo_number_400K.append(int(float(csv_line_400K[1])))
        fifo_percentage_400K.append(float(csv_line_400K[2]))
####################################################
plt.figure(figsize=[8,4])
bar_para={}
bar_para['edgecolor']=(0, 0, 0)
bar_para['linewidth']= 1.0
bar_para['width']=0.4
bar_para_200K=bar_para.copy()
bar_para_200K['color']='darkorange'
bar_para_200K['label']='200k'
plt.bar(map(lambda x: x - 0.2,fifo_occupancy_200K),fifo_percentage_200K,**bar_para_200K)
bar_para_400K=bar_para.copy()
bar_para_400K['color']='lightskyblue'
bar_para_400K['label']='400k'
plt.bar(map(lambda x: x + 0.2,fifo_occupancy_400K),fifo_percentage_400K,**bar_para_400K)
# plt.axis([-1, 16, 0, 7000000])

front_para = {'fontsize': 18}
#plt.title('Event numbers VS FIFO Occupancy',**front_para)
plt.title('Event Percentage VS FIFO Occupancy ',**front_para)
plt.ylabel('Event Percentage',**front_para)
plt.xlabel('FIFO Occupancy',**front_para)

# plt.xlim(-1,16)
# plt.ylim(0,7100000)
# plt.xticks()

plt.xticks([0, 2, 4, 6, 8, 10, 12, 14, 16],**front_para)
ylable_numbers = ('0', '10', '20', '30', '40', '50', '60', '70')
plt.yticks([0., 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7],
            ylable_numbers, **front_para)

front_para_s = {'fontsize': 15}
# plt.text(-1.2,7300000,r'$\times 10^6 $',**front_para_s)
plt.text(-1.8,0.75,r'%',**front_para_s)

grid_para = {}
grid_para['b']=True
grid_para['which']='major'#'minor''both'
grid_para['axis'] = 'y'
grid_para['linestyle'] = '--'
plt.grid(**grid_para)
plt.gca().set_axisbelow(True)

legend_para={}
legend_para['fontsize']=18
legend_para['frameon']=False
plt.legend(**legend_para)

fig1=plt.gcf()
fig1.show()

fifo_occupancy_png_file =os.path.dirname(CSV_file_path_200K)+r'/fifo_occupancy.png'
fig1.savefig(fifo_occupancy_png_file)
####################################################
plt.figure(figsize=[8,4])
bar_para={}
bar_para['edgecolor']=(0, 0, 0)
bar_para['linewidth']= 1.0
bar_para['width']=0.4
bar_para['log']=True
bar_para_200K=bar_para.copy()
bar_para_200K['color']='darkorange'
bar_para_200K['label']='200k'
plt.bar(map(lambda x: x - 0.2,fifo_occupancy_200K),fifo_percentage_200K,**bar_para_200K)
bar_para_400K=bar_para.copy()
bar_para_400K['color']='lightskyblue'
bar_para_400K['label']='400k'
plt.bar(map(lambda x: x + 0.2,fifo_occupancy_400K),fifo_percentage_400K,**bar_para_400K)


front_para = {'fontsize': 18}
#plt.title('Event numbers VS FIFO Occupancy',**front_para)
plt.title('Event Percentage VS FIFO Occupancy ',**front_para)
plt.ylabel('Event Percentage',**front_para)
plt.xlabel('FIFO Occupancy',**front_para)

# plt.xlim(-1,16)
# plt.ylim(0,7100000)
# plt.xticks()

plt.xticks([0, 2, 4, 6, 8, 10, 12, 14, 16],**front_para)
# ylable_numbers = ('0', '10', '20', '30', '40', '50', '60', '70')
# plt.yticks([0., 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7],
#             ylable_numbers, **front_para)
plt.yticks(**front_para)
#
# front_para_s = {'fontsize': 15}
# # plt.text(-1.2,7300000,r'$\times 10^6 $',**front_para_s)
# plt.text(-1.8,0.75,r'%',**front_para_s)

grid_para = {}
grid_para['b']=True
grid_para['which']='major'#'minor''both'
grid_para['axis'] = 'y'
grid_para['linestyle'] = '--'
plt.grid(**grid_para)
plt.gca().set_axisbelow(True)

legend_para={}
legend_para['fontsize']=18
legend_para['frameon']=False
plt.legend(**legend_para)

fig1=plt.gcf()
fig1.show()

fifo_occupancy_log_png_file =os.path.dirname(CSV_file_path_200K)+r'/fifo_occupancy_log.png'
fig1.savefig(fifo_occupancy_log_png_file)
####################################################
