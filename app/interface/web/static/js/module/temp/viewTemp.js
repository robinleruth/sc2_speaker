'use strict';

var app = app || {};

app.ViewTemp = app.BaseView.extend({
    template: _.template($('#generic_view_template').html()),
});
