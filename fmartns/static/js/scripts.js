var typed = new Typed(".auto-type", {
    strings: ["Filipe Martins", "Developer", "Student", "Filipe Martins"],
    typeSpeed: 150,
    backSpeed: 150,
    loop: false
})

function copiarTexto() {
    var link = document.getElementById("linkParaCopiar");
    var textarea = document.createElement("textarea");
    textarea.value = link.textContent;
    document.body.appendChild(textarea);
    textarea.select();
    textarea.setSelectionRange(0, 99999);
    document.execCommand("copy");
    document.body.removeChild(textarea);

    var notification = document.createElement("div");
    notification.className = "notification";
    notification.textContent = "Link copiado com sucesso!";

    var progressBar = document.createElement("div");
    progressBar.className = "progress-bar";
    notification.appendChild(progressBar);

    document.body.appendChild(notification);

    notification.style.display = "block";

    var progress = 0;
    var interval = setInterval(function() {
        progress += 1;
        progressBar.style.width = progress + "%";

        if (progress >= 100) {
            clearInterval(interval);
            setTimeout(function() {
                document.body.removeChild(notification);
            }, 500);
        }
    }, 10);
}

var botaoCopiar = document.getElementById("botaoCopiar");
botaoCopiar.addEventListener("click", copiarTexto);

function playCoinSound() {
    const audio = new Audio('static/audio/coin.mp3');
    audio.play();
}

document.addEventListener('keydown', function (event) {
    if (event.key === 'm' || event.key === 'M') {
        playCoinSound();
    }
});

document.addEventListener('keydown', function(event) {
    if (event.key === 's' || event.key === 'S') {
        var elementToShake = document.body;

        elementToShake.classList.add('tremor');

        setTimeout(function() {
            elementToShake.classList.remove('tremor');
        }, 2500);
    }
});