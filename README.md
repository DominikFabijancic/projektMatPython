Projekt: MFA Login Sustav

Ovo je timski projekt za implementaciju dvostruke autentifikacije (MFA) koristeći Python. Napravili smo sustav koji zahtijeva i lozinku i kod s mobitela za ulaz.
Kako ovo pokrenuti (Samo prati korake)

Ako si upravo skinuo projekt s GitHub-a, prati ove upute točno ovim redoslijedom da ti sve proradi od prve.
1. Instalacija Pythona

Provjeri imaš li Python instaliran. Otvori terminal i upiši python --version. Ako ti ne izbaci broj (npr. 3.12 ili 3.14), skini ga s njihove službene stranice.
2. Postavljanje okruženja (Virtual Environment)

Ovo radimo da ne zbrčkamo ostale stvari na kompjuteru. U mapi projekta upiši:
Bash

# Kreiranje venv-a
python -m venv venv

# Aktivacija (Windows)
.\venv\Scripts\activate

Kad vidiš (venv) na početku reda u terminalu, znači da je upaljeno.
3. Instalacija potrebnih stvari

Sve što nam treba nalazi se u requirements.txt datoteci. Instaliraj sve jednom naredbom:
Bash

pip install -r requirements.txt

4. Pokretanje aplikacije

Aplikacija ima dva dijela i oba moraju raditi u isto vrijeme.

    Terminal 1 (Backend):
    Bash

uvicorn main:app --reload

Terminal 2 (Web stranica): Otvorite novi terminal, opet aktivirajte venv (.\venv\Scripts\activate) i upišite:
Bash

    streamlit run streamlit_app.py

Sada će vam se otvoriti browser s našom stranicom. To je to.
