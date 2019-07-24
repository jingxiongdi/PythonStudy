# coding=utf-8
import sqlite3
import xlrd

connection = sqlite3.connect("blessing.db")
mycursor = connection.cursor()

pinganyeSql =  "create table pinganye( 'id' int primary key not null,'pinganye' text not null)"
yuandanSql = "create table yuandan( 'id' int primary key not null,'yuandan' text not null)"
shengdanSql = "create table shengdan( 'id' int primary key not null,'shengdan' text not null)"
chunjieSql = "create table chunjie( 'id' int primary key not null,'chunjie' text not null)"
yuanxiaoSql = "create table yuanxiao( 'id' int primary key not null,'yuanxiao' text not null)"
chuxiSql = "create table chuxi( 'id' int primary key not null,'chuxi' text not null)"
fuqinSql = "create table fuqin( 'id' int primary key not null,'fuqin' text not null)"
muqinSql = "create table muqin( 'id' int primary key not null,'muqin' text not null)"
qixiSql = "create table qixi( 'id' int primary key not null,'qixi' text not null)"
jiehunSql = "create table jiehun( 'id' int primary key not null,'jiehun' text not null)"
duanwuSql = "create table duanwu( 'id' int primary key not null,'duanwu' text not null)"
kaiyeSql = "create table kaiye( 'id' int primary key not null,'kaiye' text not null)"
qiaoqianSql = "create table qiaoqian( 'id' int primary key not null,'qiaoqian' text not null)"
xideguiziSql = "create table xideguizi( 'id' int primary key not null,'xideguizi' text not null)"
manyueSql = "create table manyue( 'id' int primary key not null,'manyue' text not null)"
zhongqiuSql = "create table zhongqiu( 'id' int primary key not null,'zhongqiu' text not null)"

colunmArr = ["pinganye","yuandan","shengdan","chunjie","yuanxiao","chuxi","fuqin","muqin","qixi",
             "jiehun","duanwu","kaiye","qiaoqian","xideguizi","manyue","zhongqiu"]
sqlArr = [pinganyeSql,yuandanSql,shengdanSql,chunjieSql,yuanxiaoSql,chuxiSql,fuqinSql,muqinSql,qixiSql,jiehunSql,
          duanwuSql,kaiyeSql,qiaoqianSql,xideguiziSql,manyueSql,zhongqiuSql]
connection.execute("BEGIN TRANSACTION;") # 关键点
for sqlStr in sqlArr:
    mycursor.execute(sqlStr)

data = xlrd.open_workbook("祝福语大全.xls")
sheetIndex = 0;

for tableName in data.sheet_names():
    table = data.sheets()[sheetIndex]
    nrows = table.nrows
    for valueIndex in range(0,nrows):
        print("tableName "+tableName+" valueIndex "+str(valueIndex))
        cell = table.cell(valueIndex,0)
        sttr2 = str(cell).replace("\\n\\t","")
        sttr3 = sttr2.replace("text:","")
        sqlData = sttr3.replace("\\xa0","")
        sqlAdd = "insert into "+colunmArr[sheetIndex]+" (id,"+colunmArr[sheetIndex]+") values ("+str(valueIndex)+","+sqlData+")"
        print(sqlAdd)
        mycursor.execute(sqlAdd)
    sheetIndex+=1
connection.execute("COMMIT;")  #关键点
connection.commit()
connection.close()