var popupWindow;

function isPopupWindowOpen(){
    if(popupWindow){
        if(popupWindow.closed) return false;
        return true;
    } else
        return false;
}

$( function() {
    $('.jpopup').click(function() {
        if(!isPopupWindowOpen()){
            var href = $(this).attr('data-href');
            popupWindow = window.open(href, 'jpopup', 'height=420, width=550, toolbar=no');
        } else {
            popupWindow.focus();
        }
        return false;
    });
});