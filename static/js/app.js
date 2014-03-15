$( document ).ready( function( ) {
    // $( '.datetimepicker' ).datetimepicker( {
    // language: 'ru',
    // format: 'YYYY-MM-DD HH:mm',
    // useSeconds: false,
    // icons: {
    // time: "fa fa-clock-o",
    // date: "fa fa-calendar",
    // up: "fa fa-arrow-up",
    // down: "fa fa-arrow-down"
    // }
    // } );
    $( '.btn-cancel' ).on( 'click', function( ) {
        var message = "Are you sure to leave this page? All unsaved data will be lost&hellip;";
        bootbox.confirm( message, function( result ) {
            if( result == true ) {
                window.location.replace( '/tasks/' );
            }
        } );
    } );
    $( '.upload-file' ).bootstrapFileInput( );
    $( '.has-error' ).tooltip( {
        container: 'body',
    } );
} );
