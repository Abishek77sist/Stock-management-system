import os
os.environ.setdefault('IP', '0.0.0.0')
os.environ.setdefault('PORT', '5000')
os.environ.setdefault('MONGO_URI', 'mongodb://localhost:27017'
) # insert connection string from the steps above
os.environ.setdefault('MONGO_DBNAME', 'config') # insert your database name


# Further info on setting email server below
os.environ.setdefault('SECRET_KEY', '04b6f80838f26be29963bf1e5c74cae7083f419b030ff04a72feef767fbdbced')  
os.environ.setdefault('MAIL_SERVER', 'smtp.gmail.com')
os.environ.setdefault('MAIL_PORT', '587')
os.environ.setdefault('MAIL_USERNAME', 'abishek050205@gmail.com')
os.environ.setdefault('MAIL_PASSWORD', 'rzafqrtqfovuvoew')
os.environ.setdefault('USER_EMAIL_SENDER_EMAIL', 'abishek050205@gmail.com')

os.environ.setdefault('DEBUG', 'True') # set to False when deploying to Heroku
