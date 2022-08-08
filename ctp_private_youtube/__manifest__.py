# -*- coding: utf-8 -*-
###################################################################################
#
#    Cybernetics Plus Co., Ltd.
#    Elearning Disabled Click Youtube Video Link
#
###################################################################################

{
    'name': 'Cybernetics Disabled Click Youtube',
    'version': '14.0.0.1.1',
    'summary': """ 
            Elearning Disabled Click Youtube Video Link
            .""",
    'description': """ 
            Elearning Disabled Click Youtube Video Link
            .""",
    'author': 'Cybernetics Plus Co., Ltd.',
    'website': 'https://www.cybernetics.plus',
    'live_test_url': 'https://www.cybernetics.plus',
    'images': ['static/description/banner.png'],
    'category': 'Website',
    'license': 'AGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False,
    'price': 54,
    'currency': 'USD',
    'contributors': [
        'Developer <dev@cybernetics.plus>',
    ],
    'depends': ['base','website_slides'],
    'assets': {
        "web.assets_frontend": [
            "ctp_private_youtube/static/src/css/style.css",
            "ctp_private_youtube/static/src/js/script.js",
        ],
    },
}
