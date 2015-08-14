# /usr/bin/env python


__author__ = 'stephen'


from optparse import OptionParser

parser = OptionParser()

parser.add_option('-o', '--output', dest='log_file_path', help='Path of log file.',)

(options, args) = parser.parse_args()
print (options, args)
print options
print dir(options)
# use getattri here
print options.log_file_path

