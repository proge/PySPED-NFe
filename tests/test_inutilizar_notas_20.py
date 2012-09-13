# -*- coding: utf-8 -*-

def test_inutilizar_notas_20(cert_info):
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
    processo = p.inutilizar_nota(cnpj=u'11111111111111',
        serie=u'101',
        numero_inicial=18,
        justificativa=u'Testando a inutilização de NF-e')

    print processo.envio.xml
    print
    print processo.resposta.xml
    print
    print "NOTA UNICA"
    assert processo.resposta.reason

    #
    # Inutilizar uma faixa de numeração
    #
    processo = p.inutilizar_nota(cnpj=u'11111111111111',
        serie=u'101',
        numero_inicial=18,
        numero_final=28,
        justificativa=u'Testando a inutilização de NF-e')

    print processo.envio.xml
    print
    print processo.resposta.xml
    print
    print "FAIXA DE NOTAS"
    assert processo.resposta.reason

