'use strict';

var app = app || {};

app.ColAction = Backbone.Collection.extend({
    model: app.Action,
    url: '/api/v1/actions'
});
