odoo.define('ctp_private_youtube.fullscreen', function (require) {
    "use strict";
    var FS = require('@website_slides/js/slides_course_fullscreen_player')[Symbol.for("default")];
    FS.include({
        xmlDependencies: (FS.prototype.xmlDependencies || []).concat(
            ["/ctp_private_youtube/static/src/xml/template.xml"]
        ),
    });
});