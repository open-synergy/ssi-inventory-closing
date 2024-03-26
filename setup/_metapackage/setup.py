import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-open-synergy-ssi-inventory-closing",
    description="Meta package for open-synergy-ssi-inventory-closing Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-ssi_inventory_closing',
        'odoo14-addon-ssi_inventory_closing_queue',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
