  $('#imageModal').on('show.bs.modal', function (event) {
    let button = $(event.relatedTarget);
    let imageUrl = button.attr('src');
    let modal = $(this);
    modal.find('#modalImage').attr('src', imageUrl);
  });



