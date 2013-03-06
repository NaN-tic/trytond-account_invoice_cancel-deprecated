====================
Cancelación facturas
====================

Permite la cancelación de facturas, pasarlas después a borrador y volver a
aprobarlas.

Si la factura tiene relacionado un apunte contable lo elimina para poder
cancelarla y volver a aprobarla. Si el apunte está realizado, la factura no se
cancelará.

Configuración
-------------

Para permitir la cancelación de facturas abra el menú |menú_account_journal| y
marque la opción de **Permitir la cancelación de facturas**.

.. |menú_account_journal| tryref:: account.menu_journal_configuration/complete_name

Para permitir la cancelación de facturas provinientes de pedidos de venta o de
compra, se deben instalar también los módulos `Cancelación facturas compras`_ y
`Cancelación facturas ventas`_.

.. _Cancelación facturas compras: ../purchase_invoice_cancel/index.html
.. _Cancelación facturas ventas: ../sale_invoice_cancel/index.html

Módulos que dependen
====================

Instalados
----------

.. toctree::
   :maxdepth: 1

   /account/index

Dependencias
------------

* Contabilidad_

.. _Contabilidad: ../account/index.html
