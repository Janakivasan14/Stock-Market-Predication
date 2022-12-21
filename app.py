from flask import Flask,render_template,request,make_response                                                                                                              
#from flask_mysqldb import MySQL   
import pred                                                                                  
                                                                           
                                                                                                         
                                                                                                 
app=Flask(__name__)                                                                                    
   
#app.secret_key = "zdcxfxfvxcvcvcv25562521cvbcgb2152521cggcg215252"
#mysql=MySQL(app)

#app.config['MYSQL_HOST']="localhost"
#app.config['MYSQL_USER']= "root"
#app.config['MYSQL_PASSWORD']="root"
#app.config['MYSQL_DB']="stock"                                                                                                   
                                                                                                              
@app.route('/')                                                                                          
def index():                                                                                               
        return render_template("index.html")                                                                 
                                                                                                            
                                                                                                                 
                                                                                                             
@app.route('/admin')                                                                                
def admin():                                                                                                 
    return render_template("admin.html")                                                                  
                                                                                                           
                                                                                                       
                                                                                                                
@app.route('/login',methods=["POST","GET"])                                       
def login():                                                                         
    if request.method=='POST':                                               
        email=request.form["name"]                                                                   
        password=request.form["password"]                                                                    
        cur=mysql.connection.cursor()
        n=cur.execute("SELECT * FROM register where email='"+email+"'")
        if n==0:
            return "<script>alert(\"Not Register\");window.location.href=\"/\";</script>"
        cur.execute("SELECT password FROM register where email='"+email+"'")
        psw=cur.fetchall()
        if password==psw[0][0]:
            data=pred.histo()
            
            cur.execute("SELECT * FROM stock_details")
            n=cur.fetchall()
            n=n[-1]
            print(n)
            rate=n[0]
            n1=rate.split()
            n_day=n1[0]
            n_day=n_day[-11:-2]
            d=n[1]
            d=d[:-1]
            da=d.split(",")
            dat=[]
            for i in da:
                dat.append(i[2:-2])
            h=n[2]
            h=h[:-1]
            hi=h.split(",")
            histo=[]
            for i in hi:
                histo.append(i[1:-2])
         

            p=n[3]
            p=p[:-1]
            pr=p.split(",")
            predict=[]
            for i in pr:
                predict.append(i[1:-2])
        

            cur.execute("SELECT * FROM stock_survey")
            sur=cur.fetchall()
            sur=sur[-1]
          
            return render_template("data.html",s=sur,pre=histo[-1],new=n_day,dates=data[0],prices=data[1],dat=dat,n=2000,m=400,histo=histo,pred=predict)                                                                 
        else:                                                                                             
            return("<script>alert(\"NOT EXIST\");window.location.href=\"/\";</script>")                 



@app.route('/register', methods=["POST","GET"])                                            
def register():                                                                                        
    if request.method=="POST":   
        name=request.form["name"]
        email=request.form["email"]  
        pnumber=request.form["pnumber"]                                                          
        password=request.form["password"]                                                             
        c_password=request.form["cpassword"]                                                              
        if password != c_password:
            return "<script>alert(\"password miss match\");window.location.href=\"/\";</script>"
        cur=mysql.connection.cursor()
        n=cur.execute("SELECT email FROM register where email='"+email+"'")
        print(n)
        if n==1:
            return "<script>alert(\"already registered\");window.location.href=\"/\";</script>"
        cur.execute('''
                        insert into register
                        (Username,Email,Password,Pnumber)
                        values(%s,%s,%s,%s)
                        ''',(name,email,password,pnumber))
        mysql.connection.commit()
        return "<script>alert(\"Register succesfully\");window.location.href=\"/\";</script>"
        






if __name__ == "__main__":
        app.run(debug=True)


