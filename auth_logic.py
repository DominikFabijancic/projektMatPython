import pyotp
import bcrypt

# Funkcija za pretvaranje lozinke u hash (sigurnosno spremanje)
def get_password_hash(password: str):
    # Pretvaramo lozinku u bajtove, generiramo sol i hashiramo
    pwd_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(pwd_bytes, salt)
    return hashed_password.decode('utf-8')

# Funkcija za provjeru lozinke prilikom prijave
def verify_password(plain_password: str, hashed_password: str):
    password_byte_enc = plain_password.encode('utf-8')
    hashed_password_enc = hashed_password.encode('utf-8')
    return bcrypt.checkpw(password_byte_enc, hashed_password_enc)

# MFA Logika (ostaje ista)
def generate_mfa_secret():
    return pyotp.random_base32()

def verify_otp(secret, code):
    totp = pyotp.TOTP(secret)
    return totp.verify(code)