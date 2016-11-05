/*
*   Credit to http://blog.saynotolinux.com/blog/2016/08/15/jetbrains-ide-remote-code-execution-and-local-file-disclosure-vulnerability-analysis/
*   There is a known problem with PhpStorm listening for
*   any request, from any origin. Although it would take
*   some work to exploit this in a meaningful way, it's
*   still theoretically possible. So I made this quick
*   js file to check for the problem, and alert users
*/

var exploitable = false;
(function(){
    var checker = new XMLHttpRequest();
    // The built-in web server listens to
    // localhost on 63342, an accepts CORS from all origins
    checker.open('GET', 'http://localhost:63342', true);
    checker.send();
    checker.onload = function(){
        // All I'm doing is checking to see if
        // we get a response, and if it has
        // the PhpStorm string inside it
        if(checker.status === 404){
            var exploitable = checker.responseText.lastIndexOf('PhpStorm') > - 1
        }
        // This technically shouldn't work
        // but if it does...well something
        // is very wonky, requiring a look
        if(checker.status === 200){
            var exploitable = true;
        }
        if(exploitable){
            // This only means that the IDE is exposing a connection
            // if you have the latest version of your IDE, jetbrains
            // says everything is safe. That being said, they were
            // not aware of the exploitability of openly accepting
            // all cross-origin requests to begin with. You can
            // they aren't thrilled with CORS by view comments: https://github.com/JetBrains/intellij-community/commit/11f333f60cd2fc5b14f8535a2f1d156e90bb372e
            console.log("WARNING: you're IDE is exposing your computer on localhost:63342. \n There's a 404 error above that shows how I determined this. \n\n")
            var el = document.getElementById('footer-message').innerHTML = '<code>Hey there! Pop open the console for an important message.</code>'
        }
    }
})()

