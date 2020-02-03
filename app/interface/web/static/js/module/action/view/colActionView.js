'use strict';

var app = app || {};

app.ColActionView = Backbone.View.extend({
    el: $('#app'),
    initialize: function(){
        this.listenTo(this.collection, 'add', this.addOne);
        this.listenTo(this.collection, 'remove', this.render);
        this.listenTo(this.collection, 'reset', this.addAll);
        this.render();
    },
    addOne: function(model){
        var view = new app.ActionView({model: model});
        this.$el.append(view.render().el);
    },
    addAll: function(){
        this.collection.each(this.addOne, this);
    },
    render: function(){
    }
});
