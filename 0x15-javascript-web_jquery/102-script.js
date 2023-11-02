$('document').ready(function () {
  const languageCode = $('INPUT#language_code').val();
  $('INPUT#btn_translate').click(function () {
    $.get('https://www.fourtonfish.com/hellosalut/hello/', { lang: languageCode }, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
