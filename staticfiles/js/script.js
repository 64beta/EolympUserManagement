document.getElementById('linkCount').innerText = document.querySelectorAll('.link-list-item').length;

function copyLinks() {
    var linkList = document.querySelectorAll('.link-list-item a');
    var links = [];

    linkList.forEach(function (link) {
        links.push(link.href);
    });

    var textarea = document.createElement('textarea');
    textarea.value = links.join('\n');
    textarea.value = document.getElementById('linkCount').innerText + "\n" + textarea.value;
    document.body.appendChild(textarea);
    textarea.select();
    document.execCommand('copy');
    document.body.removeChild(textarea);

    alert('Links copied to clipboard!');
}
