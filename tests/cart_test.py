import json
from . import app, client, cache, create_token, db_reset

class TestCart():
    # Test Case Create Token 
    # db_reset()
    def test_post_new_cart(self, client):
        token = create_token(False)

        data = {
            "status_cart": False,
            "book_id": 2,
            "judul": "Apapun",
            "penulis":"Siapapun",
            "jenis_cover": "Soft Cover",
            "foto_buku": "Image.jpg",
            "harga":50000,
            "stok":5,
            "berat": 0.245,
            "nama_lengkap":"Lelianto",
            "email":"lelianto.eko@gmail.com"
        }

        res = client.post('/cart/add', json = data, headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)

        assert res.status_code == 200

    def test_post_new_cart_same(self, client):
        token = create_token(False)

        data = {
            "status_cart": False,
            "book_id": 2,
            "judul": "Apapun",
            "penulis":"Siapapun",
            "jenis_cover": "Soft Cover",
            "foto_buku": "Image.jpg",
            "harga":50000,
            "stok":5,
            "berat": 0.245,
            "nama_lengkap":"Lelianto",
            "email":"lelianto.eko@gmail.com"
        }

        res = client.post('/cart/add', json = data, headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)

        assert res.status_code == 200

    def test_put_cart(self, client):
        token = create_token(False)

        data = {
            "stok": 7
        }

        res = client.put('/cart/product/1', json = data, headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)

        assert res.status_code == 200
    
    def test_get_all_cart(self, client):
        token = create_token(False)

        res = client.get('/cart/total', headers={'Authorization': 'Bearer ' + token})

        assert res.status_code == 200

