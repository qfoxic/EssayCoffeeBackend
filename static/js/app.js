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
        var r = confirm( "Are you sure to leave this page? All unsaved data will be lost." );
        if( r == true ) {
            window.location.replace('/tasks/');//history.back( );
            return false;
        } else {
            return false;
        }
    } );
    $( '.upload-file' ).bootstrapFileInput( );
    $( '.has-error' ).tooltip( {
        container: 'body',
    } );
} );
