odoo.define('rocker_timesheet.tree-button', function (require) {
"use strict";
var ListController = require('web.ListController');
var ListView = require('web.ListView');
var viewRegistry = require('web.view_registry');
var TreeButton = ListController.extend({
   buttons_template: 'rocker_timesheet.tree-button',
   events: _.extend({}, ListController.prototype.events, {
        'click .all2': '_All2',
        'click .member2': '_Member2',
        'click .billable2': '_Billable2',
        'click .nonbillable2': '_NonBillable2',
        'click .internal2': '_Internal2',
        'click .mine2': '_Mine2',
        'click .roller2': '_CreateRolling2',
   }),
   _All2: function () {
            var self = this;
            this.do_action('rocker_timesheet.action_searchpanel_all_tasks', {
                on_close: function () {
                }
            });
   },
    _Member2: function () {
        var self = this;
        this.do_action('rocker_timesheet.action_searchpanel_member_tasks', {
            on_close: function () {
            }
        });
    },
    _Billable2: function () {
        var self = this;
        this.do_action('rocker_timesheet.action_searchpanel_billable_tasks', {
            on_close: function () {
            }
        });
    },
    _NonBillable2: function () {
        var self = this;
        this.do_action('rocker_timesheet.action_searchpanel_nonbillable_tasks', {
            on_close: function () {
            }
        });
    },
    _Internal2: function () {
        var self = this;
        this.do_action('rocker_timesheet.action_searchpanel_internal_tasks', {
            on_close: function () {
            }
        });
    },
    _Mine2: function () {
        var self = this;
        this.do_action('rocker_timesheet.action_searchpanel_mine_tasks', {
            on_close: function () {
            }
        });
    },
    _CreateRolling2: async function () {
        var self = this;
        await this.do_action('rocker_timesheet.action_create_rolling', {
            on_close: function () {
            }
        });
//            console.log('Wait');
//            await;
        $(this.$buttons).find('.o_list_button_add').click();
    },
});
var RockerListView = ListView.extend({
   config: _.extend({}, ListView.prototype.config, {
       Controller: TreeButton,
   }),
});
viewRegistry.add('rocker_tree', RockerListView);
});