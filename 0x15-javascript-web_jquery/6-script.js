const $ = window.$;
$('#update_header').click(function () {
  const htmlString = 'New Header!!!';
  $('header').text(htmlString);
});
