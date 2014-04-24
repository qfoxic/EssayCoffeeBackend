$( document ).ready( function( ) {
    $( "#eventsRight" ).buildMbExtruder( {
        positionFixed: true,
        width: 350,
        sensibility: 800,
        position: "right", // left, right, bottom
        extruderOpacity: 1,
        flapDim: 100,
        textOrientation: "bt", // or "tb" (top-bottom or bottom-top)
        onExtOpen: function( ) {
        },
        onExtContentLoad: function( ) {
        },
        onExtClose: function( ) {
        },
        hidePanelsOnClose: true,
        autoCloseTime: 0, // 0=never
        slideTimer: 300
    } );
    $( "#reportsRight" ).buildMbExtruder( {
        positionFixed: true,
        width: 350,
        sensibility: 800,
        position: "right", // left, right, bottom
        extruderOpacity: 1,
        flapDim: 100,
        textOrientation: "bt", // or "tb" (top-bottom or bottom-top)
        onExtOpen: function( ) {
        },
        onExtContentLoad: function( ) {
        },
        onExtClose: function( ) {
        },
        hidePanelsOnClose: true,
        autoCloseTime: 0, // 0=never
        slideTimer: 300
    } );

} );
