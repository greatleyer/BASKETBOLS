from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

@app.route('/')
def index():
    
    df = pd.read_json('data.json')

    months_lv_order = [
        'Janvāris', 'Februāris', 'Marts', 'Aprīlis', 'Maijs', 'Jūnijs',
        'Jūlijs', 'Augusts', 'Septembris', 'Oktobris', 'Novembris', 'Decembris'
    ]
    df['menesis'] = pd.Categorical(df['menesis'], categories=months_lv_order, ordered=True)

    df['speletajs'] = df['vards'] + ' ' + df['uzvards']

    df_avg = df.groupby(['speletajs', 'menesis'])['punkti'].mean().reset_index()

    plt.figure(figsize=(14, 7))

    for speletajs in df_avg['speletajs'].unique():
        dati = df_avg[df_avg['speletajs'] == speletajs].copy()
        dati['delta'] = dati['punkti'].diff().fillna(0)

        izmainas = []
        for x in dati['delta']:
            if x > 0:
                izmainas.append("(+" + str(round(x, 1)) + ")")
            elif x < 0:
                izmainas.append("(" + str(round(x, 1)) + ")")
            else:
                izmainas.append("")

        plt.plot(dati['menesis'], dati['punkti'], marker='o', label=speletajs)

        for i in range(len(dati)):
            teksts = str(round(dati['punkti'].iloc[i], 1)) + " " + izmainas[i]
            plt.text(dati['menesis'].iloc[i], dati['punkti'].iloc[i] + 0.45, teksts, ha='center', fontsize=8)

    plt.title('Vidējie punkti un izmaiņas katram spēlētājam pa mēnešiem (24./25.sez.)')
    plt.xlabel('Mēnesis')
    plt.ylabel('Vidējie punkti')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend(title='Spēlētāji', loc='upper left')
    plt.tight_layout()

    
    grafiks_path = os.path.join('static', 'grafiks.png')
    plt.savefig(grafiks_path)
    plt.close()

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
