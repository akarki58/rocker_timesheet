/** @odoo-module */

import { CalendarController } from '@web/views/calendar/calendar_controller';

import { useService } from "@web/core/utils/hooks";

export class RockerCalendarController extends CalendarController {
    setup() {
        super.setup();
        this.actionService = useService("action");
    }
       all() {
//            alert('test from my  module');
            this.actionService.doAction("rocker_timesheet.action_searchpanel_all_tasks", {
                additionalContext: {
            //        default_project_id: this.projectId,
            //        active_id: this.projectId,
                },
            });
        }
       member() {this.actionService.doAction("rocker_timesheet.action_searchpanel_member_tasks", {});}
       billable() {this.actionService.doAction("rocker_timesheet.action_searchpanel_billable_tasks", {});}
       nonbillable() {this.actionService.doAction("rocker_timesheet.action_searchpanel_nonbillable_tasks", {});}
       internal() {this.actionService.doAction("rocker_timesheet.action_searchpanel_internal_tasks", {});}
       mine() {this.actionService.doAction("rocker_timesheet.action_searchpanel_mine_tasks", {});}

}
//RockerCalendarController.template = "rocker_timesheet.CalendarController";
RockerCalendarController.components = {
    ...RockerCalendarController.components,
//    FilterPanel: RockerCalendarFilterPanel,
}
