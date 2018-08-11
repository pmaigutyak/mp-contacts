
Feedback = function (url) {
    var $container = $('[data-role=feedback]');

    function loadForm() {

        $.get(url, function(response) {
            $container.html(response);

            $container.on('submit', 'form', function (event) {
                event.preventDefault();

                $.ajax({
                    method: 'POST',
                    url: url,
                    data: $container.find('form').serialize(),
                    success: function (response) {
                        if ($.notify) {
                            $.notify({message: response}, {type: 'success'});
                        }
                        loadForm();
                    },
                    error: function (response) {
                        $container.find('form').replaceWith(response.responseText);
                    }
                });
            });
        });
    }

    loadForm();
};
