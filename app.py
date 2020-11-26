from flask import Flask,request , Response
import mariadb
import dbcreds
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/qoute",methods=["POST","get"])
def qoutes():
    if request.method =="POST":

        data=request.json
        name = data.get("name")
        email = data.get("email")
        message = data.get("message")
        conn = None
        cursor = None
        result = None
        if name!="" and name !=None and email!="" and email !=None and message !="" and message !=None:
            
            try:
                conn = mariadb.connect(user=dbcreds.user,password=dbcreds.password, host=dbcreds.host,port=dbcreds.port, database=dbcreds.database)
                cursor = conn.cursor()
                cursor.execute("INSERT INTO qoute (name,email,message) VALUES (?,?,?) ",[name,email,message,])
                conn.commit()
                result = cursor.rowcount
            except mariadb.OperationalError as e:
                message = "connection error" 
            except Exception as e:
                message ="somthing went wrong" 
            finally:
                if(cursor != None):
                    cursor.close()
                if(conn != None):
                    conn.rollback()
                    conn.close()
                if(result == 1):
                    return Response("Success" ,mimetype="text/html",status=200)
                return Response(message ,mimetype="text/html",status=500)
        return Response("Something went wrong" ,mimetype="text/html",status=400)
    elif request.method == "GET" : 
        conn = None
        cursor = None
        result = None
                
        try:
            conn = mariadb.connect(user=dbcreds.user,password=dbcreds.password, host=dbcreds.host,port=dbcreds.port, database=dbcreds.database)
            cursor = conn.cursor()
            cursor.execute("SELECT * From qoute")
            result = cursor.fetchall()
        except mariadb.OperationalError as e:
            message = "connection error" 
        except Exception as e:
            message ="somthing went wrong" 
        finally:
            if(cursor != None):
                cursor.close()
            if(conn != None):
                conn.rollback()
                conn.close()
            if(result ):
                qoutes=[]
                for row in result : 
                    qoute ={
                    "name":row[0],
                    "email": row[2],
                    "message":row[1]
                    }
                    qoutes.append(qoute)
                return Response(json.dumps(qoutes,default=str) ,mimetype="application/json",status=200)
            return Response(message ,mimetype="text/html",status=500)

@app.route("/api/reviews",methods=["POST","get"])
def reviews():
    if request.method =="POST":

        data=request.json
        name = data.get("name")
        email = data.get("email")
        message = data.get("message")
        rate = data.get("rate")
        conn = None
        cursor = None
        result = None
        if name!="" and name !=None and email!="" and email !=None and message !="" and message !=None and rate !=None:
            
            try:
                conn = mariadb.connect(user=dbcreds.user,password=dbcreds.password, host=dbcreds.host,port=dbcreds.port, database=dbcreds.database)
                cursor = conn.cursor()
                cursor.execute("INSERT INTO reviews (name,email,message,rate) VALUES (?,?,?,?) ",[name,email,message,rate])
                conn.commit()
                result = cursor.rowcount
            except mariadb.OperationalError as e:
                message = "connection error" 
            except Exception as e:
                message ="somthing went wrong" 
            finally:
                if(cursor != None):
                    cursor.close()
                if(conn != None):
                    conn.rollback()
                    conn.close()
                if(result == 1):
                    return Response("Success" ,mimetype="text/html",status=200)
                return Response(message ,mimetype="text/html",status=500)
        return Response("Something went wrong" ,mimetype="text/html",status=400)
    elif request.method == "GET" : 
        conn = None
        cursor = None
        result = None
                
        try:
            conn = mariadb.connect(user=dbcreds.user,password=dbcreds.password, host=dbcreds.host,port=dbcreds.port, database=dbcreds.database)
            cursor = conn.cursor()
            cursor.execute("SELECT * From reviews")
            result = cursor.fetchall()
        except mariadb.OperationalError as e:
            message = "connection error" 
        except Exception as e:
            message ="somthing went wrong" 
        finally:
            if(cursor != None):
                cursor.close()
            if(conn != None):
                conn.rollback()
                conn.close()
            if(result ):
                reviews=[]
                for row in result : 
                    review ={
                    "id":row[0],
                    "name":row[1],
                    "email": row[2],
                    "message":row[3],
                    "rate":row[5],
                    "date": row[4]
                    }
                    reviews.append(review)
                return Response(json.dumps(reviews,default=str) ,mimetype="application/json",status=200)
            return Response(message ,mimetype="text/html",status=500)





