# -*- coding: utf-8 -*-

def test_cancelar_nota_20(cert_info):
    from pysped_nfe import ProcessadorNFe
    from pysped_nfe.webservices_flags import *

    p = ProcessadorNFe()
    p.versao = u'2.00'
    p.estado = u'SP'
    p.certificado.arquivo = cert_info.arquivo
    p.certificado.senha = cert_info.senha
    p.salvar_arquivos = True
    p.contingencia_SCAN = False
    p.caminho = u''

    #
    # O retorno de cada webservice é um dicionário
    # estruturado da seguinte maneira:
    # { TIPO_DO_WS_EXECUTADO: {
    #       u'envio'   : InstanciaDaMensagemDeEnvio,
    #       u'resposta': InstanciaDaMensagemDeResposta,
    #       }
    # }
    #
    processo = p.cancelar_nota(chave_nfe=u'35100411111111111111551010000000271123456789',
        numero_protocolo=u'135100018751878',
        justificativa=u'Somente um teste de cancelamento')

    print processo.envio.xml
    print
    print processo.resposta.xml
    print
    assert processo.resposta.reason

