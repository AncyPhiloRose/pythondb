import sqlite3
# create database and initialize cursor
def connection():
 try:
    conn= sqlite3.connect(r'C:/Users/Ancy/Desktop/python problems/dept_manager.db')
    c= conn.cursor()
    return c,conn
 except Exception as e:
     print("Error",e)

def mycode(c):
    try:
       str1=""
       a = c.execute('SELECT * FROM dept_manager')
       for row in a:
           b=','.join(row)
           str1=str1+b+'\n'
       return(str1)
    except Exception as e:
      print("Error",e)
if __name__ =='__main__':
    c,conn = connection()
    c.execute('Delete from dept_manager')
    c.execute(f'CREATE TABLE IF NOT EXISTS dept_manager( dept_no char,emp_no varchar,DOJ date)')
    with open('department.txt', 'r') as fr:
        for line in fr.readlines():
            # parse the results.txt, create a list of comma separated values
            fields = line.replace('\n', '').split(',')
            #print(fields)
            try:
                c.execute('INSERT INTO dept_manager (dept_no,emp_no,DOJ)'\
                       f"VALUES ('{fields[0]}','{fields[1]}','{fields[2]}')")

            except Exception as e:
                  print("Error",e)
    conn.commit()
    mycode(c)
    conn.close()