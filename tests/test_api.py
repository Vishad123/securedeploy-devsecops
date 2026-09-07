import unittest

from fastapi.testclient import TestClient

from app.main import app


class ApiTests(unittest.TestCase):
    def test_health(self):
        client = TestClient(app)
        response = client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "ok")

    def test_analyze(self):
        client = TestClient(app)
        response = client.post(
            "/analyze",
            json={"event": "failed login from 203.0.113.10"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(response.json()["finding_count"], 1)


if __name__ == "__main__":
    unittest.main()
