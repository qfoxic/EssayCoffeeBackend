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

    $( '.momdl' ).each( function( ) {
        var ts = $( this ).html( );
        $( this ).html( moment( ts, 'X' ).fromNow( ) );
    } );

    $( '.uploads-add' ).on( 'click', function( ) {
        var rbd = $( '#uploads-form' );
        if( rbd.is( ':visible' ) ) {
            $( this ).find( 'i' ).removeClass( 'fa-times-circle' ).addClass( 'fa-plus-circle' );
        } else {
            $( this ).find( 'i' ).removeClass( 'fa-plus-circle' ).addClass( 'fa-times-circle' );
        }
        rbd.toggle( 450 );
    } );
    
    $( '.uploads-ctrl' ).on( 'click', function( ) {
        var bid = $( this ).data( 'body-id' );
        var rbd = $( '#upload-id-' + bid );
        if( rbd.is( ':visible' ) ) {
            // rbd.hide( 'slow' );
            $( this ).find( 'i' ).removeClass( 'fa-rotate-180' );
            $( '#upload-del-' + bid ).fadeOut( 'slow' );
        } else {
            // rbd.show( 'slow' );
            $( this ).find( 'i' ).addClass( 'fa-rotate-180' );
            $( '#upload-del-' + bid ).fadeIn( 'slow' );
        }
        rbd.toggle( 300 );
    } );

    // attr view
    $( '.attr-ctrl' ).on( 'click', function( ) {
        var bid = $( '.attr-body' );
        if( bid.is( ':visible' ) ) {
            $( this ).find( 'i' ).addClass( 'fa-rotate-180' );
        } else {
            $( this ).find( 'i' ).removeClass( 'fa-rotate-180' );
        }
        bid.toggle( 300 );
    } );
    // admin reports
    $( '.adm-report-ctrl' ).on( 'click', function( ) {
        var bid = $( this ).data( 'body-id' );
        var rbd = $( '#body-id-' + bid );
        if( rbd.is( ':visible' ) ) {
            // rbd.hide( 'slow' );
            $( this ).find( 'i' ).removeClass( 'fa-rotate-180' );
            $( '#rep-del-' + bid ).fadeOut( 'slow' );
        } else {
            // rbd.show( 'slow' );
            $( this ).find( 'i' ).addClass( 'fa-rotate-180' );
            $( '#rep-del-' + bid ).fadeIn( 'slow' );
        }
        rbd.toggle( 300 );
    } );

    $( '.adm-report-add' ).on( 'click', function( ) {
        var rbd = $( '#report-form' );
        if( rbd.is( ':visible' ) ) {
            // rbd.hide( 'slow' );
            $( this ).find( 'i' ).removeClass( 'fa-times-circle' ).addClass( 'fa-plus-circle' );
        } else {
            // rbd.show( 'slow' );
            $( this ).find( 'i' ).removeClass( 'fa-plus-circle' ).addClass( 'fa-times-circle' );
        }
        rbd.toggle( 400 );
    } );

    // admin actions
    if( $( '#admin_actions' ).length ) {
        $( '#admin_actions_list' ).find( 'a' ).on( 'click', function( ev ) {
            ev.preventDefault( );
            $( '#admin_actions_button' ).html( $( this ).html( ) ).data( "status", $( this ).data( 'status' ) );
        } );
        $( '#admin_actions_list' ).find( 'i' ).removeAttr( 'style' ).removeAttr( 'title' );
    }
    $( '#admin_actions_button' ).on( 'click', function( ev ) {
        ev.preventDefault( );
        if( $( this ).data( 'status' ) ) {
            $( '#admin_actions' ).append( '<input type="hidden" name="status" value="' + $( this ).data( 'status' ) + '">' ).submit( );
        }
    } );

    $( '#lock_buttons > button' ).on( 'click', function( ev ) {
        ev.preventDefault( );
        if( $( this ).data( 'url' ) ) {
            $( '#lock_form' ).attr( 'action', $( this ).data( 'url' ) ).submit( );
        }
    } );

    if( $( '#admin_flat_buttons' ).length ) {
        $( '#admin_flat_buttons > button' ).on( 'click', function( ev ) {
            ev.preventDefault( );
            if( $( this ).data( 'status' ) ) {
                $( '#admin_flat_form' ).append( '<input type="hidden" name="status" value="' + $( this ).data( 'status' ) + '">' ).attr( 'action', $( this ).data( 'url' ) ).submit( );
            }
        } );

        $( '#admin_flat_buttons > a.send' ).on( 'click', function( ev ) {
            ev.preventDefault( );
            if( $( this ).data( 'status' ) ) {
                //     $( '#admin_flat_form' ).append( '<input type="hidden" name="status" value="' + $( this ).data( 'status' ) + '">' ).attr('action', $( this ).data( 'url' )).submit( );
                // console.log( 'dialog show' );
                $( '#writer-send' ).modal( 'show' );
            }
        } );
    }

    // $( '#writer-send' ).modal( );

    $( '.has-error, .has_tooltip' ).tooltip( {
        container: 'body',
    } );

    // tablesorter section
    $.tablesorter.addParser( {
        id: 'status',
        is: function( s ) {
            // return false so this parser is not auto detected
            return false;
        },
        format: function( s, table, cell, cellIndex ) {
            return $( cell ).data( 'status' );
        },
        // flag for filter widget (true = ALWAYS search parsed values; false = search cell text)
        parsed: false,
        // set type, either numeric or text
        type: 'numeric'
    } );
    $( '.tablesorter' ).tablesorter( {
        theme: 'default',
        dateFormat: "MMDDYYYY"/*March 27, 2014, 5:37 p.m.*/,
    } );

    $( '.tablesorter0-' ).tablesorter( {
        // *** APPEARANCE ***
        // Add a theme - try 'blackice', 'blue', 'dark', 'default'
        //  'dropbox', 'green', 'grey' or 'ice'
        // to use 'bootstrap' or 'jui', you'll need to add the "uitheme"
        // widget and also set it to the same name
        // this option only adds a table class name "tablesorter-{theme}"
        theme: 'dropbox',

        // fix the column widths
        widthFixed: false,

        // Show an indeterminate timer icon in the header when the table
        // is sorted or filtered
        showProcessing: false,

        // header layout template (HTML ok); {content} = innerHTML,
        // {icon} = <i/> (class from cssIcon)
        headerTemplate: '{content}',

        // return the modified template string
        onRenderTemplate: null, // function(index, template){ return template; },

        // called after each header cell is rendered, use index to target the column
        // customize header HTML
        onRenderHeader: function( index ) {
            // the span wrapper is added by default
            $( this ).find( 'div.tablesorter-header-inner' ).addClass( 'roundedCorners' );
        },

        // *** FUNCTIONALITY ***
        // prevent text selection in header
        cancelSelection: true,

        // other options: "ddmmyyyy" & "yyyymmdd"
        dateFormat: "mmddyyyy",

        // The key used to select more than one column for multi-column
        // sorting.
        sortMultiSortKey: "shiftKey",

        // key used to remove sorting on a column
        sortResetKey: 'ctrlKey',

        // false for German "1.234.567,89" or French "1 234 567,89"
        usNumberFormat: true,

        // If true, parsing of all table cell data will be delayed
        // until the user initializes a sort
        delayInit: false,

        // if true, server-side sorting should be performed because
        // client-side sorting will be disabled, but the ui and events
        // will still be used.
        serverSideSorting: false,

        // *** SORT OPTIONS ***
        // These are detected by default,
        // but you can change or disable them
        // these can also be set using data-attributes or class names
        /*
        headers: {
        // set "sorter : false" (no quotes) to disable the column
        0: {
        sorter: "text"
        },
        1: {
        sorter: "digit"
        },
        2: {
        sorter: "text"
        },
        3: {
        sorter: "url"
        }
        },
        */
        // ignore case while sorting
        ignoreCase: true,

        // forces the user to have this/these column(s) sorted first
        sortForce: null,
        // initial sort order of the columns, example sortList: [[0,0],[1,0]],
        // [[columnIndex, sortDirection], ... ]
        sortList: [ [ 0, 0 ], [ 1, 0 ], [ 2, 0 ] ],
        // default sort that is added to the end of the users sort
        // selection.
        sortAppend: null,

        // starting sort direction "asc" or "desc"
        sortInitialOrder: "asc",

        // Replace equivalent character (accented characters) to allow
        // for alphanumeric sorting
        sortLocaleCompare: false,

        // third click on the header will reset column to default - unsorted
        sortReset: false,

        // restart sort to "sortInitialOrder" when clicking on previously
        // unsorted columns
        sortRestart: false,

        // sort empty cell to bottom, top, none, zero
        emptyTo: "bottom",

        // sort strings in numerical column as max, min, top, bottom, zero
        stringTo: "max",

        // extract text from the table - this is how is
        // it done by default
        textExtraction: {
            0: function( node ) {
                return $( node ).text( );
            },
            1: function( node ) {
                return $( node ).text( );
            }
        },

        // use custom text sorter
        // function(a,b){ return a.sort(b); } // basic sort
        textSorter: null,

        // *** WIDGETS ***

        // apply widgets on tablesorter initialization
        initWidgets: true,

        // include zebra and any other widgets, options:
        // 'columns', 'filter', 'stickyHeaders' & 'resizable'
        // 'uitheme' is another widget, but requires loading
        // a different skin and a jQuery UI theme.
        widgets: [ 'zebra', 'columns' ],

        widgetOptions: {

            // zebra widget: adding zebra striping, using content and
            // default styles - the ui css removes the background
            // from default even and odd class names included for this
            // demo to allow switching themes
            // [ "even", "odd" ]
            zebra: [ "ui-widget-content even", "ui-state-default odd" ],

            // uitheme widget: * Updated! in tablesorter v2.4 **
            // Instead of the array of icon class names, this option now
            // contains the name of the theme. Currently jQuery UI ("jui")
            // and Bootstrap ("bootstrap") themes are supported. To modify
            // the class names used, extend from the themes variable
            // look for the "$.extend($.tablesorter.themes.jui" code below
            uitheme: 'jui',

            // columns widget: change the default column class names
            // primary is the 1st column sorted, secondary is the 2nd, etc
            columns: [ "primary", "secondary", "tertiary" ],

            // columns widget: If true, the class names from the columns
            // option will also be added to the table tfoot.
            columns_tfoot: true,

            // columns widget: If true, the class names from the columns
            // option will also be added to the table thead.
            columns_thead: true,

            // filter widget: If there are child rows in the table (rows with
            // class name from "cssChildRow" option) and this option is true
            // and a match is found anywhere in the child row, then it will make
            // that row visible; default is false
            filter_childRows: false,

            // filter widget: If true, a filter will be added to the top of
            // each table column.
            filter_columnFilters: true,

            // filter widget: css class applied to the table row containing the
            // filters & the inputs within that row
            filter_cssFilter: "tablesorter-filter",

            // filter widget: Customize the filter widget by adding a select
            // dropdown with content, custom options or custom filter functions
            // see http://goo.gl/HQQLW for more details
            filter_functions: null,

            // filter widget: Set this option to true to hide the filter row
            // initially. The rows is revealed by hovering over the filter
            // row or giving any filter input/select focus.
            filter_hideFilters: false,

            // filter widget: Set this option to false to keep the searches
            // case sensitive
            filter_ignoreCase: true,

            // filter widget: jQuery selector string of an element used to
            // reset the filters.
            filter_reset: null,

            // Delay in milliseconds before the filter widget starts searching;
            // This option prevents searching for every character while typing
            // and should make searching large tables faster.
            filter_searchDelay: 300,

            // Set this option to true if filtering is performed on the server-side.
            filter_serversideFiltering: false,

            // filter widget: Set this option to true to use the filter to find
            // text from the start of the column. So typing in "a" will find
            // "albert" but not "frank", both have a's; default is false
            filter_startsWith: false,

            // filter widget: If true, ALL filter searches will only use parsed
            // data. To only use parsed data in specific columns, set this option
            // to false and add class name "filter-parsed" to the header
            filter_useParsedData: false,

            // Resizable widget: If this option is set to false, resized column
            // widths will not be saved. Previous saved values will be restored
            // on page reload
            resizable: true,

            // saveSort widget: If this option is set to false, new sorts will
            // not be saved. Any previous saved sort will be restored on page
            // reload.
            saveSort: true,

            // stickyHeaders widget: css class name applied to the sticky header
            stickyHeaders: "tablesorter-stickyHeader"

        },

        // *** CALLBACKS ***
        // function called after tablesorter has completed initialization
        initialized: function( table ) {
        },

        // *** CSS CLASS NAMES ***
        /*
        tableClass: 'tablesorter',
        cssAsc: "tablesorter-headerSortUp",
        cssDesc: "tablesorter-headerSortDown",
        cssHeader: "tablesorter-header",
        cssHeaderRow: "tablesorter-headerRow",
        cssIcon: "tablesorter-icon",
        cssChildRow: "tablesorter-childRow",
        cssInfoBlock: "tablesorter-infoOnly",
        cssProcessing: "tablesorter-processing",
        */
        // *** SELECTORS ***
        // jQuery selectors used to find the header cells.
        selectorHeaders: '> thead th, > thead td',

        // jQuery selector of content within selectorHeaders
        // that is clickable to trigger a sort.
        selectorSort: "th, td",

        // rows with this class name will be removed automatically
        // before updating the table cache - used by "update",
        // "addRows" and "appendCache"
        selectorRemove: "tr.remove-me",

        // *** DEBUGING ***
        // send messages to console
        debug: false

    } );
} );
