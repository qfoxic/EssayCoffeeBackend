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
    $( '.adm-report-ctrl' ).on( 'click', function( ) {
        var bid = $( this ).data( 'body-id' );
        var rbd = $( '#body-id-' + bid );
        if( rbd.is( ':visible' ) ) {
            rbd.hide( 'slow' );
            $( this ).find( 'i' ).removeClass( 'fa-rotate-180' );
            $( '#rep-del-' + bid ).fadeOut( 'slow' );
        } else {
            rbd.show( 'slow' );
            $( this ).find( 'i' ).addClass( 'fa-rotate-180' );
            $( '#rep-del-' + bid ).fadeIn( 'slow' );
        }
    } );
    $( '.adm-report-add' ).on( 'click', function( ) {
        var rbd = $( '#report-form' );
        if( rbd.is( ':visible' ) ) {
            rbd.hide( 'slow' );
            $( this ).find( 'i' ).removeClass( 'fa-times-circle' ).addClass( 'fa-plus-circle' );
        } else {
            rbd.show( 'slow' );
            $( this ).find( 'i' ).removeClass( 'fa-plus-circle' ).addClass('fa-times-circle');
        }
    } );
} );
