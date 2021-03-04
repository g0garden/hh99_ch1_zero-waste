$(document).ready(function () {

})


function update_profile() {
    let name = $('#input-name').val()
    let intro = $('#textarea-about').val().trim()

    if(name==''){
        alert('수정하실 이름을 적어주세요!')
        return;
    }else if (intro==''){
        alert('수정하실 자기소개를 적어주세요!')
        return;
    }
    // alert(name, intro)
    $.ajax({
        type: "POST",
        url: "/update_profile",
        data: {
            name_give: name,
            intro_give: intro
        },
        success: function (response) {
            if (response["result"] == "success") {
                alert('프로필 수정 완료!')
                window.location.reload()

            }
        }
    });
}


function sign_out() {
    $.removeCookie('mytoken', {path: '/'});
    alert('로그아웃!')
    window.location.href = "/login"
}