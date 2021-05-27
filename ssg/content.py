import re
from yaml import load, FullLoader
from collections.abc import Mapping

class Content(Mapping):
    __delimeter = "^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimeter, re.MULTILINE)

    def load(self, cls, string):
        _, fm, content = self.__regex__regex.split(string, depth=2)

    load(, Loader=FullLoader)