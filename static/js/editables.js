$ = django.jQuery;
$(function() {
    function csrfSafeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", $("#_csrf").val());
            }
        }
    });

    $(".editable span").click(function(){
        var $this = $(this);
        var apiId = $this.parent().attr("data-id");
        var fieldName = $this.parent().attr("data-field");
        var fieldLabel = $this.parent().attr("data-field-label");
        var fieldType = $this.parent().attr("data-field-type");
        var newValue = $("#_edittext").val();

        $this.hide();
        $this.find("em").remove();

        if(fieldType == "select"){

        } else if(fieldType == "textarea"){
            $('<textarea/>', {
                'text': $this.text(),
                'rows': 5,
                'cols': 60,
                'id': '_edittext'
            }).appendTo($this.parent()).focus();
        } else {
            console.log("no field type assigned")
        }

        $('<button/>', {
            'text': 'Save',
            'id': '_save',
            'class': 'action save'
        }).on('click', function(){

            var _url = '/api/rest/apis/' + apiId + '/';
            var _data = '{"' + fieldName + '": "' + newValue + '" }';
            //console.log(_url);
            //console.log(_data);
            $.ajax({
                url : _url,
                type : 'PATCH',
                data : _data,
                headers : {
                    'Content-Type' : 'application/json'
                },
                success : function(response, textStatus, jqXhr) {
                    //console.log("Successfully Patched!", textStatus);
                    // console.log(response);
                    $this.text(newValue);
                },
                error : function(jqXHR, textStatus, errorThrown) {
                    //console.log("The following error occured: " + textStatus, errorThrown);
                },
                complete : function() {
                    $("#_save").remove();
                    $("#_cancel").remove();
                    $("#_edittext").remove();
                    $this.show();
                    if($this.val()=="") $this.append("<em>Click to add " + fieldLabel + "</em>")
                }
            });

        }).appendTo($this.parent());

        $('<button/>', {
            'text': 'Cancel',
            'id': '_cancel',
            'class': 'action cancel'
        }).on('click', function(){
            $("#_save").remove();
            $("#_edittext").remove();
            $(this).remove();
            $this.show();
            if($this.val()=="") $this.append("<em>Click to add " + fieldLabel + "</em>")
        }).appendTo($this.parent());
    });
});
