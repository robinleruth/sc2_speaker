'use strict';

var app = app || {};

app.BaseModel = Backbone.Model.extend({
    sync: function(){
        return null;
    },
    toFormat: function(){
        this.set('notional', Number(this.stringToNumber(this.get('notional'))), {silent: true});
    },
    toVisual: function(){
        this.set('notional', this.numberWithCommas(this.get('notional')), {silent: true});
    },
    compute: function(){
        this.toFormat();
        var j = this.toJSON();
        this.toVisual();
        (function(model){
            $.ajax({
                url: '',
                type: 'POST',
                data: JSON.stringify(j),
                contentType: 'application/json',
                success: function(data){
                    model.save(data);
                    model.toVisual();
                }
            });
        })(this);
    },
    toFormatOne: function(attr){
        this.set(attr, Number(this.stringToNumber(this.get(attr))));
    },
    toVisualOne: function(attr){
        this.set(attr, this.numberWithCommas(this.get(attr)));
    },
    stringToNumber: function(number){
        return String(number).replace(/,/g, '');
    },
    numberWithCommas: function(x){
        return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',');
    },
});
