from tkinter import *
from tkinter.filedialog import askdirectory
import tkinter.messagebox
import dicom
import os

def imagemodify():
    images_path = getValue(e1)   #原始文件路径
    images = 0  #总图像数目统计
    num = 1300000  #病人计数
    checkNo = int(getValue(StudyID))   #初始检查号
    SDate=getValue(StudyDate)
    for root, dirs, files in os.walk(images_path):
       
        if files:
            images_cnt = 0  #单文件图像数目统计
            filedirs = str(getValue(e2))+"/"+str(checkNo) #新建文件路径
            os.mkdir(filedirs)
            i =0
            for filename in files:
                if filename.endswith('.dcm') and i <10:
                    filepath = os.path.join(root, filename)
                    ds = dicom.read_file(filepath)

                    ds.PatientName = "patient"+str(num)+"_"+str(checkNo)
                    ds.StudyInstanceUID ="1.2.3.100651."+str(checkNo)
                    ds.PatientID = "p"+str(checkNo)
                    ds.StudyID = str(checkNo)
                    ds.SeriesInstanceUID = "0124"+str(checkNo)
                    ds.StudyDate = SDate

                    ds.save_as("{}/{}.dcm".format(filedirs,"patient"+str(num)+"_"+str(checkNo)))
                    images_cnt += 1
                    num += 1

                i +=1
            checkNo += 1

            images = images_cnt + images
            print(os.path.join(root,),"图像数量：{}".format(images_cnt))
    print("图像总数量为：{}".format(images))
    tkinter.messagebox.showinfo("message","修改完成")

def selectPath(path):
	path_=askdirectory()
	path.set(path_)

def getValue(e):
	value=e.get()
	return value

root = Tk()
root.geometry('320x250+800+200')
root.title("DICOM MODIFY")
select_path = StringVar()
save_path= StringVar()

Label(root,text="源文件路径:").grid(row=1,column=0,sticky=W)
e1=Entry(root,textvariable=select_path)
e1.grid(row=1,column=1)
Button(root,text="路径选择",command=lambda:selectPath(select_path)).grid(row=1,column=2)
Label(root,text="保存路径:").grid(row=2,column=0,sticky=W)
e2=Entry(root,textvariable=save_path)
e2.grid(row=2,column=1)
Button(root,text="路径选择",command=lambda:selectPath(save_path)).grid(row=2,column=2)

Label(root,text="PatientName").grid(row=3,sticky=W)
PatientName=Entry(root)
PatientName.grid(row=3,column=1,sticky=E)
Label(root,text="PatientID").grid(row=4,sticky=W)
PatientID=Entry(root)
PatientID.grid(row=4,column=1,sticky=E)
Label(root,text="StudyInstanceUID").grid(row=5,sticky=W)
StudyInstanceUID=Entry(root)
StudyInstanceUID.grid(row=5,column=1,sticky=E)
Label(root,text="SeriesInstanceUID").grid(row=6,sticky=W)
SeriesInstanceUID=Entry(root)
SeriesInstanceUID.grid(row=6,column=1,sticky=E)
Label(root,text="StudyID").grid(row=7,sticky=W)
StudyID=Entry(root)
StudyID.grid(row=7,column=1,sticky=E)
Label(root,text="StudyDate").grid(row=8,sticky=W)
StudyDate=Entry(root)
StudyDate.grid(row=8,column=1,sticky=E)

Button(root,text="执行",command=imagemodify).grid(row=10,column=0,sticky=E)
Button(root,text="退出",command=root.quit).grid(row=10,column=1,sticky=E) 

root.mainloop()
