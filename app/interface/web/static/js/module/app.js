'use strict';

var app = app || {};

(function(){
    app.colAction = new app.ColAction();

    app.colActionView = new app.ColActionView({collection: app.colAction});
})();
