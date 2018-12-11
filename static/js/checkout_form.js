$(function() {
    $(".popup").parent().parent().hide();

    // If the driver says yes to any of the checks, unhide the input
    $("input[type=radio]").click(function () {
        let name = $(this).attr("name").split("_");
        name = "div_id_" + name.slice(0, name.length - 1).join("_");

        let input =  name + "_input";
        input = $("div#" + input)

        let upload = name + "_upload";
        upload = $("div#" + upload)

        if ($(this).val() === "Y"){

            // Hide the input
            if (input.length > 0) {
                input.show();
                input.find("textarea").attr("required", "")
                input.find("input").attr("required", "")
            }

            // if it does, hide it.
            if (upload.length > 0) {
                upload.show();
                upload.find("input").attr("required", "")
            }

        } else {
            // Hide the input
            if (input.length > 0) {
                input.hide();
                input.find("textarea").removeAttr("required")
                input.find("input").removeAttr("required")
            }

            // if it does, hide it.
            if (upload.length > 0) {
                upload.hide();
                upload.find("input").removeAttr("required")
            }
        }
    })
})
