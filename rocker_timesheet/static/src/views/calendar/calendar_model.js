/** @odoo-module */
import { CalendarModel } from '@web/views/calendar/calendar_model';
//import { useService } from "@web/core/utils/hooks";
//import { onWillStart } from "@odoo/owl";
//import { session } from "@web/session";
//var rpc = require('web.rpc');
//var defaultModeSet = false;
//var defaultMode = 'week';

// ************** problem with sync , async ****************************
//    async function get_rocker_defaults() {
//                   console.log('function get_rocker_user_defaults');
//                   var model = 'rocker.user.defaults';
//                    var uid = session.uid;
//                    var cid = session.user_companies.current_company;
//                   var res = rpc.query({
//                      model: model,
//                      method: 'get_rocker_user_defaults',
//                      args: [uid, cid],
//                       }).then(function (data) {
//                        console.log(data);
//                        if (data[0] > 0) {
////                            console.log('Found User Defaults');
//                            defaultMode = data[2];
//                            return true;
//                            }
//                            console.log('No User Defaults, creating defs');
//                           defaultMode = "month";
//                           return true;
//
//                        });
//
//    }



export class RockerCalendarModel extends CalendarModel {
     setup(params, services) {
        console.log('model setup');
        var self = this;
//        var res = get_rocker_defaults();
        return super.setup(...arguments);
    }

//    load(params) {
//        console.log('model load');
//        var self = this;
//        var res = get_rocker_defaults();
//        return super.load(...arguments);
//    }


}
