from datetime import datetime
import mysql.connector
from tracker import Tracker

now= datetime.now()
current_time = now.strftime("%H")



if(current_time == '13'):
    pass


# Connect to the MySQL server
connection = mysql.connector.connect(user='',
                              password='',
                              host='',
                              database='')

# Create a cursor object
cur = connection.cursor()

query = 'select Phone_Number,Expected_Price,Product_url,Product_Name,p.Product_Id from product p,notification n, user u where p.Product_Id = n.Product_Id and u.User_Id = p.User_Id '
cur.execute(query)
data = cur.fetchall()

print(data)




for record in data:
    product_name=record[3]
    product_url=record[2]
    expected_price=record[0]
    phone_number =record[1]
    product_id=record[4]

    track = Tracker(product_name,product_url,expected_price,phone_number)
    price = int(track.Update())

    # update_product = "UPDATE product SET current_price = %s WHERE Product_Id = %s"
    #
    # data_product = (price,product_id)
    # cur.execute(update_product,data_product)

    cur.execute("UPDATE product SET current_price = %s WHERE (Product_Id = %s)",(price,product_id))

    # Commit the changes
    connection.commit()








cur.close()
connection.close()








