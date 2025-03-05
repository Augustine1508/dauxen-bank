$(document).ready(function (){

    $('#login-form').on('submit', function(e){
        e.preventDefault()
        const $form = $(this);
        const $loginbtn = $('#btn-login');
        const $spinner = $('.spinner-border');
        const $text = $('#login-text');
        

        
    
        $text.text('Loading')
        $spinner.show()
        $loginbtn.prop('disabled', true).css({
            'background-color': '#808080',
            'cursor': 'not-allowed'
        });
    
        const csrftoken = $('input[name="csrfmiddlewaretoken"]').val();
    
        $.ajax({
            type: 'POST',
            url:'/login',
            data: $form.serialize(),
            dataType: 'json',
            headers:{
                'X-CSRFTOKEN': csrftoken
            },
    
            success: function(res){
                console.log(res);
    
                iziToast.success({
                    title: 'success',
                    message: res.success,
                    position: 'topCenter'
                });

                
                $text.text('Logging you in  ')
    
                setTimeout(function() {
                    console.log('Redirecting to /profile');
                    window.location.href = '/profile';
                    
                }, 2000);
             
    
    
            },
    
    
            error: function(res){
                console.log(csrftoken)
    
    
                iziToast.error({
                    title: 'Error',
                    message: res.responseJSON.error,
                    position: 'topCenter'
                });
    
                $spinner.hide();
                $loginbtn.prop('disabled', false).css({
                    'background-color': '',
                    'cursor': ''
                });
                $text.text('Login')
    
                
            }
        
        })
    
    
    })
    
    
    
    })