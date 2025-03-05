$(document).ready(function () {
    $('#personal-form').on('submit', function (form) {
        form.preventDefault();
        
        const $btntext = $('#btn-text');
        const $spinner = $('.spinner-border');
        const $btnsubmiter = $('#btn-submiter');
        
        $btntext.text('Loading');
        $spinner.show();
        $btnsubmiter.prop('disabled', true).css({
            'background-color': '#808080',
            'cursor': 'not-allowed'
        });
        
        const $entireform = $(this)
        const csrftoken = $('input[name="csrfmiddlewaretoken"]').val();
        
        

        // console.log($entireform)

        $.ajax({
            type:'POST',
            url:'/signup',
            datatype: 'json',
            data: $entireform.serialize(),
            headers:{
                'X-CSRFTOKEN': csrftoken
            },

            success: function(res){
                console.log(res)

                iziToast.success({
                    title: 'success',
                    message: res.success,
                    position: 'topCenter'
                });

             
                window.location = '/email_verify';

            },

            error: function(res){
                // console.log(csrftoken)

                $btntext.text('Register Now');
                $spinner.hide();
                $btnsubmiter.prop('disabled', false).css({
                  'background-color': '',
                  'cursor': ''
                })

                iziToast.error({
                    title: 'Error',
                    message: res.responseJSON.error,
                    position: 'topCenter'
                });

                
            }
        })
        
        

    });
});










// $(document).ready(function () {
//     $('#personal-form').on('submit', function (form) {
//         form.preventDefault();
        
//         const $btntext = $('#btn-text');
//         const $spinner = $('.spinner-border');
//         const $btnsubmiter = $('#btn-submiter');
        
//         $btntext.text('Loading');
//         $spinner.show();
//         $btnsubmiter.prop('disabled', true).css({
//             'background-color': '#808080',
//             'cursor': 'not-allowed'
//         });
        
//         const $entireform = $(this);

//         console.log($entireform);

//         $.ajax({
//             type: 'POST',
//             url: '/signup',
//             dataType: 'json',
//             data: $entireform.serialize(),

//             success: function(res) {
//                 console.log('Success response:', res);

//                 iziToast.success({
//                     title: 'Success',
//                     message: res.success,
//                     position: 'topCenter'
//                 });

//                 // Add a delay to ensure the toast message is shown before redirecting
//                 setTimeout(function() {
//                     console.log('Redirecting to /email_verify');
//                     window.location.href = '/email_verify';
//                 }, 2000); // 2 seconds delay
//             },

//             error: function(res) {
//                 console.log('Error occurred:', res);
//                 $btntext.text('Register Now');
//                 $spinner.hide();
//                 $btnsubmiter.prop('disabled', false).css({
//                     'background-color': '',
//                     'cursor': ''
//                 });

//                 iziToast.error({
//                     title: 'Error',
//                     message: res.responseJSON.error,
//                     position: 'topCenter'
//                 });
//             }
//         });
//     });
// });