from os.path import abspath, dirname, join
from ConfigParser import ConfigParser
from collections import namedtuple

TEST_DIR = abspath(dirname(__file__))

def pytest_funcarg__cert_info(request):
    cp = ConfigParser()
    cp.read(join(TEST_DIR, 'config.ini'))
    cert_info = namedtuple('CertInfo', ['arquivo', 'senha'])
    cert_info.arquivo = abspath(join(TEST_DIR, cp.get('certificado', 'arquivo')))
    cert_info.senha = cp.get('certificado', 'senha')
    return cert_info

