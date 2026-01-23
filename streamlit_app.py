import streamlit as st
import requests
import qrcode
from io import BytesIO

st.set_page_config(page_title="MFA Sigurni Login", page_icon="🔐")
st.title("Sustav s Dvostrukom Autentifikacijom (MFA)")

API_URL = "http://127.0.0.1:8000"

menu = ["Prijava", "Registracija"]
choice = st.sidebar.selectbox("Izbornik", menu)

if choice == "Registracija":
    st.subheader("Kreiraj novi račun")
    new_user = st.text_input("Korisničko ime")
    new_pass = st.text_input("Lozinka", type='password')

    if st.button("Registriraj me"):
        response = requests.post(f"{API_URL}/register?username={new_user}&password={new_pass}")
        
        if response.status_code == 200:
            data = response.json()
            st.success("Račun je uspješno kreiran!")
            st.write("### Vaš MFA Tajni Ključ:")
            st.code(data['mfa_secret'])
            
            otp_uri = f"otpauth://totp/MojProjekt:{new_user}?secret={data['mfa_secret']}&issuer=MojProjekt"
            img = qrcode.make(otp_uri)
            
            buf = BytesIO()
            img.save(buf, format="PNG")
            st.image(buf.getvalue(), caption="Skenirajte ovaj kod aplikacijom Google Authenticator")
        else:
            st.error("Greška pri registraciji (Korisnik možda već postoji).")

elif choice == "Prijava":
    st.subheader("Prijava u sustav")
    user = st.text_input("Korisničko ime")
    password = st.text_input("Lozinka", type='password')
    otp = st.text_input("6-znamenkasti OTP kod s mobitela", help="Unesite kod iz svoje Authenticator aplikacije")

    if st.button("Prijavi se"):
        response = requests.post(f"{API_URL}/login?username={user}&password={password}&otp_code={otp}")
        
        if response.status_code == 200:
            st.balloons() # Mala animacija za uspjeh
            st.success(f"Dobrodošli natrag, {user}! Pristup je odobren.")
        else:

            st.error("Neuspješna prijava. Provjerite podatke ili OTP kod.")
