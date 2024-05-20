from flask import Flask, render_template_string, request
from traffic_light import get

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    context = {
        "kepadatan": 0,
        "waktu": 0,
        "hasil": 0,
        "img_kepadatan": "kepadatan.png",
        "img_waktu": "waktu.png",
        "img_durasi": "durasi.png",
    }
    
    if request.method == 'POST':
        kepadatan = request.form.get('kepadatan', type=float, default=0)
        waktu = request.form.get('waktu', type=float, default=0)
        context["hasil"] = get(kepadatan, waktu)
        context["kepadatan"] = kepadatan
        context["waktu"] = waktu
        context["img_kepadatan"] = "kepadatan_hasil.png"
        context["img_waktu"] = "waktu_hasil.png"
        context["img_durasi"] = "durasi_hasil.png"

    return render_template_string("""
        <body style="display:flex; width: 100vw; justify-content: center; align-items: center; margin-top: 2rem;">
            <div>
                <h1 style="text-align: center;">Traffic Light Berbasis Logika Fuzzy</h1>
                <form style="margin-top: 2rem;" method="post">
                    <label for="kepadatan">Kepadatan</label>
                    <input type="number" step="any" placeholder="kepadatan" id="kepadatan" name="kepadatan" value="{{ context.kepadatan }}"/>
                    <label for="waktu">Waktu</label>
                    <input type="number" step="any" placeholder="waktu" id="waktu" name="waktu" value="{{ context.waktu }}"/>
                    <button type="submit">Hitung</button>
                </form>
                {% if context.hasil != 0 %}
                <h4>Durasi Lampu = {{ context.hasil }}</h4>
                {% endif %}
                <h3 style="text-align: center; margin-top: 2rem;">Fungsi Keanggotaan Input Kepadatan</h3>
                <img src="{{ url_for('static', filename=context.img_kepadatan) }}" alt="kepadatan"/>
                <h3 style="text-align: center; margin-top: 2rem;">Fungsi Keanggotaan Input Waktu</h3>
                <img src="{{ url_for('static', filename=context.img_waktu) }}" alt="waktu"/>
                <h3 style="text-align: center; margin-top: 2rem;">Fungsi Keanggotaan Output Durasi</h3>
                <img src="{{ url_for('static', filename=context.img_durasi) }}" alt="durasi"/>
            </div>
        </body>
        """, context=context)

if __name__ == "__main__":
    app.run(debug=True)
