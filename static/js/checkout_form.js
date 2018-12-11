$(function() {
    $(".popup").parent().parent().hide();

    // If the driver says yes to any of the checks, unhide the input
    $("input").click(function () {
        let name = $(this).attr("name").split("_");
        name = "div_id_" + name.slice(0, 2).join("_");

        let input =  name + "_input";
        input = $("div#" + input)

        let upload = name + "_upload";
        upload = $("div#" + upload)

        if ($(this).val() === "Y"){

            // Hide the input
            if (input.length > 0) {
                input.show();
            }

            // if it does, hide it.
            if (upload.length > 0) {
                upload.show();
            }

        } else {
            // Hide the input
            if (input.length > 0) {
                input.hide();
            }

            // if it does, hide it.
            if (upload.length > 0) {
                upload.hide();
            }
        }
    })
})
