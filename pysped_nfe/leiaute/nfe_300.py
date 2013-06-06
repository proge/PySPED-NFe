# -*- coding: utf-8 -*-

##############################################################################
#                                                                            #
#  Copyright (C) 2013 Proge Informática Ltda (<http://www.proge.com.br>).    #
#                                                                            #
#  Author Daniel Hartmann <daniel@proge.com.br>                              #
#                                                                            #
#  This program is free software: you can redistribute it and/or modify      #
#  it under the terms of the GNU Affero General Public License as            #
#  published by the Free Software Foundation, either version 3 of the        #
#  License, or (at your option) any later version.                           #
#                                                                            #
#  This program is distributed in the hope that it will be useful,           #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of            #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             #
#  GNU Affero General Public License for more details.                       #
#                                                                            #
#  You should have received a copy of the GNU Affero General Public License  #
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.     #
#                                                                            #
##############################################################################

from __future__ import division, print_function, unicode_literals

from pysped_tools import *
from pysped_nfe.leiaute import ESQUEMA_ATUAL_VERSAO_3 as ESQUEMA_ATUAL
from pysped_nfe.leiaute import nfe_200
import os

DIRNAME = os.path.dirname(__file__)


class Dest(nfe_200.Dest):
    def __init__(self):
        super(Dest, self).__init__()
        self.idEstrangeiro

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<dest>'

        if self.CPF.valor:
            xml += self.CPF.xml
        elif self.CNPJ.valor:
            xml += self.CNPJ.xml
        else:
            xml += self.idEstrangeiro.xml

        xml += self.xNome.xml
        xml += self.enderDest.xml
        xml += self.IE.xml
        xml += self.ISUF.xml
        xml += self.email.xml
        xml += '</dest>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.CNPJ.xml = arquivo
            self.CPF.xml = arquivo
            self.idEstrangeiro.xml = arquivo
            self.xNome.xml = arquivo
            self.enderDest.xml = arquivo
            self.IE.xml = arquivo
            self.ISUF.xml = arquivo
            self.email.xml = arquivo

    def get_txt(self):
        txt = 'E|'
        txt += self.xNome.txt + '|'
        txt += self.IE.txt + '|'
        txt += self.ISUF.txt + '|'
        txt += self.email.txt + '|'
        txt += '\n'

        if self.CPF.valor:
            txt += 'E03|' + self.CPF.txt + '|\n'
        elif self.CNPJ.valor:
            txt += 'E02|' + self.CNPJ.txt + '|\n'
        else:
            txt += 'E|' + self.idEstrangeiro.txt + '|\n'

        txt += self.enderDest.txt
        return txt


class Ide(nfe_200.Ide):
    def __init__(self):
        super(Ide, self).__init__()
        self.dhEmi = TagDataHora(nome='dhEmi', codigo='B09', raiz='//NFe/infNFe/ide')
        self.dhSaiEnt = TagDataHora(nome='dhSaiEnt', codigo='B10a', raiz='//NFe/infNFe/ide', obrigatorio=False)
        self.idDest
        self.indFinal
        self.indPres

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ide>'
        xml += self.cUF.xml
        xml += self.cNF.xml
        xml += self.natOp.xml
        xml += self.indPag.xml
        xml += self.mod.xml
        xml += self.serie.xml
        xml += self.nNF.xml
        xml += self.dhEmi.xml
        xml += self.dhSaiEnt.xml
        xml += self.tpNF.xml
        xml += self.idDest.xml
        xml += self.cMunFG.xml

        for nr in self.NFref:
            xml += nr.xml

        xml += self.tpImp.xml
        xml += self.tpEmis.xml
        xml += self.cDV.xml
        xml += self.tpAmb.xml
        xml += self.finNFe.xml
        xml += self.procEmi.xml
        xml += self.verProc.xml
        xml += self.dhCont.xml
        xml += self.xJust.xml
        xml += '</ide>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cUF.xml = arquivo
            self.cNF.xml = arquivo
            self.natOp.xml = arquivo
            self.indPag.xml = arquivo
            self.mod.xml = arquivo
            self.serie.xml = arquivo
            self.nNF.xml = arquivo
            self.dhEmi.xml = arquivo
            self.dhSaiEnt.xml = arquivo
            self.tpNF.xml = arquivo
            self.idDest.xml = arquivo
            self.cMunFG.xml = arquivo

            #
            # Técnica para leitura de tags múltiplas
            # As classes dessas tags, e suas filhas, devem ser
            # "reenraizadas" (propriedade raiz) para poderem ser
            # lidas corretamente
            #
            self.NFRef = self.le_grupo('//NFe/infNFe/ide/NFref', NFRef)

            self.tpImp.xml = arquivo
            self.tpEmis.xml = arquivo
            self.cDV.xml = arquivo
            self.tpAmb.xml = arquivo
            self.finNFe.xml = arquivo
            self.procEmi.xml = arquivo
            self.verProc.xml = arquivo
            self.dhCont.xml = arquivo
            self.xJust.xml = arquivo

    def get_txt(self):
        txt = 'B|'
        txt += self.cUF.txt + '|'
        txt += self.cNF.txt + '|'
        txt += self.natOp.txt + '|'
        txt += self.indPag.txt + '|'
        txt += self.mod.txt + '|'
        txt += self.serie.txt + '|'
        txt += self.nNF.txt + '|'
        txt += self.dhEmi.txt + '|'
        txt += self.dhSaiEnt.txt + '|'
        txt += self.tpNF.txt + '|'
        txt += self.idDest.txt + '|'
        txt += self.cMunFG.txt + '|'
        txt += self.tpImp.txt + '|'
        txt += self.tpEmis.txt + '|'
        txt += self.cDV.txt + '|'
        txt += self.tpAmb.txt + '|'
        txt += self.finNFe.txt + '|'
        txt += self.procEmi.txt + '|'
        txt += self.verProc.txt + '|'
        txt += self.dhCont.txt + '|'
        txt += self.xJust.txt + '|'
        txt += '\n'

        for nr in self.NFref:
            txt += nr.txt

        return txt


class NFe(nfe_200.NFe):
    def __init__(self):
        super(NFe, self).__init__()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'nfe_v3.00.xsd'

    def monta_chave(self):
        self.gera_nova_chave()
        # Código da UF do emitente do Documento Fiscal
        chave = unicode(self.infNFe.ide.cUF.valor).strip().rjust(2, '0')
        # Ano e Mês da emissão da NF-e
        chave += unicode(self.infNFe.ide.dhEmi.valor.strftime('%y%m')).strip().rjust(4, '0')
        # CNPJ do emitente
        chave += unicode(self.infNFe.emit.CNPJ.valor).strip().rjust(14, '0')
        # Modelo do Documento Fiscal
        chave += '55'
        # Série do Documento Fiscal
        chave += unicode(self.infNFe.ide.serie.valor).strip().rjust(3, '0')
        # Número do Documento Fiscal
        chave += unicode(self.infNFe.ide.nNF.valor).strip().rjust(9, '0')
        # Forma de emissão da NF-e
        chave += unicode(self.infNFe.ide.tpEmis.valor).strip().rjust(1, '0')
        # Código numérico que compõe a Chave de Acesso
        chave += unicode(self.infNFe.ide.cNF.valor).strip().rjust(8, '0')
        # Dígito verificador da Chave de Acesso
        self.infNFe.ide.cDV.valor = self.modulus11(chave)
        chave += unicode(self.infNFe.ide.cDV.valor).strip().rjust(1, '0')

        self.chave = chave
