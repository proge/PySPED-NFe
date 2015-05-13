PySPED-NFe
==========

Code refactoring and segmentation from Aristides Caldeira's [PySPED](https://github.com/aricaldeira/PySPED).

Setup
-----

#### Instalar dependências via pip

pip install pyOpenSSL==0.14 geraldo

#### Instalar libxml

wget ftp://xmlsoft.org/libxml2/libxml2-sources-2.7.8.tar.gz

tar xvzf libxml2-sources-2.7.8.tar.gz

cd libxml2-2.7.8/python

python setup.py install

#### Instalar pyxmlsec

De acordo com o Aristildes Caldeira [1], há um bug na biblioteca PyXMLSec versão 64 bits.
Uma solução é instalar o xmlsec na mão com o patch indicado [2].

[1] - https://groups.google.com/group/pynfe/browse_thread/thread/43bdb756d8252bf5

[2] - http://pastebin.com/4QwzC1jX

wget http://labs.libre-entreprise.org/download.php/430/pyxmlsec-0.3.0.tar.gz

tar xvzf pyxmlsec-0.3.0.tar.gz

cd pyxmlsec-0.3.0

Diff:
```
--- pyxmlsec-0.3.0/setup.py     2006-01-01 15:43:37.000000000 -0200
+++ pyxmlsec-0.3.0/setup.py     2009-11-10 17:57:29.390253522 -0200
@@ -182,7 +182,8 @@
                define_macros = define_macros,
                include_dirs  = include_dirs,
                library_dirs  = library_dirs,
-               libraries     = libraries
+               libraries     = libraries,
+               extra_compile_args = ['-DXMLSEC_NO_SIZE_T']
                )
```

python setup.py install


#### Instalar PySPED-NFe

git clone https://github.com/proge/PySPED-NFe.git

cd PySPED-NFe

python setup.py install
