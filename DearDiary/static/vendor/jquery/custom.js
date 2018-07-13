
$(window).on('load', function() {
            $('#loading').fadeOut(1000);
            
        });
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
//  console.log($(window).height());
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
  

   $('body').on('click', '.clear', function(e){
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
            
            console.log('Bytes Loaded ' + e.loaded);
            console.log('Total size ' + e.total);
            console.log('Percentage  Uploaded ' + (e.loaded / e.total)*100 + '%');
            var percent = Math.round((e.loaded / e.total)*100);
            $('.progress-bar').attr('aria-valuenow', percent).css('width', percent + '%').text(percent + '%');
          }
        });
        return xhr;
      },
      type:'POST',
      url:'/create',
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
   
//Ajax
$.ajax
       
       ({
           url:'/register',
           success:function(data)
           {
               var jq=jQuery(data);
               var title = jq.find(".omb_loginForm"); 
               $(document).find('.omb_loginForm').replaceWith(title);
                if ( $('.signup').is( "a" ) ) {
                $('.signup').contents().unwrap();
                $('.log-in').wrap( "<a href='#' class='login'></a>" );
              } else {
                  $('.signup').wrap( "<a></a>" );
              }
                        
               
           } //Success function ends.
           
       }); //Ajax ends.
       
    
});


$(document).on('click', '.omb_authTitle .login', function(e){
    //alert('log-in');
    e.preventDefault();
    
 //Ajax
$.ajax
       
       ({
           url:'/login',
           success:function(data)
           {
               var jq=jQuery(data);
               var title = jq.find(".omb_loginForm"); 
               $(document).find('.omb_loginForm').replaceWith(title);
                if ( $('.login').is( "a" ) ) {
                $('.login').contents().unwrap();
                $('.sign-up').wrap( "<a href='#' class='signup'></a>" );
              } else {
                  //$('.login').wrap( "<a></a>" );
              }
               
           } //Success function ends.
           
       }); //Ajax ends.
    
});


$(document).ready(function(e){
    $('.nav-lsink').click();
    
});

$("#checkAll").click(function () {
    $('.checkbox').prop('checked', $(this).prop('checked')); 
    
    if($('#checkAll').prop('checked') == true)
    {
          $('.deleteBtn').fadeIn();
    }
    else
    {
          $('.deleteBtn').fadeOut();
    }
    
  
 });
 
 $('.checkbox').click(function(e) {
     if (!$('.checkbox').is(':checked') == false)
    {
        $('#checkAll').prop('checked', false);
         $('.deleteBtn').fadeIn();
    }
    else {
        
        //  $('#checkAll').prop('checked', false);
         $('.deleteBtn').fadeOut();
    } 
    
//     $(".checkbox").each(function(){
//     if (!$(this).prop('checked')==true){ 
//         $('#checkAll').prop('checked', false);
//     }
// });
 });
 
//  $('.deleteBtn').click(function(e){
//  var answer = confirm('Are you sure to delete this??');
//   if(answer == true){
//     $('demo').hide();
//   }
//   else{
//     e.preventDefault();
//   }
//  });

$(document).on('click','.replace',function(e){
    
   x= $(this).attr("src");
$('.inline-flex').find('img').map(function() { return this.src; }).get();
    y = $(".change").attr("src", x);
    
     var t = ('https://2b5cbf3294174e5cb85c8cda01fcd0b6.vfs.cloud9.us-east-2.amazonaws.com' + $(this).attr('src'));
     
     
     setTimeout(function() {
         
 var images = $('.inline-flex').find('.replace').map(function() { return this.src; }).get();
 
 for (var p =0; p<=images.length; p++){
     var i = jQuery.inArray(t, images);
     }
 $('.next').click(function(e){
       if(i<=images.length-2){
    i=i+1;
     $(".change").attr("src", images[i]);
    
     }
     
     else if (i>images.length-2 ){
         i = 0;
          y = $(".change").attr("src", images[i]);
     }
     
     else{
         console.log('Image not found in aray!');
     }
    });
    
    
     $('.previous').click(function(e){
    if(i<=images.length-1 && i>0){
    i=i-1;
     $(".change").attr("src", images[i]);
     }
     
     else if (i<=0){
         i = images.length-1;
          y = $(".change").attr("src", images[i]);
     }
     
     else{
         console.log('Image not foind in aray!');
     }
    });

    }, 607);
    
});

    
   $(document).on('click','.image', function(e){
    var src= $(this).attr('src');
    $('.change').attr('src', src);
    $('.img-modal').toggleClass('showing');
    $('body').toggleClass('scrollbar');
    var addressValue = $(this).closest('.strip').find('.col-md-8').find('a').attr('href');
         $.ajax({
      url: addressValue,
      type: 'get',
      success: function(data) {
        var jq=jQuery(data);
        var title = jq.find(".col-md-2");
        $(document).find('.inline-flex').html(title);
    }
    });
   
     var t = ('https://2b5cbf3294174e5cb85c8cda01fcd0b6.vfs.cloud9.us-east-2.amazonaws.com' + $(this).attr('src'));
     
     
     setTimeout(function() {
         
 var images = $('.inline-flex').find('.replace').map(function() { return this.src; }).get();
 
 for (var p =0; p<=images.length; p++){
     var i = jQuery.inArray(t, images);
     }
 $('.next').click(function(e){
       if(i<=images.length-2){
    i=i+1;
     $(".change").attr("src", images[i]);
    
     }
     
     else if (i>images.length-2 ){
         i = 0;
          y = $(".change").attr("src", images[i]);
     }
     
     else{
         console.log('Image not found in aray!');
     }
    });
    
    
     $('.previous').click(function(e){
    if(i<=images.length-1 && i>0){
    i=i-1;
     $(".change").attr("src", images[i]);
     }
     
     else if (i<=0){
         i = images.length-1;
          y = $(".change").attr("src", images[i]);
     }
     
     else{
         console.log('Image not foind in aray!');
     }
    });

    }, 607);
    
   });    


