import unittest
from fakerData import myFaker
from faker import Faker
import copy


class testFaker(unittest.TestCase):
    def setUp(self):
        self.mf = myFaker()
        return super().setUp()
        print()

    @unittest.skip('')
    def test_demo(self):
        ret = self.fake.syncGetparameter("a=213&b=456", None)
        self.assertEqual(True, True)

    def test_guess_type(self):
        gt = [
            ["int", '1'],
            ["float", "1.4"],
            ["dict", '{"guess":213}'],
            ["list", "['12',123]"],
            ["bool", 'true'],
            ["str", ''],
            ["str", 'google'],
            ["None", "null"],
            ["str", '2+3'],
            ["str", '[1]+[2]']
        ]
        for case in gt:
            obj_type = self.mf.guess_type(case[1])
            if case[0] not in obj_type:
                print('error case is {} return obj_type is {}'.format(case, obj_type))

    def test_is_list(self):
        cases = [
            ['[1,2,3,4,[1,2,[1,2]]]', True],
            ['[1,2,3,4,[1,2,[1,]]]', False],
            ['[1]+[2]', False]
        ]
        for case in cases:
            self.assertEqual(myFaker.isList(
                case[0]), case[1], 'error case is %s' % case[0])

    def test_generatorUrlParameter(self):
        datas = [
            "?a=123&b=error",
            "a=12&b=12.012&c=tea",
            "https://www.google.com/search?q=linux+%E6%9F%A5%E7%9C%8B%E8%BF%9B%E7%A8%8B&oq=linux+%E6%9F%A5%E7%9C%8B%E8%BF%9B%E7%A8%8B&aqs=chrome..69i57j0i12l3j0i12i395l4.12150j1j7&sourceid=chrome&ie=UTF-8"
        ]

    def test_generatorBodyParameter(self):
        print("-"*30)
        datas = [
            {"int": 1, "float": 1.2, "bool": True, "list": [], "dict":{}},
            {"int": 1, "float": 1.2, "bool": True,
                "list": [], "dict":{"errcode": 0, "list": []}},
            {'errormsg': "fake data", "result": {
                "total": {"show_num": ["213++", 3], "hide_num":0}}}
        ]


def init_suite():
    suite = unittest.TestSuite()
    suite.addTest(testFaker('test_generatorUrlParameter'))
    suite.addTest(testFaker('test_generatorBodyParameter'))
    return suite


if __name__ == "__main__":
    suite = init_suite()
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
