'use strict';

var app = app || {};

app.ActionView = Backbone.View.extend({
    template: _.template($('#action_view_template').html()),
    initialize: function(){
        this.listenTo(this.model, 'change', this.render);
        this.listenTo(this.model, 'destroy', this.remove);
    },
    render: function(){
        this.$el.html(this.template(this.model.toJSON()));
        return this;
    }
});
