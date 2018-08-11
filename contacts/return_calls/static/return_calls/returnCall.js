
ReturnCall = function (url) {

    var $container = $('[data-role=return-call]'),
        ASAP = '1';

    function refreshTimeFields() {
        $container.find('input[name=answer_time]:checked').trigger('change');
    }

    function loadForm() {

        $.get(url, function(response) {

            $container.html(response);

            $container.on('change', '[name=answer_time]', function (event) {

                var action = $(this).val() === ASAP ? 'hide' : 'show';

                $container.find('[data-role=time-fields]')[action]();

            });

            refreshTimeFields();

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
                        refreshTimeFields();
                    }
                });
            });
        });
    }

    loadForm();

};
