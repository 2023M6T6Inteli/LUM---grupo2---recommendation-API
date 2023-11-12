import unittest
import json
from flask import Flask
from API.arquivo import perform_prediction, app  # Certifique-se de substituir 'seu_arquivo' pelo nome do seu arquivo principal

class TestPredictEndpoint(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_predict_endpoint_status_code(self):
        # Dados de exemplo para o teste
        data = {
            "CIE": "12"
        }

        # Envia uma solicitação POST para o endpoint /prever
        response = self.app.post('/predictSupplier', json=data)

        # Verifica se a resposta tem o código de status 200 (OK)
        self.assertEqual(response.status_code, 200)

    def test_predict_endpoint_missing_key(self):
        # Envia uma solicitação POST para o endpoint /prever sem a chave "CIE" nos dados
        data = {}

        response = self.app.post('/predictSupplier', json=data)

        # Verifica se a resposta tem o código de status 400 (Bad Request)
        self.assertEqual(response.status_code, 400)

        # Analisa o conteúdo da resposta JSON de erro
        error = json.loads(response.get_data(as_text=True))

        # Verifica se a chave "Erro" está presente no resultado de erro
        self.assertIn("Error", error)
        self.assertIn("Key 'CIE' is missing in the data", error["Error"])

    def test_predict_endpoint_invalid_input(self):
        # Envia uma solicitação POST para o endpoint /prever com dados inválidos
        data = {
            "CIE": "ABC"
        }

        response = self.app.post('/predictSupplier', json=data)

        # Verifica se a resposta tem o código de status 200 (OK)
        self.assertEqual(response.status_code, 200)

    def test_predict_endpoint_empty_input(self):
        # Envia uma solicitação POST para o endpoint /prever com dados vazios
        data = {}

        response = self.app.post('/predictSupplier', json=data)

        # Verifica se a resposta tem o código de status 400 (Bad Request)
        self.assertEqual(response.status_code, 400)

        # Analisa o conteúdo da resposta JSON de erro
        error = json.loads(response.get_data(as_text=True))

        # Verifica se a chave "Erro" está presente no resultado de erro
        self.assertIn("Error", error)
        self.assertIn("Key 'CIE' is missing in the data", error["Error"])

if __name__ == '__main__':
    unittest.main()

