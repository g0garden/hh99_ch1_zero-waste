$(document).ready(function () {
    tab_show();
    name = $('.myname_name').text()
    // alert(name)

    if ($('.card').hasClass('true')) {
        $('#placeholder_img').hide();
    }else {
        $('#placeholder_img').show();
    }
})

function tab_show() {
    $('.see-all').on('click', function () {
        $('.see-all').addClass('active')
        $('.see-search').removeClass('active')
        window.location.reload()

        $('.see-all-area').show()
        $('.see-search-area').hide()
    })
    $('.see-search').on('click', function () {
        $('.see-all').removeClass('active')
        $('.see-search').addClass('active')

        $('.see-search-area').show()
        $('.see-all-area').hide()
    })
}

function textarea_edit_post(id) {
    textarea_show_hide(id);
    let contents = $(`#${id}-contents`).text().trim();
    console.log(contents)
    $(`#${id}-edit`).val(contents.trim())
}

function textarea_show_hide(id) {
    if ($(`#${id}-edit`).css('display') == 'none') {
        $(`#${id}-edit`).show()
        // alert(id)
        $(`#${id}-icon`).addClass('active')
        $(`#${id}-icon`).removeClass('deactive')
        $(`#${id}-save-btn`).addClass('active')
    } else if ($(`#${id}-edit`).css('display') == 'block') {
        $(`#${id}-edit`).hide()
        $(`#${id}-icon`).removeClass('active')
        $(`#${id}-icon`).addClass('deactive')
        $(`#${id}-save-btn`).removeClass('active')
    }
}

function toggle_marking(article_id, type) {
    console.log(article_id, type)
    let $a_like = $(`#${article_id} a[aria-label='${type}']`)
    let $i_like = $a_like.find("i")
    if ($i_like.hasClass("fas")) {
        $.ajax({
            type: 'POST',
            url: '/update_marking',
            data: {
                'article_id_give': article_id,
                'type_give': type,
                'action_give': "unmarking"
            },
            success: function (response) {
                console.log("unmarking")
                $i_like.addClass("far").removeClass('fas')
            }
        })
    } else {
        $.ajax({
            type: 'POST',
            url: '/update_marking',
            data: {
                'article_id_give': article_id,
                'type_give': type,
                'action_give': "marking",
                'memo_give': ""
            },
            success: function (response) {
                console.log("marking")
                $i_like.addClass("fas").removeClass('far')
            }
        })
    }
}

function edit_memo(article_id) {
    $()
    let memo = $(`#${article_id}-edit`).val().trim()
    // alert(memo)
    if (memo == '') {
        alert('메모를 적어주세요!')
        return;
    }
    $.ajax({
        type: 'POST',
        url: '/memo_edit',
        data: {memo_give: memo, id_give: article_id},
        success: function (response) {
            alert('메모 수정 완료!')
            window.location.reload()
        }
    })
}