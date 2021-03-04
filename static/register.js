$(document).ready(function () {

})

function join_blank_check() {
    let name = $('#register-name').val()
    let id = $('#register-id').val()
    let pw = $('#register-pw').val()


    if (name == '') {
        alert('이름을 입력하세요')
        return;
    } else if (id == '') {
        alert('아이디를 입력하세요')
        return;
    } else if (pw == '') {
        alert('비밀번호를 입력하세요')
        return;
    }
    if (!$("#help-id").hasClass("is-checked")) {
        alert("아이디 중복확인을 해주세요.")
        return;
    }
    if (checkPassword(pw) == false) {
        return;
    }
    alert('가입을 환영합니다. ' + name + '님')
    register()
    window.location.href = "/login"
}

function overlap_check() {
    let id = $('#register-id').val()
    if (id == '') {
        alert('아이디를 입력하세요')
        return;
    }
    $.ajax({
        type: 'POST',
        url: '/register/overlap_check',
        data: {
            'id_give': id
        },
        success: function (response) {

            if (response["exists"]) {
                alert('이미 존재 하는 아이디 입니다.')
            } else {
                $('#help-id').addClass('is-checked')
                alert('사용가능한 아이디 입니다.')
            }
        }
    })
}

function checkPassword(pw) {
    if (!/^[a-zA-Z0-9]{7,20}$/.test(pw)) {
        alert('비밀번호 오류!! 숫자와 영문자 조합으로 8~20자리를 사용해야 합니다.');
        return false;
    }
    var checkNumber = pw.search(/[0-9]/g);
    var checkEnglish = pw.search(/[a-z]/ig);

    if (checkNumber < 0 || checkEnglish < 0) {
        alert("비밀번호 오류!! 숫자와 영문자를 혼용하여야 합니다.");
        return false;
    }

    if (/(\w)\1\1\1/.test(pw)) {
        alert('비밀번호 오류!! 444같은 문자를 4번 이상 사용하실 수 없습니다.');
        return false;
    }
    return true;
}

function register() {
    let name = $('#register-name').val()
    let id = $('#register-id').val()
    let pw = $('#register-pw').val()

    $.ajax({
        type: 'POST',
        url: '/register/save',
        data: {
            id_give: id,
            pw_give: pw,
            name_give: name,
            intro_give: '',
        },
        success: function (response) {
            if (response['result'] == 'success') {
                window.location.href = '/login'
            } else {
            }
        }
    })
}
