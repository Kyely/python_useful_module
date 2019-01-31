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
                                             title="Please select a 200K latecy file:", filetypes=CSV_filetypes)
CSV_file_path_400K = tkFileDialog.askopenfilename(parent=root, initialdir=os.getcwd(),
                                             title="Please select a 400K latecy file:", filetypes=CSV_filetypes)
root.destroy()

latency_200K = []
latency_number_200K = []
latency_percentage_200K = []
latency_percentage_sum_200K = [0]
with open(CSV_file_path_200K, "r") as csvFile_200K:
    reader_200K = csv.reader(csvFile_200K)
    for csv_line_200K in reader_200K:
        # print csv_line
        latency_200K.append(int(csv_line_200K[0]))
        latency_number_200K.append(int(float(csv_line_200K[1])))
        latency_percentage_200K.append(float(csv_line_200K[2]))
        latency_percentage_sum_200K.append(latency_percentage_sum_200K[-1]+latency_percentage_200K[-1])
latency_percentage_sum_200K = latency_percentage_sum_200K[1:]

latency_400K = []
latency_number_400K = []
latency_percentage_400K = []
latency_percentage_sum_400K = [0]
with open(CSV_file_path_400K, "r") as csvFile_400K:
    reader_400K = csv.reader(csvFile_400K)
    for csv_line_400K in reader_400K:
        # print csv_line
        latency_400K.append(int(csv_line_400K[0]))
        latency_number_400K.append(int(float(csv_line_400K[1])))
        latency_percentage_400K.append(float(csv_line_400K[2]))
        latency_percentage_sum_400K.append(latency_percentage_sum_400K[-1]+latency_percentage_400K[-1])
latency_percentage_sum_400K = latency_percentage_sum_400K[1:]
####################################################
plt.figure(figsize=[8,4])
bar_para={}
# bar_para['edgecolor']=(0, 0, 0)
# bar_para['linewidth']= 1.0
bar_para['width']=4
bar_para_200K=bar_para.copy()
bar_para_200K['color']='darkorange'
bar_para_200K['label']='200k'
plt.bar(map(lambda x: x,latency_200K),map(lambda x: x*100, latency_percentage_200K),**bar_para_200K)
front_para = {'fontsize': 18}
# plt.title('Event numbers VS FIFO Occupancy',**front_para)
plt.title('Latency Distribution 200k',**front_para)
plt.ylabel('Event Percentage',**front_para)
plt.xlabel('Latency/ns',**front_para)

plt.axis([0, 400, 0, 72])
front_para_s = {'fontsize': 15}
plt.text(-5,72,r'%',**front_para_s)

plt.yticks(**front_para)
plt.xticks(**front_para)

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

# latency_200k_png_file =os.path.dirname(CSV_file_path_200K)+r'/latency_200k.png'
# fig1.savefig(latency_200k_png_file)

####################################################
plt.figure(figsize=[8,4])
bar_para={}
# bar_para['edgecolor']=(0, 0, 0)
# bar_para['linewidth']= 1.0
bar_para['width']=4
bar_para_400K=bar_para.copy()
bar_para_400K['color']='lightskyblue'
bar_para_400K['label']='400k'
plt.bar(map(lambda x: x,latency_400K),map(lambda x: x*100, latency_percentage_400K), **bar_para_400K)
front_para = {'fontsize': 18}
# plt.title('Event numbers VS FIFO Occupancy',**front_para)
plt.title('Latency Distribution 400k',**front_para)
plt.ylabel('Event Percentage',**front_para)
plt.xlabel('Latency/ns',**front_para)

plt.axis([0, 400, 0, 42])
front_para_s = {'fontsize': 15}
plt.text(-5,42,r'%',**front_para_s)
grid_para = {}
grid_para['b']=True
grid_para['which']='major'#'minor''both'
grid_para['axis'] = 'y'
grid_para['linestyle'] = '--'
plt.grid(**grid_para)
plt.gca().set_axisbelow(True)

plt.yticks(**front_para)
plt.xticks(**front_para)

legend_para={}
legend_para['fontsize']=18
legend_para['frameon']=False
plt.legend(**legend_para)

fig1=plt.gcf()
fig1.show()

# latency_400k_png_file =os.path.dirname(CSV_file_path_400K)+r'/latency_400k.png'
# fig1.savefig(latency_400k_png_file)

#######################################################################
plt.figure(figsize=[8,4])
line_para={}
line_para['linewidth']=2

line_para_200K = line_para.copy()
line_para_200K['color'] = 'darkorange'
line_para_200K['label'] = '200k'
line_para_200K['marker'] = 'o'
line_para_200K['markeredgecolor'] = 'k'
line_para_200K['markeredgewidth'] = 1
line_para_200K['markersize'] = 5
plt.plot(latency_200K,map(lambda x: x*100, latency_percentage_sum_200K),**line_para_200K)


line_para_400K = line_para.copy()
line_para_400K['color'] = 'lightskyblue'
line_para_400K['label'] = '400k'
line_para_400K['marker'] = '^'
line_para_400K['markeredgecolor'] = 'k'
line_para_400K['markeredgewidth'] = 1
line_para_400K['markersize'] = 5
plt.plot(latency_400K,map(lambda x: x*100, latency_percentage_sum_400K),**line_para_400K)

front_para = {'fontsize': 18}

plt.title('Latency cumulative Distribution',**front_para)
plt.ylabel('Event cumulative Percentage',**front_para)
plt.xlabel('Latency/ns',**front_para)

plt.axis([0, 400, -5, 105])
front_para_s = {'fontsize': 15}
plt.text(-5,105,r'%',**front_para_s)
#
plt.yticks(**front_para)
plt.xticks(**front_para)
#
grid_para = {}
grid_para['b']=True
grid_para['which']='major'#'minor''both'
grid_para['axis'] = 'y'
grid_para['linestyle'] = '--'
plt.grid(**grid_para)
plt.gca().set_axisbelow(True)
#
legend_para={}
legend_para['fontsize']=18
legend_para['frameon']=False
plt.legend(**legend_para)

fig1=plt.gcf()
fig1.show()

latency_cumulative_png_file =os.path.dirname(CSV_file_path_200K)+r'/latency_latency_cumulative_png_file.png'
fig1.savefig(latency_cumulative_png_file)