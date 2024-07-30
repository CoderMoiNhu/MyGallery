from app.export import LoginUI,db_connect

db_connect()

app=LoginUI()
app.run_ui()    
