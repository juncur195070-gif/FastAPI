from fastapi import FastAPI
from datetime import datetime
import zoneinfo

app = FastAPI()

@app.get('/')
async def root():
    return {
        "message": "Hello World"
    }

country_timezones = {
    'CO': 'America/Bogota',
    'MX': 'America/Mexico_City',
    'AR': 'America/Argentina/Buenos_Aires',
    'BR': 'America/Sao_Paulo',
    'PE': 'America/Lima'
}

@app.get('/time/{iso_code}')
def time(iso_code: str):
    iso = iso_code.upper()
    timezone_str = country_timezones.get(iso)
    tz = zoneinfo.ZoneInfo(timezone_str)
    return {
        "time": datetime.now(tz)
    }

@app.get('/health')
def health():
    return {
        "status": "Ok"
    }

@app.get('/message')
def message():
    return {
        "message": "Hello World"
    }
@app.get('/new')
def newversion():
    return {
        "message": "esto es de la version nueva creada"
    }