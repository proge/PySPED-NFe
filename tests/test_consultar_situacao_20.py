# -*- coding: utf-8 -*-

def test_consultar_situacao_20(cert_info):
    from pysped_nfe import ProcessadorNFe

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
    processo = p.consultar_servico()

    print processo.envio.xml
    print
    print processo.resposta.xml
    print
    assert processo.resposta.reason != 'Forbidden'

