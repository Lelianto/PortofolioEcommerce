import json
from . import app, client, cache, create_token, db_reset

class TestBook():
    # Test Case Create Token 
    db_reset()
    def test_post_new_book(self, client):
        token = create_token(False)

        data = {
            "judul":"Belajar Apapun Selain Hidup",
            "penulis": "Penguasa",
            "jumlah_halaman": "257",
            "tanggal_terbit":"01/2017",
            "isbn": "182319191123418481238418",
            "genre": "Romantis",
            "bahasa":"Indonesia",
            "berat":0.245,
            "lebar": 15,
            "panjang": 24,
            "penerbit":"gramedia",
            "jenis_cover":"Soft Cover",
            "status": "Ready Stock",
            "foto_buku": "Image.jpg",
            "sinopsis":"Melakukan bebas dengan terbatas",
            "harga":50000,
            "stok": 30
        }

        res = client.post('/book', json = data, headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)

        assert res.status_code == 200

    def test_post_new_book1(self, client):
        token = create_token(False)

        data = {
            "judul":"Bahasa Matematika",
            "penulis": "Penguasa",
            "jumlah_halaman": "257",
            "tanggal_terbit":"01/2017",
            "isbn": "18231234234234239123818",
            "genre": "Romantis",
            "bahasa":"Indonesia",
            "berat":0.245,
            "lebar": 15,
            "panjang": 24,
            "penerbit":"gramedia",
            "jenis_cover":"Soft Cover",
            "status": "Ready Stock",
            "foto_buku": "Image.jpg",
            "sinopsis":"Melakukan bebas dengan terbatas",
            "harga":50000,
            "stok": 30
        }

        res = client.post('/book', json = data, headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)

        assert res.status_code == 200

    def test_put_book(self, client):
        token = create_token(False)
        data = {
            'judul':"Selamanya Berubah",
            "penulis": "Penguasa",
            "jumlah_halaman": "257",
            "tanggal_terbit":"01/2017",
            "isbn": "182319435247619123818",
            "genre": "Romantis",
            "bahasa":"Indonesia",
            "berat":0.245,
            "lebar": 15,
            "panjang": 25,
            "penerbit":"gramedia",
            "jenis_cover":"Soft Cover",
            "status": "Ready Stock",
            "foto_buku": "Image.jpg",
            "sinopsis":"Melakukan bebas dengan terbatas",
            "harga":55000,
            "stok": 30
        }

        res = client.put('/book/edit/1', json = data, headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)

        assert res.status_code == 200
    
    def test_get_by_id_book(self, client):
        token = create_token(False)

        data = {
        }

        res = client.get('/book/edit/1', json = data, headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)

        assert res.status_code == 200
    
    def test_get_all_book(self, client):
        token = create_token(False)

        data = {
        }

        res = client.get('/book', json = data, headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)

        assert res.status_code == 200
    
    def test_get_all_book_mine(self, client):
        token = create_token(False)

        data = {
        }

        res = client.get('/book/mine', json = data, headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)

        assert res.status_code == 200
    
    def test_get_search(self, client):
        token = create_token(False)

        data = {
            "keyword":"selamanya"
        }

        res = client.get('/book/search', json = data, headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)

        assert res.status_code == 200
    
    def test_get_search_category(self, client):
        token = create_token(False)

        data = {
            "keyword":"Romantis"
        }

        res = client.get('/book/category', json = data, headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)

        assert res.status_code == 200

    def test_post_new_book2(self, client):
        token = create_token(False)

        data = {
            "judul":"Belajar Apapun Selain Hidup",
            "penulis": "Penguasa",
            "jumlah_halaman": 257,
            "tanggal_terbit":"01/2017",
            "isbn": "18231384180959844877575",
            "genre": "Romantis",
            "bahasa":"Indonesia",
            "berat":0.245,
            "lebar": 15,
            "panjang": 24,
            "penerbit":"gramedia",
            "jenis_cover":"Soft Cover",
            "status": "Ready Stock",
            "foto_buku": "Image.jpg",
            "sinopsis":"Melakukan bebas dengan terbatas",
            "harga":50000,
            "stok": 30
        }

        res = client.post('/book', json = data, headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)

        assert res.status_code == 200

    def test_delete_by_id_book_internal(self, client):
        token = create_token(True)

        res = client.delete('/book/edit/1', headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)

        assert res.status_code == 200
    
    def test_delete_by_id_book_user(self, client):
        token = create_token(False)

        res = client.delete('/book/edit/3', headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)

        assert res.status_code == 200