class N():
    """
    N
    FN
    """
    def __init__(self, given_name, family_name=None, additional_names=[],
                 honorific_prefixes=[], honorific_prefixes=[]):
        self.family_name = family_name
        self.given_name = given_name
        self.additional_names = additional_names
        self.honorific_prefixes = honorific_prefixes
        self.honorific_suffixes = honorific_suffixes

    def get_family_name(self):
        return self.family_name

    def get_given_name(self):
        return self.given_name

    def get_additional_names(self):
        return self.additional_names

    def get_honorific_prefixes(self):
        return self.honorific_prefixes

    def get_honorific_suffixes(self):
        return self.honorific_suffixes


    def set_family_name(self, family_name):
        self.family_name = family_name

    def set_given_name(self, given_name):
        self.given_name = given_name

    def set_additional_names(self, additional_names):
        self.additional_names = additional_names

    def set_honorific_prefixes(self, honorific_prefixes):
        self.honorific_prefixes = honorific_prefixes

    def set_honorific_suffixes(self, honorific_suffixes):
        self.honorific_suffixes = honorific_suffixes


    def name(self, with_prefix=False):
        """
        Return
            Gump;Forrest;;Mr.
        or
            N:Gump;Forrest;;Mr.
        """
        n = ";".join([self.family_name, self.given_name,
                       ",".join(self.additional_names),
                       ",".join(self.honorific_prefixes),
                       ",".join(self.honorific_suffixes)])
        if with_prefix:
            return "N:%s" % n
        return n

    def formatted_name(self, with_prefix=False):
        """
        Return
            Forrest Gump
        or
            FN:Forrest Gump
        """
        honorific_prefixes += " ".join(self.honorific_prefixes)
        given_name = self.given_name
        family_name = self.family_name

        fn = " ".join([given_name, family_name])

        if self.honorific_prefixes:
            fn = "%s %s" % (honorific_prefixes, fn)

        if self.honorific_suffixes:
            fn = "%s %s" % (fn, honorific_suffixes)

        if with_prefix:
            return "FN:%s" % fn
        return fn
