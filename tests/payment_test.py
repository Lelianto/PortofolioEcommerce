import json
from . import app, client, cache, create_token, db_reset

class TestPayment():
    # Test Case Create Token 
    db_reset()
    def test_post_new_payment(self, client):
        token = create_token(False)

        data = {
            "kota_kabupaten":"Malang"
        }

        res = client.post('/payment/ongkir', json = data, headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)

        assert res.status_code == 200
