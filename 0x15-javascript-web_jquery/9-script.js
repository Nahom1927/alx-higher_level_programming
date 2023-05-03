const $ = window.$;
const url = 'https://fourtonfish.com/hellosalut/?lang=fr';

$(document).ready(function () {
  $.getJSON(url, function (resp) {
    const hello = resp.hello;
    $('#hello').text(hello);
  });
});
