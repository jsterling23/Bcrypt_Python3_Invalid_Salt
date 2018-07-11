import bcrypt

# work around for storing my hashed passwords in the db. 
# I decode('utf-8') the hashed PW then store it in the db. 
# Because when validating the hashed pw on login it continues 
# to throw a Invalid Salt error.
db_new_passwordhash = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
            
    User.objects.create(
        first_name=postData['first_name'],
        last_name=postData['last_name'],
        email=postData['email'],
        password=db_new_passwordhash.decode('utf-8'), # <<< magic 
    )

# validating the hashed pw
user = User.objects.get(email=postData['email'])

db_password = user.password

if bcrypt.checkpw(postData['password'].encode(), db_password.encode()):
    print('this worked')
else:
    print('it didnt work')

# without decoding, it just keeps giving Invalid Salt. Any suggestions on 
# possible problems would be great.
