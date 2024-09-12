document.addEventListener('DOMContentLoaded', function() {
    var links = document.querySelectorAll('a');
    links.forEach(function(link) {
        var url = new URL(link.href);

        // Check if the link points to the same domain as your website or if it points to the resume
        if (url.hostname !== window.location.hostname || url.pathname === '/resume/') {
            link.setAttribute('target', '_blank');
            link.setAttribute('rel', 'noopener noreferrer'); // Security best practice
        } else {
            // Optional: You can remove the 'target' attribute in case you want to handle internal links differently
            link.removeAttribute('target');
        }
    });
});
