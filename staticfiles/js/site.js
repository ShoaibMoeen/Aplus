function searchTextChanged() {
    let value = $('#search-course').val();
    if (value && value != undefined && value != '') {
        $('.search-box > .placeholder').css('display', 'none');
    } else {
        $('.search-box > .placeholder').css('display', 'block');
    }
}