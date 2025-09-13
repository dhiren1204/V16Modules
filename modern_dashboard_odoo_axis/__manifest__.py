# -*- coding: utf-8 -*-
{
    'name': "Modern Odoo Dashboards for CRM, Inventory, Sales, Account, Invoice and POS Dashboard",
    'description' : "Modern Odoo Dashboards - CRM Dashboard, Inventory Dashboard, Sales Dashboard, Account Dashboard, Invoice Dashboard, Odoo POS Dashboard, all in one dashboard, beautiful dashboard, create dashboard, dynamic dashboard ",
    'version': '16.0.0.5',
   'summary': "Odoo Dashboard CRM dashboard inventory dashboard sales dashboard account dashboard POS dashboard Invoice Dashboard revamp dashboard in odoo best dashboard odoo apps dashboard ninja analytic large data best ninja dashboard analytic dashboard pre-configured Dashboard create dashboard beautiful dashboard customized robust dashboard predefined dashboard  multiple dashboards advance dashboard Beautiful Powerful Dashboards chart graphs table view All in One Dynamic Dashboard accounting stock Dashboard pie chart dashboard create own dashboard modern dashboard.",
    'live_test_url': 'https://youtu.be/puGmVsi_LtY',

    'depends': ['base','sale_management','crm','stock','account','hr_attendance'],


    'data': [
        'security/security.xml',
        # 'views/assets.xml',
        'views/sale_search_view.xml',
        # 'views/pos_config.xml',
        'views/account_search_view.xml',
        'views/crm_search_view.xml',
        'views/inventory_searcch_view.xml',
        'views/menu_dashboard_view.xml',
    ],

    'application': True,

    'assets': {
     'web._assets_primary_variables': [
      'modern_dashboard_odoo_axis/static/src/scss/style.scss',

     ],
     'web.assets_backend': [
      '/modern_dashboard_odoo_axis/static/src/xml/**/*',
      '/modern_dashboard_odoo_axis/static/src/js/account_dashbboard.js',
      '/modern_dashboard_odoo_axis/static/src/js/crm_dashboard.js',
      '/modern_dashboard_odoo_axis/static/src/js/inventory_dashboard.js',
      '/modern_dashboard_odoo_axis/static/src/js/sale_dashboard.js',
      '/modern_dashboard_odoo_axis/static/src/js/sales_dashboard.js',

      'modern_dashboard_odoo_axis/static/src/scss/lib/nv.d3.css',
      'modern_dashboard_odoo_axis/static/src/js/lib/d3.min.js',
      'modern_dashboard_odoo_axis/static/src/js/jquery.dataTables.min.js',

      'modern_dashboard_odoo_axis/static/lib/charts/Chart.bundle.js',
      'modern_dashboard_odoo_axis/static/lib/charts/Chart.bundle.min.js',
      'modern_dashboard_odoo_axis/static/lib/charts/Chart.min.js',
      'modern_dashboard_odoo_axis/static/lib/charts/Chart.js',
      # database tables
      'modern_dashboard_odoo_axis/static/lib/dataTables/datatables.min.js',
      'modern_dashboard_odoo_axis/static/lib/dataTables/dataTables.buttons.min.js',
      'modern_dashboard_odoo_axis/static/lib/dataTables/buttons.flash.min.js',
      'modern_dashboard_odoo_axis/static/lib/dataTables/buttons.html5.min.js',
      'modern_dashboard_odoo_axis/static/lib/dataTables/buttons.print.min.js',
      'modern_dashboard_odoo_axis/static/lib/dataTables/pdfmake.min.js',
      'modern_dashboard_odoo_axis/static/lib/dataTables/vfs_fonts.js',
      'modern_dashboard_odoo_axis/static/lib/dataTables/jszip.min.js',
      'modern_dashboard_odoo_axis/static/lib/dataTables/buttons.bootstrap.min.js',
      'modern_dashboard_odoo_axis/static/lib/dataTables/buttons.bootstrap4.min.js',
      'modern_dashboard_odoo_axis/static/lib/dataTables/buttons.colVis.min.js',
      # export pdf
      'modern_dashboard_odoo_axis/static/lib/jsPdf/jspdf.min.js',
      'modern_dashboard_odoo_axis/static/lib/jsPdf/jspdf.debug.js',
      # Css scripts for dashboard view and table
      'modern_dashboard_odoo_axis/static/lib/dataTables/datatables.min.css',
      'modern_dashboard_odoo_axis/static/lib/dataTables/buttons.dataTables.min.css',
      'modern_dashboard_odoo_axis/static/src/js/models.js',
      'modern_dashboard_odoo_axis/static/src/js/lib/canvasjs.min.js',

      'modern_dashboard_odoo_axis/static/src/js/backend_dashboard_js/dashboard.js',
      'modern_dashboard_odoo_axis/static/src/js/backend_dashboard_js/amcharts.js',
      'modern_dashboard_odoo_axis/static/src/js/backend_dashboard_js/serial.js',
      'modern_dashboard_odoo_axis/static/src/js/backend_dashboard_js/jquery.dataTables.min.js',
      'modern_dashboard_odoo_axis/static/src/js/backend_dashboard_js/daterangepicker.js',
      'modern_dashboard_odoo_axis/static/src/js/backend_dashboard_js/pie.js',
      'modern_dashboard_odoo_axis/static/src/js/backend_dashboard_js/export.js',
      'modern_dashboard_odoo_axis/static/src/js/backend_dashboard_js/light.js',
      'modern_dashboard_odoo_axis/static/src/js/backend_dashboard_js/list.js',
      'modern_dashboard_odoo_axis/static/src/js/backend_dashboard_js/libs/blob.js/blob.js',
      'modern_dashboard_odoo_axis/static/src/js/backend_dashboard_js/libs/fabric.js/fabric.min.js',
      'modern_dashboard_odoo_axis/static/src/js/backend_dashboard_js/libs/pdfmake/pdfmake.min.js',
      'modern_dashboard_odoo_axis/static/src/js/backend_dashboard_js/libs/pdfmake/vfs_fonts.js',
      'modern_dashboard_odoo_axis/static/src/js/backend_dashboard_js/libs/jszip/jszip.min.js',
      'modern_dashboard_odoo_axis/static/src/js/backend_dashboard_js/libs/xlsx/xlsx.min.js',
      'modern_dashboard_odoo_axis/static/src/js/backend_dashboard_js/libs/FileSaver.js/FileSaver.min.js',
      'modern_dashboard_odoo_axis/static/src/css/custom.css',
      'modern_dashboard_odoo_axis/static/src/css/custom_design.css',
      'modern_dashboard_odoo_axis/static/src/css/daterangepicker.css',
      'modern_dashboard_odoo_axis/static/src/css/export.css',
      # 'modern_dashboard_odoo_axis/static/src/css/pos_style.css',
      'modern_dashboard_odoo_axis/static/src/css/sales_dashboard.css',
      'modern_dashboard_odoo_axis/static/src/css/style.css',
     ],

    },

    'license': 'OPL-1',
    'price': 85,
    'currency': 'USD',
    'support': 'business@axistechnolabs.com',
    'author': 'Axis Technolabs',
    'website': 'https://www.axistechnolabs.com',
    'images': ['static/description/images/modern_dashboard.gif','static/description/images/Banner-Img.png',],        
}
