from app import app
app.run('0.0.0.0')

from app.connection import connect 
connect()