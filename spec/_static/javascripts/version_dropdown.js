function assign_href( a, url, path ) {
    const r = fetch( url + "/" + path );
    r.then( response => {
        console.log('...', response);
        if( response.ok ){
            a.href = url + "/" + path;
        }
    }).catch( error => {
        a.href = url;
    });
}

function add_version_dropdown(json_loc, target_loc, text) {
    var dropdown = document.createElement("div");
    dropdown.className = "md-flex__cell md-flex__cell--shrink dropdown";
    var button = document.createElement("button");
    button.className = "dropdownbutton";
    var content = document.createElement("div");
    content.className = "dropdown-content md-hero";
    dropdown.appendChild(button);
    dropdown.appendChild(content);
    console.log('*********');
    $.getJSON(json_loc, function(versions) {
        var currentURL = window.location.href;
        var path = currentURL.split( "_site" )[ 1 ];
        path = path.split('/');
        path = path.slice(2, path.length);
        path = path.join('/');
        for (var key in versions) {
            if (versions.hasOwnProperty(key)) {
                console.log(key, versions[key]);
                var a = document.createElement("a");
                a.innerHTML = key;
                a.title = key;
                assign_href( a, target_loc + versions[key], path );
                content.appendChild(a);
            }
        }
    }).done(function() {
        button.innerHTML = text;
    }).fail(function() {
        button.innerHTML = "Other Versions Not Found";
    }).always(function() {
        $(".navheader").append(dropdown);
    });
};
