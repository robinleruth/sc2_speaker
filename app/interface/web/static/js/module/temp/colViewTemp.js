'use strict';

var app = app || {};

app.ColViewTemp = app.ColBaseView.extend({
    el: $('#temp'),
    addOne: function(model){
        var view = new app.ViewTemp({model: model});
        this.$el.append(view.render().el);
    },
});
