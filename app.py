from flask import Flask,request , Response
import mariadb
import dbcreds
import json

app = Flask(__name__)

@app.route("/api/qoute",methods=["POST","get"])
def post():
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





