var basic = $('#main-cropper').croppie({
    viewport: { width: 340, height: 340 },
    boundary: { width: 360, height: 380 },
    showZoomer: false,
    url: 'http://lorempixel.com/500/400/'
});

function readFile(input) {
  if (input.files && input.files[0]) {
    var reader = new FileReader();

    reader.onload = function (e) {
      $('#main-cropper').croppie('bind', {
        url: e.target.result
      });
      $('.actionDone').toggle();
      $('.actionUpload').toggle();
    }

    reader.readAsDataURL(input.files[0]);
  }
}

$('.actionUpload input').on('change', function () { readFile(this); });
$('.actionDone').on('click', function(){
  $('.actionDone').toggle();
  $('.actionUpload').toggle();
})
