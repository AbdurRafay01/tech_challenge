from werkzeug.security import safe_str_cmp
from user import User

users = [
    User(1, 'user1', 'leef2'),
    User(2, 'user2', 'jam3'),
]


username_table = {u.username: u for u in users}
# 
userid_table = {u.id: u for u in users}

def authenticate(username, password):
    #None is the default value i.e if there is no username like the given.
    user = username_table.get(username, None)
    if user and safe_str_cmp(user.password, password):
        return user 

#Identity function takes in the payload (payload is the contents of the jwt token)
def identity(payload):
    #extract the user id from that payload
    userid = payload['identity']
    #retrieve the user which matches this userid
    return userid_table.get(userid, None)