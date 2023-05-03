const $ = window.$;
const url = 'https://swapi.co/api/films/?format=json';

$.getJSON(url, function (resp) {
  for (let i = 0; i < resp.results.length; i++) {
    $('#list_movies').append('<li>' + resp.results[i].title + '</li>');
  }
});
