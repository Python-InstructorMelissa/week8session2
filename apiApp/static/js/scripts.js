var nasa = keys.NASAKEY
var apiKey = keys.OPENWEATHER
var toons = 'https://dojo.navyladyveteran.com/characters/'
var squish = 'https://dojo.navyladyveteran.com/squishies/'


$(document).ready(function(){
    $('#image').click(function(){
        console.log('button clicked')
        $('#images').animate( {
            width: 'toggle'
        })
    })
    $('#forecast').click(function() {
        console.log('button clicked')
        $('#temps').animate( {
            width: 'toggle'
        })
    })
    nasaurl = `https://api.nasa.gov/planetary/apod?api_key=${nasa}`

    $.get(nasaurl, function(res) {
        console.log(res)
        var html_str ="<img id='img' src='" + res.url + "' alt='Nasa Photo'>"
        $(".photo").html(html_str)
        var nasaImgTitle = `<input type='hidden' name='name' value='" + res.title +"'>`
        var nasaImg = `<input type='hidden' name='img' value='" + res.url +"'>`
        $("#nasaImgTitle").html(nasaImgTitle)
        $('#nasaImg').html(nasaImg)
    }, 'json')
    $('#button').click(function(){
        console.log('button clicked')
        $('#img').animate( {
            width: 'toggle'
        })
    })
    $.get(toons, function(res) {
        console.log(res)
    })
    $('.form').submit(function () {
        var city = $('#city').val();
        var cityString = `${city}`

        var url = `https://api.openweathermap.org/data/2.5/weather?q=${cityString}&appid=${apiKey}&units=imperial`

        $.get(url, function (res) {
            console.log(res)
            var htmlString = `<h1>${cityString}</h1><p>Temperature: ${res.main.temp}&#8457;</p>`
            htmlString+= `<p>Description: ${res.weather[0].description}</p><p>Wind Speed: ${res.wind.speed} mph</p>`
            $('#forecast').html(htmlString);
            var conditions = `<input type='hidden' name='conditions' value=${res.weather[0].description}>`
            var temp = `<input type='hidden' name='temp' value='${res.main.temp}'> `
            var theCity = `<input type='hidden' name='city' value=${cityString}>`
            $('#city2').html(theCity)
            $('#conditions').html(conditions)
            $('#temp').html(temp)
        }, 'json');
        return false;
    });
})
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');
console.log(csrftoken)

async function getToons() {
    var response = await fetch(`${toons}`)
    var data = await response.json()
    console.log("full toon api data:", data)
    for (var i = 0; i < data.length; i++) {
        // console.log(data[i])
        var node = document.createElement('div')
        var h2 = document.createElement('h2')
        var h3 = document.createElement('h3')
        var form = document.createElement('form')
        var nameInput = document.createElement('input')
        var imgInput = document.createElement('input')
        var tokenInput = document.createElement('input')
        var button = document.createElement('button')
        var submit = document.createTextNode('Save Image to Database')
        button.appendChild(submit)
        var img = new Image()
        img.src = `${data[i].img}`
        img.alt = `${data[i].name}`
        var name = document.createTextNode(data[i].name)
        h2.appendChild(name)
        var birth = document.createTextNode(data[i].birthDay)
        form.setAttribute('method', 'post')
        form.setAttribute('action', '/images/create/')
        namesrc = `${data[i].name}`
        imgsrc = `${data[i].img}`
        nameInput.setAttribute('type', 'hidden')
        nameInput.setAttribute('name', 'name')
        nameInput.setAttribute('value', namesrc)
        imgInput.setAttribute('type', 'hidden')
        imgInput.setAttribute('name', 'img')
        imgInput.setAttribute('value', imgsrc)
        tokenInput.setAttribute('type', 'hidden')
        tokenInput.setAttribute('name', 'csrfmiddlewaretoken')
        tokenInput.setAttribute('value', csrftoken)
        form.appendChild(tokenInput)
        form.appendChild(nameInput)
        form.appendChild(imgInput)
        form.appendChild(button)
        // console.log("name and img only: ", namesrc, imgsrc)
        h3.appendChild(birth)
        node.appendChild(h2)
        node.appendChild(h3)
        node.appendChild(img)
        node.appendChild(form)
        document.getElementById('tune').appendChild(node)
    }
}