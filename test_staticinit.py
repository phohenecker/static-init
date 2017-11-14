#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest

import staticinit


__author__ = "Patrick Hohenecker"
__copyright__ = (
        "Copyright (c) 2017 Patrick Hohenecker\n"
        "\n"
        "Permission is hereby granted, free of charge, to any person obtaining a copy\n"
        "of this software and associated documentation files (the \"Software\"), to deal\n"
        "in the Software without restriction, including without limitation the rights\n"
        "to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n"
        "copies of the Software, and to permit persons to whom the Software is\n"
        "furnished to do so, subject to the following conditions:\n"
        "\n"
        "The above copyright notice and this permission notice shall be included in all\n"
        "copies or substantial portions of the Software.\n"
        "\n"
        "THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n"
        "IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n"
        "FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n"
        "AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n"
        "LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n"
        "OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\n"
        "SOFTWARE."
)
__license__ = "MIT License"
__version__ = "2017.1"
__date__ = "Nov 13, 2017"
__maintainer__ = "Patrick Hohenecker"
__email__ = "mail@paho.at"
__status__ = "Production"


class StaticInitTest(unittest.TestCase):
    
    def test_init(self):
        # CHECK --------------------------------------------------------------------------------------------------------
        # annotating something else than a class causes a TypeError
        
        with self.assertRaises(TypeError):
            @staticinit.init()
            def some_func():
                print("just testing")
        
        # CHECK --------------------------------------------------------------------------------------------------------
        # if the specified constructor function does not exist, then a ValueError is raised
        with self.assertRaises(ValueError):
            @staticinit.init()
            class SomeClass(object):
                pass
        
        # CHECK --------------------------------------------------------------------------------------------------------
        # if the constructor function is not a classmethod, then a ValueError is raised
        
        with self.assertRaises(ValueError):
            @staticinit.init(init_meth="static_init")
            class SomeClass(object):
                def static_init(self):
                    print("just testing")
        
        with self.assertRaises(ValueError):
            @staticinit.init(init_meth="static_init")
            class SomeClass(object):
                @staticmethod
                def static_init():
                    print("just testing")
        
        # CHECK --------------------------------------------------------------------------------------------------------
        # proper application works as expected
        
        @staticinit.init()
        class WorkingClass1(object):
            check = False
            
            @classmethod
            def __static_init__(cls):
                cls.check = True
           
        @staticinit.init(init_meth="static_init")
        class WorkingClass2(object):
            check = False
            
            @classmethod
            def static_init(cls):
                cls.check = True
         
        self.assertTrue(WorkingClass1.check)
        self.assertTrue(WorkingClass2.check)


if __name__ == "__main__":
    unittest.main()
