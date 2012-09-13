# -*- coding: utf-8 -*-

from datetime import datetime

def test_gerar_enviar_nota_20(cert_info):
    from pysped_nfe import ProcessadorNFe
    from pysped_nfe.manual_401 import *
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
    # Instancia uma NF-e
    #
    n = NFe_200()

    #
    # Identificação da NF-e
    #
    n.infNFe.ide.cUF.valor     = UF_CODIGO[u'SP']
    n.infNFe.ide.natOp.valor   = u'Venda de produto do estabelecimento'
    n.infNFe.ide.indPag.valor  = 2
    n.infNFe.ide.serie.valor   = 101
    n.infNFe.ide.nNF.valor     = 37
    n.infNFe.ide.dEmi.valor    = datetime(2011, 5, 25)
    n.infNFe.ide.dSaiEnt.valor = datetime(2011, 5, 25)
    n.infNFe.ide.cMunFG.valor  = 3513801
    n.infNFe.ide.tpImp.valor   = 1
    n.infNFe.ide.tpEmis.valor  = 1
    n.infNFe.ide.indPag.valor  = 1
    n.infNFe.ide.finNFe.valor  = 1
    n.infNFe.ide.procEmi.valor = 0
    n.infNFe.ide.verProc.valor = u'TaugaRS Haveno 1.0'

    #
    # Emitente
    #
    n.infNFe.emit.CNPJ.valor  = u'11111111111111'
    n.infNFe.emit.xNome.valor = u'Razao Social Emitente Ltda. EPP'
    n.infNFe.emit.xFant.valor = u'Bromelia'
    n.infNFe.emit.enderEmit.xLgr.valor    = u'R. Ibiuna'
    n.infNFe.emit.enderEmit.nro.valor     = u'729'
    n.infNFe.emit.enderEmit.xCpl.valor    = u'sala 3'
    n.infNFe.emit.enderEmit.xBairro.valor = u'Jd. Guanabara'
    n.infNFe.emit.enderEmit.cMun.valor    = u'3552205'
    n.infNFe.emit.enderEmit.xMun.valor    = u'Sorocaba'
    n.infNFe.emit.enderEmit.UF.valor      = u'SP'
    n.infNFe.emit.enderEmit.CEP.valor     = u'18085520'
    #n.infNFe.emit.enderEmit.cPais.valor   = u'1058'
    #n.infNFe.emit.enderEmit.xPais.valor   = u'Brasil'
    n.infNFe.emit.enderEmit.fone.valor    = u'1534110602'
    n.infNFe.emit.IE.valor = u'111111111111'
    #
    # Regime tributário
    #
    n.infNFe.emit.CRT.valor = u'1'

    #
    # Destinatário
    #
    n.infNFe.dest.CNPJ.valor  = u'11143192000101'
    n.infNFe.dest.xNome.valor = u'Razao Social Destinatario Ltda. EPP'
    n.infNFe.dest.enderDest.xLgr.valor    = u'R. Ibiuna'
    n.infNFe.dest.enderDest.nro.valor     = u'729'
    n.infNFe.dest.enderDest.xCpl.valor    = u'sala 3'
    n.infNFe.dest.enderDest.xBairro.valor = u'Jd. Morumbi'
    n.infNFe.dest.enderDest.cMun.valor    = u'3552205'
    n.infNFe.dest.enderDest.xMun.valor    = u'Sorocaba'
    n.infNFe.dest.enderDest.UF.valor      = u'SP'
    n.infNFe.dest.enderDest.CEP.valor     = u'18085520'
    #n.infNFe.dest.enderDest.cPais.valor   = u'1058'
    #n.infNFe.dest.enderDest.xPais.valor   = u'Brasil'
    n.infNFe.dest.enderDest.fone.valor    = u'1534110602'
    n.infNFe.dest.IE.valor = u'795009239110'

    #
    # Emeio
    #
    n.infNFe.dest.email.valor = u'emeio@servidor.com.br'

    #
    # Detalhe
    #
    d1 = Det_200()

    d1.nItem.valor = 1
    d1.prod.cProd.valor    = u'codigo do produto um'
    d1.prod.cEAN.valor     = u''
    d1.prod.xProd.valor    = u'Descricao do produto'
    d1.prod.NCM.valor      = u'94034000'
    d1.prod.EXTIPI.valor   = u''
    d1.prod.CFOP.valor     = u'5101'
    d1.prod.uCom.valor     = u'UND'
    d1.prod.qCom.valor     = u'100.00'
    d1.prod.vUnCom.valor   = u'10.0000'
    d1.prod.vProd.valor    = u'1000.00'
    d1.prod.cEANTrib.valor = u''
    d1.prod.uTrib.valor    = d1.prod.uCom.valor
    d1.prod.qTrib.valor    = d1.prod.qCom.valor
    d1.prod.vUnTrib.valor  = d1.prod.vUnCom.valor
    d1.prod.vFrete.valor   = u'0.00'
    d1.prod.vSeg.valor     = u'0.00'
    d1.prod.vDesc.valor    = u'0.00'
    d1.prod.vOutro.valor   = u'0.00'
    #
    # Produto entra no total da NF-e
    #
    d1.prod.indTot.valor   = 1

    #
    # Impostos
    #
    d1.imposto.regime_tributario = 1
    d1.imposto.ICMS.CSOSN.valor   = u'400'
    #d1.imposto.ICMS.vBC.valor    = u'1000.00'

    d1.imposto.IPI.CST.valor    = u'99'
    #d1.imposto.IPI.vBC.valor    = u'1000.00'
    #d1.imposto.IPI.pIPI.valor   = u'10.00'
    #d1.imposto.IPI.vIPI.valor   = u'100.00'

    d1.imposto.PIS.CST.valor    = u'06'
    #d1.imposto.PIS.vBC.valor    = u'1000.00'
    #d1.imposto.PIS.pPIS.valor   = u'0.65'
    #d1.imposto.PIS.vPIS.valor   = u'6.50'

    d1.imposto.COFINS.CST.valor    = u'06'
    #d1.imposto.COFINS.vBC.valor    = u'1000.00'
    #d1.imposto.COFINS.pCOFINS.valor   = u'3.00'
    #d1.imposto.COFINS.vCOFINS.valor   = u'30.00'

    #
    # Detalhe
    #
    d2 = Det_200()

    d2.nItem.valor = 2
    d2.prod.cProd.valor    = u'codigo do produto dois'
    d2.prod.cEAN.valor     = u''
    d2.prod.xProd.valor    = u'Descricao do produto'
    d2.prod.NCM.valor      = u'94034000'
    d2.prod.EXTIPI.valor   = u''
    d2.prod.CFOP.valor     = u'5101'
    d2.prod.uCom.valor     = u'UND'
    d2.prod.qCom.valor     = u'100.00'
    d2.prod.vUnCom.valor   = u'10.0000'
    d2.prod.vProd.valor    = u'1000.00'
    d2.prod.cEANTrib.valor = u''
    d2.prod.uTrib.valor    = d1.prod.uCom.valor
    d2.prod.qTrib.valor    = d1.prod.qCom.valor
    d2.prod.vUnTrib.valor  = d1.prod.vUnCom.valor
    d2.prod.vFrete.valor   = u'0.00'
    d2.prod.vSeg.valor     = u'0.00'
    d2.prod.vDesc.valor    = u'0.00'
    d2.prod.vOutro.valor   = u'0.00'
    #
    # Produto entra no total da NF-e
    #
    d2.prod.indTot.valor   = 1

    #
    # Impostos
    #
    d2.imposto.regime_tributario = 1
    d2.imposto.ICMS.CSOSN.valor   = u'400'
    #d2.imposto.ICMS.vBC.valor    = u'1000.00'

    d2.imposto.IPI.CST.valor    = u'99'
    #d2.imposto.IPI.vBC.valor    = u'1000.00'
    #d2.imposto.IPI.pIPI.valor   = u'10.00'
    #d2.imposto.IPI.vIPI.valor   = u'100.00'

    d2.imposto.PIS.CST.valor    = u'06'
    #d2.imposto.PIS.vBC.valor    = u'1000.00'
    #d2.imposto.PIS.pPIS.valor   = u'0.65'
    #d2.imposto.PIS.vPIS.valor   = u'6.50'

    d2.imposto.COFINS.CST.valor    = u'06'
    #d2.imposto.COFINS.vBC.valor    = u'1000.00'
    #d2.imposto.COFINS.pCOFINS.valor   = u'3.00'
    #d2.imposto.COFINS.vCOFINS.valor   = u'30.00'



    #
    # Os primeiros 188 caracteres desta string
    # são todos os caracteres válidos em tags da NF-e
    #
    #d1.infAdProd.valor = u'!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ·¸¹º»¼½¾¿À'

    #
    # Inclui o detalhe na NF-e
    #
    n.infNFe.det.append(d1)

    #
    # Totais
    #
    n.infNFe.total.ICMSTot.vBC.valor     = u'0.00'
    n.infNFe.total.ICMSTot.vICMS.valor   = u'0.00'
    n.infNFe.total.ICMSTot.vBCST.valor   = u'0.00'
    n.infNFe.total.ICMSTot.vST.valor     = u'0.00'
    n.infNFe.total.ICMSTot.vProd.valor   = u'1000.00'
    n.infNFe.total.ICMSTot.vFrete.valor  = u'0.00'
    n.infNFe.total.ICMSTot.vSeg.valor    = u'0.00'
    n.infNFe.total.ICMSTot.vDesc.valor   = u'0.00'
    n.infNFe.total.ICMSTot.vII.valor     = u'0.00'
    n.infNFe.total.ICMSTot.vIPI.valor    = u'0.00'
    n.infNFe.total.ICMSTot.vPIS.valor    = u'0.00'
    n.infNFe.total.ICMSTot.vCOFINS.valor = u'0.00'
    n.infNFe.total.ICMSTot.vOutro.valor  = u'0.00'
    n.infNFe.total.ICMSTot.vNF.valor     = u'0.00'

    n.infNFe.infAdic.infCpl.valor = u'Documento emitido por ME ou EPP optante pelo Simples Nacional. ' \
                                    u'Nao gera direito a credito fiscal de IPI. '
    #
    # O retorno de cada webservice é um dicionário
    # estruturado da seguinte maneira:
    # { TIPO_DO_WS_EXECUTADO: {
    #       u'envio'   : InstanciaDaMensagemDeEnvio,
    #       u'resposta': InstanciaDaMensagemDeResposta,
    #       }
    # }
    #
    for processo in p.processar_notas([n]):
        print
        print
        print processo.envio.xml
        print
        print processo.resposta.xml
        print
        assert processo.resposta.reason != u'Forbidden'

