$(".js-create-book").click(function(e){
    var addressValue = $(this).attr("href");
        e.preventDefault();
       $.ajax({
      url: addressValue,
      type: 'get',
      success: function(data) {
        var jq=jQuery(data);
        var title = jq.find(".modal-title");
        var description = jq.find(".modal-body");
        $(document).find('.modal-title').replaceWith(title);
        $(document).find('.modal-body').replaceWith(description); 
        $(document).find("#exampleModal").css('padding-right' , 0);
    }
    });
  });
  var x = 100;
 var width = 500;
 console.log($(window).height());
 $(".change").on('wheel', function(e) {
     
  if (e.originalEvent.deltaY < 0) {
    e.preventDefault();
    width= width + x;
    if (width >= $(window).height()){
     $('.img-modal').css('overflow', 'scroll');
    }
  } else {
    e.preventDefault();
     width= width - x;
     if (width < $(window).height()) {
      $('.img-modal').css('overflow', 'hidden');
      $('html, body').animate({scrollTop: '0px'}, 500);
    }
  }
  $('.change').css('height', width);
});
   $('body').on('click', '.image', function(){
    var src= $(this).attr('src');
    $('.change').attr('src', src);
    $('.img-modal').toggleClass('showing');
    $('body').toggleClass('scrollbar');
});
$('.demo').click(function(e){
  var answer = confirm('Are you sure to delete this??');
  if(answer == true){
    $('demo').hide();
  }
  else{
    e.preventDefault();
  }
});
$(document).ready(function(){
  $("#image_upload").click(function(){
    $('#image_update').remove();
  });
});

$(document).ready(function(){
  $('#image_form').submit(function(e){
    function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

 //e.preventDefault();
     var formData= new FormData($('#image_form')[0]);
// var file_data = $('#image').prop('files')[0];
// var formData = new FormData($('#image_form')[0]);
//   formData.append('file', file_data);
    $.ajax({
      
      xhr:function(){
        
        var xhr= new window.XMLHttpRequest();
        xhr.upload.addEventListener('progress', function(e){
          
          if( e.lengthComputable){
            
            // console.log('Bytes Loaded ' + e.loaded);
            // console.log('Total size ' + e.total);
            // console.log('Percentage  Uploaded ' + (e.loaded / e.total)*100 + '%');
            var percent = Math.round((e.loaded / e.total)*100);
            $('.progress-bar').attr('aria-valuenow', percent).css('width', percent + '%').text(percent + '%');
          }
        });
        return xhr;
      },
      //Ajax call for creating post
      
      type:'POST',
      processData: false,
      contentType: false,
      data:formData,
      success:function(){
      
      }
      
    });
    
  });
  
});

$(document).on('click', '.omb_authTitle .signup', function(e){
    // e.preventDefault();
    $('#login_form').css('display', 'none');
   $('#register_form').css('display', 'block');
   if ( $('.signup').is( "a" ) ) {
                $('.signup').contents().unwrap();
                $('.log-in').wrap( "<a href='#' class='login'></a>" );
              } else {
                  $('.signup').wrap( "<a></a>" );
              }

});
$(document).on('click', '.omb_authTitle .login', function(e){
     $('#login_form').css('display', 'block');
   $('#register_form').css('display', 'none');
   if ( $('.login').is( "a" ) ) {
                $('.login').contents().unwrap();
                $('.sign-up').wrap( "<a href='#' class='signup'></a>" );
              } 
});

$('.UserLoginForm').submit(function(e){
    alert('I got somewhere!');
    
    
});

// $(document).ready(function(e){
//     $('.nav-link').click();
    
// });