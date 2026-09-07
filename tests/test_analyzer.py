import unittest

from app.analyzer import analyze_event


class AnalyzerTests(unittest.TestCase):
    def test_failed_login_is_detected(self):
        findings = analyze_event("failed login from 203.0.113.10")
        self.assertTrue(any(item.category == "AUTH_FAILURE" for item in findings))

    def test_admin_login_is_high_severity(self):
        findings = analyze_event("successful admin login")
        self.assertTrue(any(item.severity == "HIGH" for item in findings))

    def test_unknown_event_is_low_severity(self):
        findings = analyze_event("routine backup completed")
        self.assertEqual(findings[0].severity, "LOW")


if __name__ == "__main__":
    unittest.main()
