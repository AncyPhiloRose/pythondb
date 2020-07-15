import logging
import sqlite3
# Database Connectivity
logging.info("Connecting to database")
dbmodel =sqlite3.connect(db=dept_manager)
logging.basicConfig (filename="mylog.log",
                     filemode='a',
                     format='%(asctime)s - %(message)s',
                     level=logging.INFO)
logging.info("Database connected")
logging.info("This is an info message")