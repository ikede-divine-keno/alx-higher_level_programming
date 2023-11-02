// Using jQuery's Ajax convenience methods
// Get plain text or HTML
$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (resp) {
  $.each(resp.results, function (index, item) {
    $('UL#list_movies').append('<li>' + item.title + '</li>');
  });
});
