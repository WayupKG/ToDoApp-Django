// Набор функций
var base = {
    // Поиск элементов по классу
    findClass: function(str, node) {
         if(document.getElementsByClassName) return (node || document).getElementsByClassName(str);
         else {
              var node = node || document, list = node.getElementsByTagName('*'), length = list.length, Class = str.split(/\s+/), classes = Class.length, array = [], i, j, key;
              for(i = 0; i < length; i++) {
                    key = true;
                    for(j = 0; j < classes; j++) if(list[i].className.search('\\b' + Class[j] + '\\b') == -1) key = false;
                    if(key) array.push(list[i]);
              }
              return array;
         }
    },
    // Добавление обработчиков событий
    bind: function(node, type, listener) {
        if(node.addEventListener) node.addEventListener(type, listener, false);
        //@cc_on node.attachEvent('on' + type, function() { listener.call(node); });
    },
    // Реализация DOMContentLoaded
    init: [],
    ready: function() {
        if(!arguments.callee.done) {
            arguments.callee.done = true;
            if(this.timer) clearInterval(this.timer);
            var i, length = this.init.length;
            for(i = 0; i < length; i++) this.init[i]();
            this.init = [];
        }
    },
    check: function() {
        var _this = this, listener = function() {
            _this.ready();
        };
        if(document.addEventListener) document.addEventListener('DOMContentLoaded', listener, false);
        if(/KHTML|WebKit/i.test(navigator.userAgent)) this.timer = setInterval(function() {
            if(/loaded|complete/.test(document.readyState)) base.ready();
        }, 10);
        /*@cc_on document.write(unescape('%3CSCRIPT onreadystatechange="if(this.readyState==\'complete\') base.ready()" defer=defer src=\/\/:%3E%3C/SCRIPT%3E')); @*/
        this.bind(window, 'load', listener);
    }
};

// Функции для работы с панельками
var toggler = {
    process: function() {
        var i, list = base.findClass('toggler'), length = list.length;
        for(i = 0; i < length; i++) base.bind(list[i], 'click', this.toggle);
        list = base.findClass('content');
        length = list.length;
        for(i = 0; i < length; i++) list[i].style.display = 'none';
    },
    toggle: function() {
        var content = base.findClass('content', this.parentNode)[0], e = arguments[0] || window.event;
        if(content.style.display == 'block') {
            content.style.display = 'none';
        }
        else {
            content.style.display = 'block';
        }
        e.preventDefault ? e.preventDefault() : e.returnValue = false;
    }
};

// Ищем блоки с классом «toggle» по событию DOMContentLoaded
base.init.push(function() {
    toggler.process();
});

// Запускаем проверку готовности DOM
base.check();
