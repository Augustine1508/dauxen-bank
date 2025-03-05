$(document).ready(function (){

$('#verify-form').on('submit', function(e){
    e.preventDefault()
    const $form = $(this);
    const $btn = $('#btn-verify');
    const $spinner = $('.spinner-border');
    const $btntext = $('#verify-text');
    

    $btntext.text('Verifying')
    $spinner.show()
    $btn.prop('disabled', true).css({
        'background-color': '#808080',
        'cursor': 'not-allowed'
    });

    const csrftoken = $('input[name="csrfmiddlewaretoken"]').val();

    $.ajax({
        type: 'POST',
        url:'/email_verify',
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


            setTimeout(function() {
                console.log('Redirecting to /email_verify');
                window.location.href = '/email_verify';
            }, 2000);
         


        },


        error: function(res){
            console.log(csrftoken)


            iziToast.error({
                title: 'Error',
                message: res.responseJSON.error,
                position: 'topCenter'
            });

            $form[0].reset();
            $spinner.hide();
            $btn.prop('disabled', false).css({
                'background-color': '',
                'cursor': ''
            });
            $btntext.text('Verify Now')

            
        }
    
    })


})



})