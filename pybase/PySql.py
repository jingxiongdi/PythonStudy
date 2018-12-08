import sqlite3

#表示创建一个数据库,并获得连接
connection = sqlite3.connect("ab.db")

cursor = connection.cursor()
#创建表
#sql =  "create table company( 'id' int primary key not null,'name' text not null,'salary' text not null)"
#cursor.execute(sql)
#connection.commit()
#connection.close()

#查询
# c = cursor.execute("SELECT id, name, salary  from company")
# for row in c:
#    print("ID = ", row[0])
#    print("NAME = ", row[1])
#    print("SALARY = ", row[2], "\n")

#插入操作
#c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#      VALUES (1, 'Paul', 32, 'California', 20000.00 )");
#更新操作
#c.execute("UPDATE COMPANY set SALARY = 25000.00 where ID=1")

#删除操作
#c = cursor.execute("DELETE from company")


