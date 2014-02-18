$( document ).ready( function( ) {
    $( '.datetimepicker' ).datetimepicker( {
        language: 'ru',
        format: 'DD-MM-YYYY',
        useSeconds: false,
        icons: {
            time: "fa fa-clock-o",
            date: "fa fa-calendar",
            up: "fa fa-arrow-up",
            down: "fa fa-arrow-down"
        }
    } );
} );
