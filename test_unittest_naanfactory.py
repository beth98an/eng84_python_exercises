from naan_factory import NaanFactory


import unittest


class RunFactory(unittest.TestCase):

    fact = NaanFactory()

    def test_make(self):
        self.assertEqual(self.fact.make("water", "flour"), "dough")

    def test_bake(self):
        self.assertEqual(self.fact.bake("dough"), "naan")

    def test_run_fact(self):
        self.assertEqual(self.fact.run_fact("water", "flour"), "naan")
