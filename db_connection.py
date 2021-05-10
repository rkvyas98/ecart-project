import mysql.connector as mc

db = mc.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "ecart"
)