from optparse import Option, OptionParser, make_option, OptionConflictError

class OptionGroup(object):
    def __init__(self, header, helpstr, *args):
        self.header = header
        self.helpstr = helpstr
        self.options = args

    def get_option_group(self, parser):
        group = optparse.OptionGroup(parser, self.header, self.helpstr)
        group.add_options(self.options)
        return group
