document.addEventListener('DOMContentLoaded', (event) => {
    window.setTimeout(function() {
        var notifications = document.querySelectorAll('.notification');
        notifications.forEach(function(notification) {
            notification.style.opacity = '0';
            setTimeout(function() {
                notification.style.display = 'none';
            }, 600);
        });
    }, 4000);
});