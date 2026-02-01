/** @odoo-module */
//
// 2026-01-25
//
//import { registry } from '@web/core/registry';
import { listView } from '@web/views/list/list_view';
import { ListController } from '@web/views/list/list_controller';
import { useService } from "@web/core/utils/hooks";

export class RockerListController extends ListController {
    setup() {
        console.log('setup');
        super.setup();
        this.actionService = useService("action");
      }

//    get buttons() {
//        return [
//            ...super.buttons,
//            {
//                name: "roller",
//                label: "New Rolling",
//                class: "btn-primary",
//                onClick: () => this.onRollerClick(),
//            },
//        ];
//    }

    async OnRollerClick() {
        var self = this;
       await this.actionService.doAction("rocker_timesheet.action_create_rolling", {
            on_close: function () {
                console.log('OnRollerClick close');
            }
        });
//        $(document).find('.o_list_button_add').click();
        var add_button = document.getElementsByClassName('o_list_button_add')[0];
        console.log(add_button);
        add_button.click();
    }
    async all() {await this.actionService.doAction("rocker_timesheet.action_searchpanel_all_tasks", {});}
    async member() {await this.actionService.doAction("rocker_timesheet.action_searchpanel_member_tasks", {});}
    async billable() {await this.actionService.doAction("rocker_timesheet.action_searchpanel_billable_tasks", {});}
    async nonbillable() {await this.actionService.doAction("rocker_timesheet.action_searchpanel_nonbillable_tasks", {});}
    async internal() {await this.actionService.doAction("rocker_timesheet.action_searchpanel_internal_tasks", {});}
    async mine() {await this.actionService.doAction("rocker_timesheet.action_searchpanel_mine_tasks", {});}

}
RockerListController.template = "rocker_timesheet.RockerListController";
//registry.category("views").add("rocker_list", {
//    ...listView,
//    Controller: RockerListController,
//    buttonTemplate: "rocker_timesheet.list_buttons",
//});

RockerListController.components = {
    ...RockerListController.components,

//    QuickCreateFormView: CalendarQuickCreate,
}
