'use strict';

var app = app || {};

app.Action = Backbone.Model.extend({
    defaults: function(){
        return {
            time: 0,
            name: ""
        };
    },
    sync: function(){
        return null;
    }
});
