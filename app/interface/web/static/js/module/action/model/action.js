'use strict';

var app = app || {};

app.Action = Backbone.Model.extend({
    defaults: function(){
        return {
            time: 0,
            name: "Name",
            action_type: "fixed_action",
            build_order_id: 0
        };
    }
});
