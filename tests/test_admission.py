import unittest
from app.admission import validate_deployment
GOOD={"kind":"Deployment","metadata":{"labels":{"app.kubernetes.io/name":"api","app.kubernetes.io/version":"1.2.3"}},"spec":{"template":{"spec":{"containers":[{"image":"repo/api:1.2.3","resources":{"requests":{"cpu":"100m"}}}]}}}}
class Admission(unittest.TestCase):
 def test_accepts_versioned_resourced_workload(self): self.assertTrue(validate_deployment(GOOD))
 def test_rejects_latest(self):
  bad={**GOOD,"spec":{"template":{"spec":{"containers":[{"image":"repo/api:latest","resources":{"requests":{"cpu":"1"}}}]}}}}
  with self.assertRaises(ValueError): validate_deployment(bad)
 def test_rejects_missing_labels(self):
  with self.assertRaises(ValueError): validate_deployment({"kind":"Deployment","spec":{}})
