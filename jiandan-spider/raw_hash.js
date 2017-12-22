var f_9p6oITyYH5VB5TtKLVE6aWh86LzKK9FU = function(hash, constant, d) {
    var e = "DECODE";
    var constant = constant ? constant : "";
    var d = d ? d : 0;
    var q = 4;
    constant = md5(constant);
    var o = md5(constant.substr(0, 16));
    var n = md5(constant.substr(16, 16));
    if (q) {
        if (e == "DECODE") {
            var l = hash.substr(0, q)
        }
    } else {
        var l = ""
    }
    var c = o + md5(o + l);
    var k;
    if (e == "DECODE") {
        hash = hash.substr(q);
        k = base64_decode(hash)
    }
    var h = new Array(256);
    for (var g = 0; g < 256; g++) {
        h[g] = g
    }
    var b = new Array();
    for (var g = 0; g < 256; g++) {
        b[g] = c.charCodeAt(g % c.length)
    }
    for (var f = g = 0; g < 256; g++) {
        f = (f + h[g] + b[g]) % 256;
        tmp = h[g];
        h[g] = h[f];
        h[f] = tmp
    }
    var t = "";
    k = k.split("");
    for (var p = f = g = 0; g < k.length; g++) {
        p = (p + 1) % 256;
        f = (f + h[p]) % 256;
        tmp = h[p];
        h[p] = h[f];
        h[f] = tmp;
        t += chr(ord(k[g]) ^ (h[(h[p] + h[f]) % 256]))
    }
    if (e == "DECODE") {
        if ((t.substr(0, 10) == 0 || t.substr(0, 10) - time() > 0) && t.substr(10, 16) == md5(t.substr(26) + n).substr(0, 16)) {
            t = t.substr(26)
        } else {
            t = ""
        }
    }
    return t
};

function jandan_load_img(b) {
    var d = $(b);
    var f = d.next("span.img-hash");
    var e = f.text(); 
    f.remove(); 
    var c = f_9p6oITyYH5VB5TtKLVE6aWh86LzKK9FU(e, "P7mC7lBFx7AhURx8jKs61ENNQUkFexl3");
    var a = $('<a href="' + c.replace(/(\/\/\w+\.sinaimg\.cn\/)(\w+)(\/.+\.(gif|jpg|jpeg))/, "$1large$3") + '" target="_blank" class="view_img_link">[查看原图]</a>');
    d.before(a);
    d.before("<br>");
    d.removeAttr("onload");
    d.attr("src", location.protocol + c.replace(/(\/\/\w+\.sinaimg\.cn\/)(\w+)(\/.+\.gif)/, "$1thumb180$3"));
    if (/\.gif$/.test(c)) {
        d.attr("org_src", location.protocol + c);
        b.onload = function() {
            add_img_loading_mask(this, load_sina_gif)
        }
    }
}