# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Inventory Closing + Operating Unit",
    "version": "14.0.1.0.0",
    "website": "https://simetri-sinergi.id",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "ssi_inventory_closing",
        "ssi_operating_unit_mixin",
    ],
    "data": [
        "security/res_group/inventory_closing.xml",
        "security/ir_rule/inventory_closing.xml",
        "view/inventory_closing.xml",
    ],
}
