'use strict';

var app = app || {};

app.ColAction = Backbone.Collection.extend({
    initialize: function(models, options){
        this.build_order = options.build_order || '';
    },
    model: app.Action,
    url: function(){
        return '/api/v1/actions/' + this.build_order;
    },
    // comparator: 'time'
});
