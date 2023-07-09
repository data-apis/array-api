/**
* Returns a promise for resolving a URL corresponding to a versioned resource (if one exists).
*
* @private
* @param {string} url - base URL
* @param {string} path - resource path
* @returns {Promise} promise which resolves a resource URL
*/
function href(url, path) {
    const defaultURL = url + "/index.html";
    url += "/" + path;

    // If a versioned resource exists, return the resource's URL; otherwise, return a default URL:
    return fetch(url).then(onResponse).catch(onError);

    /**
    * Callback invoked upon successfully resolving a resource.
    *
    * @private
    * @param {Object} response - response object
    */
    function onResponse(response) {
        if (response.ok) {
            return url;
        }
        return defaultURL;
    }

    /**
    * Callback invoked upon failing to resolve a resource.
    *
    * @private
    * @param {Error} error - error object
    */
    function onError(error) {
        return defaultURL;
    }
}

/**
* Adds a version dropdown menu with custom URL paths depending on the current page.
*
* @param {string} json_loc - JSON URL
* @param {string} target_loc - target URL
* @param {string} text - text
* @returns {Promise} promise which resolves upon adding a version menu
*/
async function add_version_dropdown(json_loc, target_loc, text) {
    const dropdown = document.createElement("div");
    dropdown.className = "md-flex__cell md-flex__cell--shrink dropdown";

    const button = document.createElement("button");
    button.className = "dropdownbutton";

    const content = document.createElement("div");
    content.className = "dropdown-content md-hero";

    dropdown.appendChild(button);
    dropdown.appendChild(content);

    const opts = {
        'method': 'GET'
    };
    await fetch(json_loc, opts).then(onResponse).then(onVersions).catch(onError);

    /**
    * Callback invoked upon resolving a resource.
    *
    * @private
    * @param {Object} response - response object
    */
    function onResponse(response) {
        return response.json();
    }

    /**
    * Callback invoked upon resolving a JSON resource.
    *
    * @private
    * @param {Object} versions - versions object
    * @returns {Promise} promise which resolves upon processing version data
    */
    async function onVersions(versions) {
        console.log(versions);
        
        // Resolve the current browser URL:
        const currentURL = window.location.href;

        // Check whether the user is currently on a resource page (e.g., is viewing the specification for a particular function):
        let path = currentURL.split(/_site|array_api/)[1];

        // Extract the resource subpath:
        if (path) {
            path = path.split("/");
            path = path.slice(2, path.length);
            path = path.join("/");
        } else {
            path = "";
        }
        // For each version, create an anchor element and attempt to resolve a given resource for that version...
        const promises = [];
        const el = [];
        for (let key in versions) {
            if (versions.hasOwnProperty(key)) {
                let a = document.createElement("a");
                a.innerHTML = key;
                a.title = key;
                el.push(a);
                promises.push(href(target_loc + versions[key], path));
            }
        }
        // Resolve all resource URLs:
        const urls = await Promise.all(promises);

        // Append the version links to the dropdown menu:
        for (let i = 0; i < urls.length; i++) {
            let a = el[i];
            a.href = urls[i];
            content.appendChild(a);
        }
        // Set the button text:
        button.innerHTML = text;

        // Append dropdown:
        $(".navheader").append(dropdown);
    }

    /**
    * Callback invoked upon failing to resolve a resource.
    *
    * @private
    */
    function onError() {
        button.innerHTML = "Other Versions Not Found";

        // Append dropdown:
        $(".navheader").append(dropdown);
    }
};
