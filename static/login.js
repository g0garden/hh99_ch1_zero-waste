$(document).ready(function () {

})

function sign_in() {
    let id = $('#login-id').val()
    let pw = $('#login-pw').val()

    if (id == '') {
        alert('아이디를 입력하세요')
        return;
    } else if (pw == '') {
        alert('비밀번호를 입력하세요')
        return;
    }
    $.ajax({
        type: 'POST',
        url: '/sign_in',
        data: {
            id_give: id,
            pw_give: pw
        },
        success: function (response) {
            if (response['result'] == 'success') {
                $.cookie('mytoken', response['token'], {path: '/'});
                window.location.replace("/")
            } else {
                alert(response['msg'])
            }
        }
    })

}