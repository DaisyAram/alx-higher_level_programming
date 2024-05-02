dy(function () {
        $("#add_item").click(function () {
                $("<li>").text("Item").appendTo("ul.my_list");
        });
        $("#remove_item").click(function () {
                $("ul.my_list li:last-child").remove();
        });
        $("#clear_list").click(function () {
                $("ul.my_list").empty();
        });
});
root@d9978b7d4bb5:/alx-higher_level_programming/0x15-javascript-web_jquery# cat 102-script.js
$(document).ready(function () {
        $("INPUT#btn_translate").click(function () {
                const language_code = $("INPUT#language_code").val();
                $.getJSON(
                        `https://fourtonfish.com/hellosalut/hello/?lang=${language_code}`,
                        function (data) {
                                $("#hello").text(data.hello);
                        }
                );
        });
});
