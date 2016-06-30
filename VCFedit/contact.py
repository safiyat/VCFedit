class N():
    def __init__(self):
        self.family_name = None
        self.given_name = None
        self.additional_names = None
        self.honorific_prefixes = None
        self.honorific_suffixes = None

    def get_name(self, with_prefix=False):
        n = ";".join([self.family_name, self.given_name,
                       ",".join(self.additional_names),
                       ",".join(self.honorific_prefixes),
                       ",".join(self.honorific_suffixes)])
        if with_prefix:
            return "N:%s" % n
        return n

    def formatted_name(self, with_prefix=False):
        honorific_prefixes += " ".join(self.honorific_prefixes)
        given_name = self.given_name
        family_name = self.family_name
        if self.honorific_suffixes:
            honorific_suffixes = ", ".join(self.honorific_suffixes)

        fn = " ".join([honorific_prefixes, given_name, family_name])
        if self.honorific_suffixes:
            fn = "%s %s" % (fn, honorific_suffixes)

        if with_prefix:
            return "FN:%s" % fn
        return fn


class Contact():
    def __init__(self):
        self.n = N()
        self.fn = n.formatted_name()  # Full Name
