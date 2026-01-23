from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, database, auth_logic

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/register")
def register(username: str, password: str, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.username == username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Korisnik već postoji")
    
    secret = auth_logic.generate_mfa_secret()
    hashed_pwd = auth_logic.get_password_hash(password)
    
    new_user = models.User(username=username, hashed_password=hashed_pwd, mfa_secret=secret)
    db.add(new_user)
    db.commit()
    
    return {
        "msg": "Korisnik kreiran",
        "mfa_secret": secret,
        "upute": "Unesite ovaj secret u Google Authenticator ili skenirajte QR kod (u idućoj fazi)"
    }

@app.post("/login")
def login(username: str, password: str, otp_code: str, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user or not auth_logic.verify_password(password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Pogrešno ime ili lozinka")
    
    if not auth_logic.verify_otp(user.mfa_secret, otp_code):
        raise HTTPException(status_code=401, detail="Pogrešan OTP kod")
    

    return {"msg": "Uspješna prijava! Dobrodošli."}
