'use strict';

var app = app || {};

(function(){
    app.colTemp = new app.ColTemp();
    app.colTempView = new app.ColViewTemp({collection: app.colTemp});
})();
