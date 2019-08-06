$('document').ready(function () {
    $('.gallery-other-item').click(function () {
        $('.gallery-other-item').removeClass('active')
        $(this).addClass('active')
        var src = $(this).attr('data-src')
        var page = $(this).attr('data-page')
        $('#page').val(page)
        $('#gallery-main-picture').css('background-image', "url('"+ src +"')")
    })
    $('#gallery-prev-button').click(function () {
        var page = parseInt($('#page').val())
        if (page > 1) {
            $('.gallery-other-item[data-page='+(page-1)+']').click()
        }
    })
    $('#gallery-next-button').click(function () {
        var page = parseInt($('#page').val())
        var length = $('.gallery-other-item').length
        if (page < length) {
            $('.gallery-other-item[data-page='+(page+1)+']').click()
        }
    })
})