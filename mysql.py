import pymysql
import logging
conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="pyl82465", db="owei",charset='utf8mb4')

def insert(blog_source,content,author,imgurl):
    cursor = conn.cursor()
    
    # print("content:",content)

    sql= "INSERT INTO crawler_data ( blog_source ,content,author,imgurl ) VALUES ( '{0}','{1}','{2}','{3}') ".format(blog_source, content,author,imgurl)
    print("sql:",sql)
    cursor.execute(sql)
    #提交
    conn.commit()

def query(blog_source):
    cursor= conn.cursor()
    
    sql="select * from crawler_data where blog_source= '{0}' ".format(blog_source)
    print("sql:",sql)
    cursor.execute(sql)
    results=cursor.fetchall()
    result_content=[]
    for result in results:
        data = {
            "author":result[1],
            "content":result[2],
            "imgurl":result[3]
        }
        result_content.append(data)
        print(result[2])
    return result_content
    
    
    
    