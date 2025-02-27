import unittest
from main import app

class TestApp(unittest.TestCase):
  
  def setUp(self):
    self.app = app.test_client()
    self.app.testing = True
    
  def test_read_all(self):
    response = self.app.get('/flores')
    assert response.status_code == 200
    
  def test_read_one(self):
    response = self.app.get('/flores/8a939645-7c3f-42b5-9c44-d9fe31583494')
    assert response.status_code == 200

  def test_create_one(self):
    response = self.app.post('/flores', json={'nome': 'Lirio-do-Vale', 'cor': 'Branco', 'preco': 19.9, 'data': '09/09/1900', 'especie': 'Convallaria majalis'})
    assert response.status_code == 201

  def test_update_one(self):
    response = self.app.put('/flores/8a939645-7c3f-42b5-9c44-d9fe31583494', json={'nome': 'Girassol', 'cor': 'Amarelo', 'preco': 16.9, 'data': '10/03/2024', 'especie': 'Helianthus annuus L.'})
    assert response.status_code == 201

  def test_delete_one(self):
    response = self.app.delete('/flores/2162383b-b6ea-4509-bf11-f3912bd7569a')
    assert response.status_code == 200

if __name__ == '__main__':
  unittest.main()