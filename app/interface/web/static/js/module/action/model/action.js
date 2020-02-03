'use strict';

var app = app || {};

app.Action = Backbone.Model.extend({
    defaults: function(){
        return {
            id: 0,
            time: 0,
            name: "",
            action_type: ""
        };
    }
});
