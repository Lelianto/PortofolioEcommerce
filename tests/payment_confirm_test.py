import json
from . import app, client, cache, create_token, db_reset

class TestPaymentConfirm():
    # Test Case Create Token 
    db_reset()
    def test_post_payment(self, client):
        token = create_token(False)

        data = {
            "kota_kabupaten":"Malang"
        }

        res = client.post('/payment/ongkir', json = data, headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)

        assert res.status_code == 500
    def test_post_payment_confirm(self, client):
        token = create_token(False)

        data = {
        }

        res = client.post('/payment_confirm/bill', json = data, headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)

        assert res.status_code == 500

    def test_get_all_payment_confirm(self, client):
        token = create_token(False)

        data = {
        }

        res = client.get('/payment_confirm/all', json = data, headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)

        assert res.status_code == 200
