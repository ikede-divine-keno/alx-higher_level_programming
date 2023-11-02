// Using jQuery's Ajax convenience methods

// Get plain text or HTML
$(document).ready(function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (resp) {
    $('DIV#hello').text(resp.hello);
  });
});
