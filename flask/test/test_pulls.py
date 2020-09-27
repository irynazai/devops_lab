import os
from unittest import TestCase
from handlers import pulls as p
from test import variables as v
from handlers.pulls import path


class TestPulls(TestCase):

    def setUp(self):
        """Init"""
        self.dir = os.path.dirname(path)

    def test_get_pulls(self):
        """Test for _get_pulls"""
        for i in ("open", "closed", "accepted", "needs work", None):
            res = p.get_pulls(i)
            assert res is not None

    def test_check_exist_folder(self):
        """Test for _get_json_response"""
        self.assertTrue(p.check_exist_folder("/tmp/json_path"), True)

    def test_load_from_json_to_list(self):
        """Test for _load_from_json_to_list"""
        self.assertTrue(type(p.load_from_json_to_list()), list)
        self.assertTrue(p.load_from_json_to_list(), v.template_all)

    def test_get_json_response(self):
        """Test for _check_exist_folder"""
        self.assertTrue(p.get_json_response(v.response, None), v.template_all)
        self.assertTrue(p.get_json_response(v.response_open, 'open'), v.template_open)
        self.assertTrue(p.get_json_response(v.response_closed, 'closed'), v.template_closed)
        self.assertTrue(p.get_json_response(v.response, 'accepted'), v.template_accepted)
        self.assertTrue(p.get_json_response(v.response, 'needs work'), v.template_need_work)

    def tearDown(self):
        """Finish"""
