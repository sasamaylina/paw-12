from flask import Flask, render_template, request, redirect, url_for
from models import KategoriRoti, DaftarRoti

app = Flask(__name__)

@app.route('/')
def index():
    kategori = KategoriRoti.get_all()
    roti = DaftarRoti.get_all()
    return render_template('index.html', kategori=kategori, roti=roti)

@app.route('/kategori/insert')
def form_insert_kategori():
    return render_template('insert_kategori.html')

@app.route('/kategori/insert', methods=['POST'])
def insert_kategori():
    nama = request.form.get("nama_kategori")
    deskripsi = request.form.get("deskripsi")
    KategoriRoti.create(nama, deskripsi)
    return redirect(url_for('index'))

@app.route('/kategori/update/<int:id_kategori>')
def form_update_kategori(id_kategori):
    data = KategoriRoti.get_by_id(id_kategori)
    return render_template('update_kategori.html', data=data)

@app.route('/kategori/update/<int:id_kategori>', methods=['POST'])
def update_kategori(id_kategori):
    nama = request.form.get("nama_kategori")
    deskripsi = request.form.get("deskripsi")
    KategoriRoti.update(id_kategori, nama, deskripsi)
    return redirect(url_for('index'))

@app.route('/kategori/delete/<int:id_kategori>')
def delete_kategori(id_kategori):
    KategoriRoti.delete(id_kategori)
    return redirect(url_for('index'))

@app.route('/roti/insert')
def form_insert_roti():
    kategori = KategoriRoti.get_all()
    return render_template('insert_daftar.html', kategori=kategori)

@app.route('/roti/insert', methods=['POST'])
def insert_roti():
    nama = request.form.get("nama_roti")
    id_kat = request.form.get("id_kategori")
    deskripsi = request.form.get("deskripsi")
    harga = request.form.get("harga")
    stok = request.form.get("stok")
    DaftarRoti.create(nama, id_kat, deskripsi, harga, stok)
    return redirect(url_for('index'))

@app.route('/roti/update/<int:id_roti>')
def form_update_roti(id_roti):
    data = DaftarRoti.get_by_id(id_roti)
    kategori = KategoriRoti.get_all()
    return render_template('update_daftar.html', data=data, kategori=kategori)

@app.route('/roti/update/<int:id_roti>', methods=['POST'])
def update_roti(id_roti):
    nama = request.form.get("nama_roti")
    id_kat = request.form.get("id_kategori")
    deskripsi = request.form.get("deskripsi")
    harga = request.form.get("harga")
    stok = request.form.get("stok")
    DaftarRoti.update(id_roti, nama, id_kat, deskripsi, harga, stok)
    return redirect(url_for('index'))

@app.route('/roti/delete/<int:id_roti>')
def delete_roti(id_roti):
    DaftarRoti.delete(id_roti)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
