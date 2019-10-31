import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo12-addons-oca-sale-workflow",
    description="Meta package for oca-sale-workflow Odoo addons",
    version=version,
    install_requires=[
        'odoo12-addon-partner_prospect',
        'odoo12-addon-portal_sale_personal_data_only',
        'odoo12-addon-sale_automatic_workflow',
        'odoo12-addon-sale_automatic_workflow_payment_mode',
        'odoo12-addon-sale_cancel_reason',
        'odoo12-addon-sale_commercial_partner',
        'odoo12-addon-sale_disable_inventory_check',
        'odoo12-addon-sale_discount_display_amount',
        'odoo12-addon-sale_double_validation',
        'odoo12-addon-sale_exception',
        'odoo12-addon-sale_force_invoiced',
        'odoo12-addon-sale_invoice_group_method',
        'odoo12-addon-sale_invoice_plan',
        'odoo12-addon-sale_last_price_info',
        'odoo12-addon-sale_merge_draft_invoice',
        'odoo12-addon-sale_milestone_profile_invoicing',
        'odoo12-addon-sale_order_action_invoice_create_hook',
        'odoo12-addon-sale_order_archive',
        'odoo12-addon-sale_order_digitized_signature',
        'odoo12-addon-sale_order_general_discount',
        'odoo12-addon-sale_order_invoicing_finished_task',
        'odoo12-addon-sale_order_line_description',
        'odoo12-addon-sale_order_line_input',
        'odoo12-addon-sale_order_line_price_history',
        'odoo12-addon-sale_order_line_sequence',
        'odoo12-addon-sale_order_price_recalculation',
        'odoo12-addon-sale_order_revision',
        'odoo12-addon-sale_order_type',
        'odoo12-addon-sale_partner_incoterm',
        'odoo12-addon-sale_product_multi_add',
        'odoo12-addon-sale_product_set',
        'odoo12-addon-sale_shipping_info_helper',
        'odoo12-addon-sale_stock_picking_blocking',
        'odoo12-addon-sale_stock_sourcing_address',
        'odoo12-addon-sale_validity',
        'odoo12-addon-sales_team_security',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)