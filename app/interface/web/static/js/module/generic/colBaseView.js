'use strict';

var app = app || {};

app.ColBaseView = Backbone.View.extend({
    events: {
        'click .new_one': 'create',
    },
    initialize: function(){
        this.listenTo(this.collection, 'add', this.addOne);
        // this.listenTo(this.collection, 'remove', this.render);
        this.listenTo(this.collection, 're-render', this.render);
        this.render();
    },
    render: function(){},
    addOne: function(model){},
    addAll: function(){
        this.collection.each(this.addOne, this);
    },
    create: function(){
        this.collection.create();
    }
});
