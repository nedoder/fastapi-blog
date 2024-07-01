import bcrypt

def hash(password: str):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

def verify(password, hashed_password):
    return pwd_context.verify(password, hashed_password)