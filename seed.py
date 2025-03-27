from models import db, SpeletajaStatistika

db.connect()
db.create_tables([SpeletajaStatistika])

if not SpeletajaStatistika.select().exists():
    dati = [
        {"vards": "Vladislavs", "uzvards": "Pozdnaks", "minutes": 28.5, "augstums_cm": 190, "svars_kg": 85, "vertikalais_leciens_cm": 72},
        {"vards": "Maksims", "uzvards": "Konotops", "minutes": 31.2, "augstums_cm": 178, "svars_kg": 70, "vertikalais_leciens_cm": 65},
        {"vards": "Glebs", "uzvards": "Cvetkovs", "minutes": 25.0, "augstums_cm": 195, "svars_kg": 90, "vertikalais_leciens_cm": 80},
        {"vards": "Maksims", "uzvards": "Rubins", "minutes": 29.7, "augstums_cm": 172, "svars_kg": 68, "vertikalais_leciens_cm": 60},
        {"vards": "Nils", "uzvards": "Ivanovs", "minutes": 32.0, "augstums_cm": 200, "svars_kg": 95, "vertikalais_leciens_cm": 85}
    ]

    dati_sakartoti = sorted(dati, key=lambda x: x["augstums_cm"], reverse=True)

    for ieraksts in dati_sakartoti:
        SpeletajaStatistika.create(**ieraksts)

print("Dati saglabāti datubāzē sakārtoti no augstākā līdz zemākajam augstumam.")
