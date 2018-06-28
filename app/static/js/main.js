
// When you click on a
$('table.table.is-model-list').on('click', 'tr', function() {
    let current_url = window.location.href;
    let model_id = $(this).find("td:first")[0].textContent
    window.location = current_url + '/edit/' + model_id;
});