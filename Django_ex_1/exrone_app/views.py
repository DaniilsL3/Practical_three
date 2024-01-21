from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello_world_view(request):
    html_content = """
 <!DOCTYPE html>
<html>
<head>
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js" type="text/javascript"></script>
<script>
	document.addEventListener('DOMContentLoaded', function() {
    var previewWindow = document.getElementById('previewWindow');
    var wikiLink = document.querySelector('a'); // Adjust the selector if needed

    document.addEventListener('mousemove', function(e) {
        // Position the previewWindow 10px below and to the right of the cursor
        var x = e.clientX + 10;
        var y = e.clientY + 10;

        previewWindow.style.left = x + 'px';
        previewWindow.style.top = y + 'px';
    });

    wikiLink.addEventListener('mouseover', function() {
        console.log('Mouse over link'); // Debugging
        let color = '#'+Math.floor(Math.random()*16777215).toString(16);
        previewWindow.style.display = 'block';
        console.log(color);
        $("#previewWindow").css("background-color", color);
    });

    wikiLink.addEventListener('mouseout', function() {
        console.log('Mouse out of link'); // Debugging
        previewWindow.style.display = 'none';
    });
});

	function loadWikiContent(title) {
    var url = 'https://en.wikipedia.org/w/api.php?' +
              new URLSearchParams({
                  origin: '*',
                  action: 'query',
                  format: 'json',
                  prop: 'extracts',
                  titles: title,
                  exintro: true,
                  explaintext: true,
              });

    fetch(url)
        .then(response => response.json())
        .then(data => {
            var page = data.query.pages;
            var pageId = Object.keys(page)[0];
            document.getElementById('previewWindow').innerHTML = page[pageId].extract;
        })
        .catch(error => console.error(error));
}

// Call this function with the title of the Wikipedia page when you want to load the content
loadWikiContent('Beautiful');

</script>
</head>
<body>

<h1 style="background-color: red; text-align: center;">Hello World!</h1>
<p>Too lazy to make it <a href="https://en.wikipedia.org/wiki/Beautiful" style="color: yellow; font-weight: bold; font-style: italic;"><i>beautiful</i></a>.</p>


<div id="previewWindow" style="display: none; position: absolute; min-height: 100px; min-width: 100px; background-color: red;"></div>

</body>
</html>

    """

    return HttpResponse(html_content)