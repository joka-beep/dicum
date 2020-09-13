function updateTime(time, divName)
{
    var datetime = new Date(time + "Z").getTime();
    document.getElementById(divName).innerHTML = time + "<br/>" + new Date(datetime)

    update(datetime, divName)
    setInterval(function(){ update(datetime, divName) }, 1000);
}

function update(datetime, divName)
{
    var now = new Date().getTime();
    var millisec_diff = datetime - now;
    var days = Math.floor(millisec_diff / (1000 * 60 * 60 * 24));
    var date_diff = new Date( millisec_diff );

    document.getElementById(divName).innerHTML = ("Welcome to Dicum<br/>You are restricted for "
                + days + " days and "
                + date_diff.getHours() + ":" + date_diff.getMinutes() + ":" + date_diff.getSeconds());
}