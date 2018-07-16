
// When you click on a table cell, open the detail view for that model.
$("table.table.is-model-list").on("click", "tr", function() {
    let current_url = window.location.href;
    let model_id = $(this).find("td:first")[0].textContent
    window.location = current_url + "/" + model_id;
});


// Delete buttons should trigger the delete modal
$("button#model-delete-button").on("click", function() {
    $("div.modal#delete-modal").addClass("is-active")
})

// Modal close buttons should close the modal
$("button.modal-close").on("click", function() {
    $("div.modal#delete-modal").removeClass("is-active")
})

// Modal cancel buttons should also close the modal
$("button.modal-cancel").on("click", function() {
    $("div.modal#delete-modal").removeClass("is-active")
})