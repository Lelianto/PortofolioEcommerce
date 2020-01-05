import json
from . import app, client, cache, create_token, db_reset

class TestUser():
    # Test Case Create Token 
    def test_post_new_user(self, client):
        db_reset()

        data = {
            "nama_lengkap":"Garry Ariel",
            "email": "garry@alterra.id",
            "kata_sandi": "123454321",
            "tanggal_lahir":"01/01/1992",
            "nomor_telepon": "0812345734534",
            "foto_profil": "1234.jpg",
            "genre":"Komedi"
        }

        res = client.post('/user', json = data)
        res_json = json.loads(res.data)

        assert res.status_code == 200

    def test_get_token_valid_user(self, client):
        data = {
            "email": "garry@alterra.id",
            "kata_sandi": "123454321"
        }

        res = client.get('/token', json = data)
        res_json = json.loads(res.data)

        assert res.status_code == 200

    def test_get_token_valid_internal(self, client):
        data = {
            "email": "lian@alterra.id",
            "kata_sandi": "l3l11234"
        }

        res = client.get('/token', json = data)
        res_json = json.loads(res.data)

        assert res.status_code == 200

    def test_get_all_user_internal(self, client):
        token = create_token(True)

        data = {

        }

        res = client.get('/user', json = data, headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)

        assert res.status_code == 200
    
    def test_get_user_byID_internal(self, client):
        token = create_token(True)

        data = {
        }

        res = client.get('/user/1', json = data, headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)

        assert res.status_code == 200
    
    def test_get_user_byID_noninternal(self, client):
        token = create_token(False)

        data = {
        }

        res = client.get('/user/2', json = data, headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)

        assert res.status_code == 200

    def test_get_user_byID_noninternal_false(self, client):
        token = create_token(False)

        data = {
        }

        res = client.get('/user/3', json = data, headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)

        assert res.status_code == 404
    
    def test_put_user(self, client):
        token = create_token(False)

        data = {
            "tanggal_lahir":"01/01/1992",
            "nomor_telepon": "0812345734534",
            "foto_profil": "1234.jpg",
            "genre":"Komedi"
        }

        res = client.put('/user/2', json = data, headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)

        assert res.status_code == 200
    
    def test_delete_user_myself_false(self, client):
        token = create_token(False)

        data = {
        }

        res = client.delete('/user/3', json = data, headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)

        assert res.status_code == 404

    def test_delete_user_myself(self, client):
        token = create_token(False)

        data = {
        }

        res = client.delete('/user/2', json = data, headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)

        assert res.status_code == 200
    
    def test_delete_user_myself1(self, client):
        token = create_token(False)

        data = {
        }

        res = client.delete('/user/2', json = data, headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)

        assert res.status_code == 404
    
    def test_post_new_user1(self, client):
        db_reset()

        data = {
            "nama_lengkap":"Garry Ariel",
            "email": "garry@alterra.id",
            "kata_sandi": "123454321",
            "tanggal_lahir":"01/01/1992",
            "nomor_telepon": "0812345734534",
            "foto_profil": "1234.jpg",
            "genre":"Komedi"
        }

        res = client.post('/user', json = data)
        res_json = json.loads(res.data)

        assert res.status_code == 200

    def test_delete_user_byinternal(self, client):
        token = create_token(True)

        data = {
        }

        res = client.delete('/user/3', json = data, headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)

        assert res.status_code == 200

        

