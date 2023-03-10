/** @odoo-module */

import { calendarView } from '@web/views/calendar/calendar_view';
import { RockerCalendarController } from './calendar_controller';
import { RockerCalendarModel } from './calendar_model';
import { RockerCalendarRenderer} from './calendar_renderer';

import { registry } from '@web/core/registry';

const RockerCalendarView = {
    ...calendarView,

    Controller: RockerCalendarController,
    Renderer: RockerCalendarRenderer,
    Model: RockerCalendarModel,

    buttonTemplate: "rocker_timesheet.CalendarController.controlButtons",


}

registry.category('views').add('rocker_calendar', RockerCalendarView);
