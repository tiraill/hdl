let all_params, old_location, filters, searchReq, searchName;

function getAllUrlParams(){
    let options = window.location.search.slice(1)
          .split('&')
          .reduce(function _reduce (/*Object*/ a, /*String*/ b) {
            b = b.split('=');
            a[b[0]] = decodeURIComponent(b[1]);
            return a;
          }, {});
    return options
}

function useFilters(all_params, old_location) {
    let new_location, object_length;

    new_location = Array();

    object_length = Object.keys(all_params).length;
    if (object_length !== 0)
        new_location.push(old_location + "?");
    else {
        new_location.push(old_location);
    }

    for (const [index, [key, value]] of Object.entries(Object.entries(all_params))) {
        if (key !== "") {
            if (object_length === parseInt(index) + 1) {
                new_location.push(key + "=" + value);
            } else {
                new_location.push(key + "=" + value + "&");
            }
        }}

    window.location.href = new_location.join('');
}


all_params = getAllUrlParams();
old_location = window.location.href.slice(0, window.location.href.indexOf('?'));

filters = document.getElementsByClassName('filters__item');
searchReq = document.getElementById('catalog-search-input');

Array.from(filters).forEach(function(element){
    let closest_input = $(element).children(":first");
    let elementName = closest_input.attr("name");
    let elementSlug = closest_input.data("slug");

    if (elementName in all_params && elementSlug === all_params[elementName]) {
        closest_input.prop("checked", true)
    }

})

searchName = $(searchReq).attr("name");

if (searchName in all_params) {
    $(searchReq).val(all_params[searchName])
}

$('#catalog-search-input').keypress(function(event){
    let keycode = (event.keyCode ? event.keyCode : event.which);
    if (keycode === 13){
        event.preventDefault();
        all_params['search'] = $(searchReq).val()
        useFilters(all_params, old_location);
    }
})

$('#catalog__search__symbol').click(function (event) {
    event.preventDefault();
    all_params['search'] = $(searchReq).val();
    useFilters(all_params, old_location);
})


$('.filters__item').click(function(event){
    event.preventDefault();
    let closest_input, elementName, elementSlug;

    closest_input = $(this).children(":first");
    if (closest_input.is(":checked")) {
        closest_input.prop("checked", false)
        elementName = closest_input.attr("name");
        delete all_params[elementName];
    } else {
        closest_input.prop("checked", true)
        elementName = closest_input.attr("name");
        elementSlug = closest_input.data("slug");
        all_params[elementName] = elementSlug;
    }

    useFilters(all_params, old_location);
})