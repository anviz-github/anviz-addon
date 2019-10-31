# -*- coding: utf-8 -*-
#################################################################################
# Author      : Webkul Software Pvt. Ltd. (<https://webkul.com/>)
# Copyright(c): 2015-Present Webkul Software Pvt. Ltd.
# All Rights Reserved.
#
#
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#
# You should have received a copy of the License along with this program.
# If not, see <https://store.webkul.com/license.html/>
#################################################################################
{
  "name"                 :  "Backbone For Shipping Api Integration",
  "summary"              :  "ODOO-Shipping Service API Integration: PROVIDE CORE SERVICE LAYER FOR API INTEGRATION  With FedEx , USPS, UPS, DHL, Australia Post, Aramex, Canada Post, Hermes etc.",
  "category"             :  "Website",
  "version"              :  "1.1.3",
  "author"               :  "Webkul Software Pvt. Ltd.",
  "website"              :  "https://store.webkul.com/Odoo.html",
  "description"          :  """FedEx , USPS, UPS, DHL, DHL Intraship, Australia Post, Hermes, Canada Post, and Aramex Shipping API Integration as Odoo Delivery Method .
  Provide Shipping Label Generation and Shipping Rate Calculator For Website as Well Odoo BackEnd.""",
  "depends"              :  [
                             'product',
                             'wk_wizard_messages',
                             'delivery',
                            ],
  "data"                 :  [
                             'security/ir.model.access.csv',
                             'data/data.xml',
                             'views/carrier_history.xml',
                             'views/delivery_view.xml',
                             'views/product_packaging.xml',
                             'views/res_config.xml',
                             'views/sale.xml',
                             'views/stock_picking.xml',
                             'views/stock_quant.xml',
                            ],
  "images"               :  ['static/description/Banner.png'],
  "application"          :  True,
  "installable"          :  True,
  "auto_install"         :  False,
  "pre_init_hook"        :  "pre_init_check",
}