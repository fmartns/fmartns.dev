var endDate = moment.tz("2024-07-08 00:00:00", "America/Sao_Paulo");

var countdown = setInterval(function() {
    var now = moment.tz("America/Sao_Paulo");

    var distance = moment.duration(endDate.diff(now));

    var days = Math.floor(distance.asDays());
    var hours = distance.hours();
    var minutes = distance.minutes();
    var seconds = distance.seconds();

    document.getElementById("countdown").innerHTML = days + "d " + hours + "h "
    + minutes + "m " + seconds + "s ";

    if (distance <= 0) {
        clearInterval(countdown);
        document.getElementById("countdown").innerHTML = "Férias!";
    }
}, 1000);