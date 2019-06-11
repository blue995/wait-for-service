#!/usr/bin/env python3

import sys

from argparse import ArgumentParser
from enum import Enum
from subprocess import call


def version():
    return 'Version: {0}'.format(1.0)


def check_retcode_for_error(parser: ArgumentParser, retcode: int):
    if retcode != 0:
        parser.print_help()
        exit(retcode)

class WaitingType(Enum):
    BASIC = 'basic'
    CONSUL = 'consul'
    
    def __str__(self):
        return self.value


def main():
    parser = ArgumentParser(prog='wait-for-service', description='Wait for a service.', allow_abbrev=False)
    parser.add_argument('--host', type=str, required=True, help='Specify the service host.')
    parser.add_argument('--port', '-p', type=int, required=True, help='Specify the service port.')
    parser.add_argument('--service', '-s', type=str, help='Specify the name of the service. (Mandatory for waiting type {0})'.format(WaitingType.CONSUL))
    parser.add_argument('--type', '-t', type=WaitingType, choices=list(WaitingType), default=WaitingType.BASIC, help='Specify the waiting algorithm. (Default: %(default)s)')
    parser.add_argument('--version', action='version', version=version())
    args = parser.parse_args()

    script_name = "{0}-scripts/wait-for-service".format(str(args.type))
    service = args.service
    needs_service_name = args.type is WaitingType.CONSUL
    has_no_service_name = service is None
    subprocess_args = [script_name, "--host", args.host, "--port", str(args.port)]

    if needs_service_name:
        if has_no_service_name:
            check_retcode_for_error(parser, 1)
        subprocess_args.append('--service')
        subprocess_args.append(service)

    try:
        retcode = call(subprocess_args)
        check_retcode_for_error(parser, retcode)
    except FileNotFoundError:
        print('Could not find script {0}'.format(script_name))
        check_retcode_for_error(parser, 2)
    except TypeError as err:
        print('Some type error occurred when calling the subprocess script: {}'.format(err))
        check_retcode_for_error(parser, 3)
    except:
        print("Unexpected error: ", sys.exc_info()[0])
        check_retcode_for_error(parser, 4)


if __name__ == "__main__":
    main()