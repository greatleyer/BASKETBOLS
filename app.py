from models import SpeletajaStatistika

def iegut_statistikas_datus():
    dati = SpeletajaStatistika.select()
    return dati