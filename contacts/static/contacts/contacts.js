(function ( $ ) {

    $.fn.contactMessageModal = function(options) {

        $(this).click(function () {

            $.get(options.url, function (response) {

                var $modal = $(response).modal();

                $modal.on('submit', 'form', function (event) {
                    event.preventDefault();

                    $.ajax({
                        method: 'POST',
                        url: options.url,
                        data: $modal.find('form').serialize(),
                        success: function (response) {
                            $modal.modal('hide');
                            if ($.notify) {
                                $.notify({message: response}, {type: 'success'});
                            }
                        },
                        error: function (response) {
                            $modal.find('form').replaceWith(response.responseText);
                        }
                    });
                });

                $modal.on('click', '[data-role="submit-form-btn"]', function () {
                    $modal.find('form').submit();
                });

                $modal.on('hidden.bs.modal', function () {
                    $modal.remove();
                });
            })

        });

        return this;

    };

}(jQuery));