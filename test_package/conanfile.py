# -*- coding: utf-8 -*-

from conans import ConanFile, tools
import os


class TestPackageConan(ConanFile):

    def test(self):
        self.run("%s --version" % os.environ["LD"], run_environment=True)
