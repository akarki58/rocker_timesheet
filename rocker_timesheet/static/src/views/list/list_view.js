/** @odoo-module **/
//
// 2025-01-25
//

import { registry } from "@web/core/registry";
import { listView } from "@web/views/list/list_view";
import { RockerListController } from './list_controller';

export const RockerListView = {
    ...listView,
    Controller: RockerListController,
    buttonTemplate: "rocker_timesheet.list_buttons",
};

registry.category("views").add("rocker_list", RockerListView);

