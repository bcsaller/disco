import unittest

from utils import local_stream
from layer_cake.knowledge import Knowledge


class TestKnowledge(unittest.TestCase):
    def test_valid_yaml(self):
        kb = Knowledge()
        kb.load(local_stream("mysql.yaml"))
        kb.load_schema(local_stream("interface-mysql.schema"))
        kb.validate("mysql", "mysql")
