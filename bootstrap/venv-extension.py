#coding: utf-8
import os
from os.path import abspath, basename, dirname, join, pardir
import subprocess

##file postactivate
POSTACTIVATE = """
source $VIRTUAL_ENV/contrib/aliases.bash
"""


def adjust_options(options, args):
    BOOTSTRAP_PATH = abspath(dirname(__file__))

    # force a destdir
    while len(args):
        args.pop()

    args.append(join(BOOTSTRAP_PATH, pardir))


def extend_parser(parser):
    # overide default options
    parser.set_defaults(no_site_packages=True,
                        unzip_setuptools=True,
                        use_distribute=True)

def after_install(options, home_dir):
    # Install project requirements
    def run(cmd, *args):
        executable = join(home_dir, 'bin', cmd)
        command = [executable] + list(args)
        subprocess.call(command)

    # Create the default postactivate file
    postactivate = abspath(join(home_dir, 'bin', 'postactivate'))
    with open(postactivate, 'w') as f:
        f.write(POSTACTIVATE)

    requirements = abspath(
        join(home_dir, 'bootstrap', 'requirements.txt')
    )
    run('pip', 'install', '-r', requirements)

    print """
    Para finalizar a configuracao do seu ambiente de desenvolvimento:

        1) Ative seu virtualenv:
    """
    print "\tsource %s" % join(home_dir, 'bin', 'activate')
    print "Se voce usa o virtualenvwrapper:"
    print "\tworkon %s" % basename(home_dir)
    print """
        2) Crie o seu settings de desenvolvimento

        3) manage syncdb

        4) Rode os testes do projeto
            manage test
    """
