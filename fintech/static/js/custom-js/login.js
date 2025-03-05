$(document).ready(function (){

    $('#login-form').on('submit', function(e){
        e.preventDefault()
        const $form = $(this);
        const $loginbtn = $('#btn-login');
        const $spinner = $('.spinner-border');
        const $text = $('#login-text');
        
    
        // $text.text('Please Wait');
        // $spinner.show();
        // $loginbtn.prop('disabled', true).css({
        //     'background-color': '#808080',
        //     'cursor': 'not-allowed'
        // });
    

        const $form = $(this)
        const csrftoken = $('input[name="csrfmiddlewaretoken"]').val();
    
        $.ajax({
            type: 'POST',
            url:'/login',
            data: $form.serialize(),
            dataType: 'json',
            headers:{
                'X-CSRFToken': csrftoken
            },
    
            success: function(res){
                console.log(res);
    
                iziToast.success({
                    title: 'success',
                    message: res.success,
                    position: 'topCenter'
                });
    
    
                setTimeout(function() {
                    window.location.href = '/profile';
                }, 2000);
             
    
    
            },
    
    
            error: function(res) {
                
                
                
                iziToast.error({
                    title: 'Error',
                    message: res.responseJSON.error,
                    position: 'topCenter'
                });
            


                $form[0].reset();
                $text.text('Login');
                $spinner.hide();
                $loginbtn.prop('disabled', false).css({
                  'background-color': '',
                  'cursor': ''
                });
            }
            
        
        })
    
    
    })
    
    
    
    })