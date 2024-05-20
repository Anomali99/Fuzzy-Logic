from flask import Flask, render_template_string, request
from traffic_light import get

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        kepadatan = float(request.form['kepadatan'])
        waktu = float(request.form['waktu'])
        hasil = get(kepadatan, waktu)
        context = {
            "kepadatan": kepadatan,
            "waktu": waktu,
            "hasil": hasil,
        }
        return render_template_string("""
            <body style="display:flex; width: 100vw; justify-content: center; align-items: center; margin-top: 2rem;">
                <div>
                    <h1 style="width: 100%; justify-content: center;">Traffic Light Berbasis Logika Fuzzy </h1>
                    <form style="margin-top: 2rem;"  method="post">
                        <label for="kepadatan">Kepadatan</label>
                        <input type="number" placeholder="kepadatan" id="kepadatan" name="kepadatan" value="{{ context.kepadatan }}"/>
                        <label for="waktu">Waktu</label>
                        <input type="number" placeholder="waktu" id="waktu" name="waktu" value="{{ context.waktu }}"/>
                        <button type="submit">Hitung</button>
                    </form>
                    <h4 style="width: 100%; justify-content: center;">Durasi Lampu = {{ context.hasil }}</h4>
                    <h3 style="width: 100%; justify-content: center; margin-top: 2rem;">Fungsi Keanggotaan Input Kepadatan</h3>
                    <img src="{{ url_for('static', filename='kepadatan_hasil.png') }}" alt="kepadatan"/>
                    <h3 style="width: 100%; justify-content: center; margin-top: 2rem;">Fungsi Keanggotaan Input Waktu</h3>
                    <img src="{{ url_for('static', filename='waktu_hasil.png') }}" alt="waktu"/>
                    <h3 style="width: 100%; justify-content: center; margin-top: 2rem;">Fungsi Keanggotaan Output Durasi</h3>
                    <img src="{{ url_for('static', filename='durasi_hasil.png') }}" alt="durasi"/>
                </div>
            </body>
            """, context=context)

    return render_template_string("""
        <body style="display:flex; width: 100vw; justify-content: center; align-items: center; margin-top: 2rem;">
            <div>
                <h1 style="width: 100%; justify-content: center;">Traffic Light Berbasis Logika Fuzzy </h1>
                <form style="margin-top: 2rem;"  method="post">
                    <label for="kepadatan">Kepadatan</label>
                    <input type="number" placeholder="kepadatan" id="kepadatan" name="kepadatan" />
                    <label for="waktu">Waktu</label>
                    <input type="number" placeholder="waktu" id="waktu" name="waktu" />
                    <button type="submit">Hitung</button>
                </form>
                <h3 style="width: 100%; justify-content: center; margin-top: 2rem;">Fungsi Keanggotaan Input Kepadatan</h3>
                <img src="{{ url_for('static', filename='kepadatan.png') }}" alt="kepadatan"/>
                <h3 style="width: 100%; justify-content: center; margin-top: 2rem;">Fungsi Keanggotaan Input Waktu</h3>
                <img src="{{ url_for('static', filename='waktu.png') }}" alt="waktu"/>
                <h3 style="width: 100%; justify-content: center; margin-top: 2rem;">Fungsi Keanggotaan Output Durasi</h3>
                <img src="{{ url_for('static', filename='durasi.png') }}" alt="durasi"/>
            </div>
        </body>
        """)

if __name__ == "__main__":
    app.run(debug=True)
