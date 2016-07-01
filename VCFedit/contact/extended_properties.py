class ExtendedProperties():
    def __init__(self, property_name, value=None):
        self.property_name = property_name
        self.value = value

    def get_property_name(self):
        return self.property_name

    def get_value(self):
        return self.value

    def set_property_name(self, property_name):
        self.property_name = property_name

    def set_value(self, value):
        self.value = value

    def property(self):
        p = ":".join([self.property_name.upper(), self.value])
        p = "X-%s" % p
        return p
