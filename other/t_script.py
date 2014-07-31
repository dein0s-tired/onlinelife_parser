#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import argparse

__author__ = 'dein0s'

updated = '29.07.2014'

def create_parser():
    parser = argparse.ArgumentParser(
        description='Nothing to add here',
        add_help=True,
    )
    #subparsers = parser.add_subparsers(dest='command')
    # method_parser = subparsers.add_parser('')
    # parser.add_argument('name', nargs='?', default='World')
    parser.add_argument('-m', '--method', required=True, help='Stub')
    parser.add_argument('-r', '--realm', required=True, help='Stub')
    parser.add_argument('-u', '--updated', action='version', help='Script last update date',
                        version='%s last time updated %s' % (sys.argv[0], updated))
    return parser


if __name__ == "__main__":
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])
    if namespace.realm not in ('STUB1', 'STUB2'):
        namespace.realm = 'You SUCK'

    print namespace
    print 'Realm: %s' % namespace.realm
    print 'Method: %s' % namespace.method