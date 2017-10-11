var submit = false;

function form_submit(obj, url) {

    if (submit) {
        return true;
    }

    var lnk_val = $.trim($('#multiurl').val());
    if (lnk_val == '') {
        dialog_tips('请填写要缩短的网址！');
        $('#multiurl').focus();
        return false;
    }

    $(obj).html('正在生成...');

    submit = true;
    $.ajax({
        type: 'POST',
        url: '/',
        data:  JSON.stringify({'url': lnk_val}),
        success: function(data) {
            if (data.status == '-1') {
                dialog_tips(data.err_msg);
            } else {
                if (data.msg) {
                    dialog_tips(data.msg);
                }
                $('#multiurl').val(data.list);
            }
            submit = false;
            $(obj).html('批量缩短网址');
        },
        contentType: "application/json",
        dataType: 'json'
    });

    // $.post(url, JSON.stringify({'url': lnk_val}), function (data) {
    //     alert(data.url);
    //     if (data.status == '-1') {
    //         dialog_tips(data.err_msg);
    //     } else {
    //         if (data.msg) {
    //             dialog_tips(data.msg);
    //         }

    //         $('#multiurl').val(data.list);
    //     }
    //     submit = false;
    //     $(obj).html('批量缩短网址');
    // }, 'json');

}

function dialog_tips(text) {

    var tobj = document.getElementById('dialog_tips'), tip_box = document.getElementById('dialog_tip_box');

    if (!tobj) {

        tobj = document.createElement('div');

        tobj.id = 'dialog_tips';

        tobj.setAttribute('style', ' text-align:center; position:fixed; z-index:999; top:30%; left:10%; width:80%; ');

        tip_box = document.createElement('span');

        tip_box.id = 'dialog_tip_box';

        tip_box.setAttribute('style', 'background:#000000; padding:10px 15px;-webkit-box-shadow:0 0 10px rgba(153, 153, 153, .5);  -moz-box-shadow:0 0 10px rgba(153, 153, 153, .5);  box-shadow:0 0 10px rgba(153, 153, 153, .5);max-width:100%; display:inline-block;text-align:left;  color: #ffffff;filter: alpha(opacity=90);-moz-opacity: 0.9;  opacity: 0.9;  border-radius: 8px; font-size: 1.875rem;');

        tobj.appendChild(tip_box);

        $('body').append(tobj);
    }

    tip_box.innerHTML = text;

    $(tobj).show();

    setTimeout(function () {

        $(tobj).fadeOut();

    }, 2000);

}