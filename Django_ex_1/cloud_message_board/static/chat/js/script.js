$(document).ready(function() {
    $('form').on('submit', function(event) {
        event.preventDefault(); // Prevent the form from submitting via the browser

        $.ajax({
            url: '', // Current URL
            type: 'post',
            data: $(this).serialize(),
            success: function(data) {
                // Clear the form
                $('form')[0].reset();
            }
        });
    });
});

