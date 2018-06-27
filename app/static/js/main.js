
// When you click on a
$('table.table').on('click', 'tr', function() {
    let current_url = window.location.href;
    let model_id = $(this).find("td:first")[0].textContent
    window.location = current_url + '/' + model_id;
});