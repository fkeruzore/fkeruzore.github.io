// Abstract toggle functionality for publications
$(document).ready(function() {
  $('.abstract-toggle').click(function(e) {
    e.preventDefault();

    var targetId = $(this).data('target');
    var $abstractDiv = $('#' + targetId);

    // Toggle the abstract visibility with slide animation
    $abstractDiv.slideToggle(300);

    // Update link text
    var currentText = $(this).text();
    $(this).text(currentText === 'Abstract' ? 'Hide Abstract' : 'Abstract');
  });
});
