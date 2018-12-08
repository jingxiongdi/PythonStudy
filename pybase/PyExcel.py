#导入excel包
#from imp import reload
#import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')
import xlwt
import xlrd
#打开txt文件
#excel  = open("E:\\pythonWorkspace\\testFile\\test.txt")
#print(excel.name)
#可以读取文本文件.txt
#str = excel.read()
#print(str)
#关闭文件
#excel.close()

#打开excel读取数据
data = xlrd.open_workbook("E:\\pythonWorkspace\\testFile\\班级成绩表.xls")

#获取一个工作表
table = data.sheets()[0]          #通过索引顺序获取
#table = data.sheet_by_index(0) #通过索引顺序获取
#table = data.sheet_by_name(u'Sheet1')#通过名称获取
#获取行数和列数
nrows = table.nrows
ncols = table.ncols
print("行数 ：",nrows,"列数 : ",ncols)
# 循环行列表数据
#for i in range(nrows ):
#    print(table.row_values(i))

#单元格
#cell_A1 = table.cell(0,0).value
#cell_C4 = table.cell(2,3).value
#print("A1 : ",cell_A1,"C4",cell_C4)

#使用行列索引
#cell_A1 = table.row(0)[0].value
#cell_A2 = table.col(1)[0].value

#写入excel
# 类型 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
#ctype = 1
#value = '单元格的值'
#xf = 0 # 扩展的格式化
#table.put_cell(row, col, ctype, value, xf)

#创建一个新的excel,并且复制之前的excel
excelTabel= xlwt.Workbook()#创建excel对象
sheet1=excelTabel.add_sheet('班级成绩表')
for i in range(nrows ):
    for j in range(ncols ):
        sheet1.write(i,j,table.cell(i,j).value)
excelTabel.save("E:\\pythonWorkspace\\testFile\\test.xls")