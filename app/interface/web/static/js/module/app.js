'use strict';

var app = app || {};

(function(){
    app.colAction = new app.ColAction(null, {build_order: ''});

    app.colActionView = new app.ColActionView({collection: app.colAction});
    app.colAction.fetch();
})();
