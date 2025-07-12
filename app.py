from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

yorumlar = []

ustalar = [
    {
        "id": 1,
        "isim": "Mehmet Emin Yağbasan",
        "meslek": "Marangoz",
        "aciklama": "20 yıllık tecrübesiyle her türlü mobilya ve ahşap tamir işleri yapmaktadır.",
        "resim": "images/mehmet_emin_yagbasan.jpeg"

    }
]

@app.route('/')
def index():
    return render_template('index.html', ustalar=ustalar)

@app.route('/usta/<int:usta_id>', methods=['GET', 'POST'])
def usta(usta_id):
    usta = next((u for u in ustalar if u["id"] == usta_id), None)
    if usta is None:
        return "Usta bulunamadı", 404

    # Bu ustaya özel yorumlar
    usta_yorumlar = [y for y in yorumlar if y["usta_id"] == usta_id]

    if request.method == 'POST':
        ad = request.form['ad']
        puan = int(request.form['puan'])
        yorum = request.form['yorum']
        yorumlar.append({
            "usta_id": usta_id,
            "ad": ad,
            "puan": puan,
            "yorum": yorum
        })
        return redirect(url_for('usta', usta_id=usta_id))

    return render_template('usta.html', usta=usta, yorumlar=usta_yorumlar)

@app.route('/iletisim')
def iletisim():
    return render_template('iletisim.html')

if __name__ == '__main__':
    app.run(debug=True)

