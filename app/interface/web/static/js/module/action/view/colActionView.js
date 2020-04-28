'use strict';

var app = app || {};

app.ColActionView = Backbone.View.extend({
    el: $('#app'),
    events: {
        'click .new_one': 'create',
        'click .create_new_build': 'display_input',
        'click .launch': 'launch',
        'click .test_audio': 'testAudio',
        'click .toogle_voice': 'toogleVoice',
        'blur .build_order_name': 'fetch_actions',
        'blur .dropdown': 'fetch_actions',
        'blur #new_build_name': 'create_new_build_order',
    },
    initialize: function(){
        this.english_voice = true;
        this.voice_name = 'Google US English';
        this.listenTo(this.collection, 'add', this.addOne);
        this.listenTo(this.collection, 'remove', this.render);
        this.listenTo(this.collection, 'reset', this.addAll);
        this.populate_select();
        this.render();
    },
    display_input: function() {
        this.input = this.$('#new_build_name');
        this.input.css('display', 'block');
        this.input.focus();
    },
    create_new_build_order: function() {
        this.input.css('display', 'none');
        var view = this;
        $.post('/api/v1/create_new_build_order', {name: this.input.val()})
            .done(function(data){
                view.populate_select();
                var name = view.input.val();
                setTimeout(function(){
                    view.$('.dropdown').get()[0].value = name;
                    view.fetch_actions(data.id);
                }, 500);
            });
    },
    populate_select: function() {
        let dropdown = this.$('.dropdown');
        dropdown.empty();
        dropdown.append('<option selected="true" disabled>Choose build order</option>');
        dropdown.prop('selectedIndex', 0);
        const url = '/api/v1/get_all_build_orders_name';
        // Populate dropdown with list of provinces
        $.getJSON(url, function (data) {
            $.each(data, function (key, entry) {
                dropdown.append($('<option></option>').attr('value', entry).text(entry));
            })
        });
    },
    addOne: function(model){
        var view = new app.ActionView({model: model});
        this.$('.list').append(view.render().el);
    },
    addAll: function(){
        this.collection.each(this.addOne, this);
    },
    render: function(){
        this.$('.list').children().remove();
        this.addAll();
    },
    create: function(){
        this.collection.create();
        var that = this;
        var model = that.collection.last();
        var first_model = that.collection.first();
        setTimeout(function(){
            model.set('build_order_id', first_model.get('build_order_id'));
            model.save();
        }, 1000);
    },
    fetch_actions: function(build_order_id) {
        var view = this;
        var e = this.$('.dropdown').get()[0];
        var build_order_name = e.options[e.selectedIndex].text;
        this.collection = new app.ColAction(null, {build_order: build_order_name});
        this.listenTo(this.collection, 'add', this.addOne);
        this.listenTo(this.collection, 'remove', this.render);
        this.listenTo(this.collection, 'reset', this.addAll);
        this.collection.fetch({
            // reset: true, 
            success: function(collection){
                if(!collection.length){
                    collection.create();
                    let model = collection.first();
                    model.set('build_order_id', build_order_id);
                    model.save();
                }
                view.render();
            },
            error: function(){
                view.render();
            },
        });
    },
    launch: function() {

            var output = this.$('#output').get()[0];
            var xhr = new XMLHttpRequest();
            var e = this.$('.dropdown').get()[0];
            var name = e.options[e.selectedIndex].text;
            xhr.open('GET', '/stream_run?name=' + name);
            xhr.send();
            var temp_msg = '';
            function getDifference(a, b)
            {
                var i = 0;
                var j = 0;
                var result = "";

                while (j < b.length)
                {
                if (a[i] != b[j] || i == a.length)
                    result += b[j];
                else
                    i++;
                j++;
                }
                return result;
            }
            let that = this;
            (function(temp_msg){
                setInterval(function(){
                    // output.textContent = xhr.responseText;
                    if(temp_msg.trim() !== xhr.responseText.trim()){
                        var msg_to_speak = getDifference(temp_msg.trim(), xhr.responseText.trim());
                        msg_to_speak = msg_to_speak.replace(/\d{1}:\d{2}:\d{2} : /g, '')
                        var msg = new SpeechSynthesisUtterance(msg_to_speak);
                        var voices = window.speechSynthesis.getVoices();
                        msg.voice = voices.filter(function(voice) { return voice.name == that.voice_name; })[0];
                        window.speechSynthesis.speak(msg);
                        output.textContent = xhr.responseText;
                        window.scrollTo(0,document.body.scrollHeight);
                    }
                    temp_msg = output.textContent || '';
                }, 1000);
            })(temp_msg);
    },
    testAudio: function() {
        var msg = new SpeechSynthesisUtterance("Test audio");
        var voices = window.speechSynthesis.getVoices();
        let that = this;
        msg.voice = voices.filter(function(voice) { return voice.name == that.voice_name; })[0];
        window.speechSynthesis.speak(msg);
    },
    toogleVoice: function() {
        if(this.english_voice === true){
            this.voice_name = 'Google US English';
        } else {
            this.voice_name = 'Google français';
        }
        alert(this.voice_name);
        this.english_voice = !this.english_voice;
    }
});
