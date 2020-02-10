'use strict';

var app = app || {};

app.Temp = app.BaseModel.extend({
    defaults: function(){
        return {
            notional: '0'
        }
    },
});
