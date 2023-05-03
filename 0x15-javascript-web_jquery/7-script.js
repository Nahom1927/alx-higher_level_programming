const $ = window.$;
const url = 'https://swapi.co/api/people/5/?format=json';

$.getJSON(url, function (resp) {
  const name = resp.name;
  $('#character').text(name);
});
