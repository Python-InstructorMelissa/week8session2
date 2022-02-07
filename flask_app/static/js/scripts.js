var tune = 'https://dojo.navyladyveteran.com/characters/'
var squish = 'https://dojo.navyladyveteran.com/squishies/'

async function getTune() {
    var response = await fetch(`${tune}`)
    var data = await response.json()
    console.log("full tune api data: ", data)
    // console.log("pull back just name: ", data[0].name)
    for (var i = 0; i < data.length; i++) {
        // console.log(data[i])
        var node = document.createElement('div')
        var h2 = document.createElement('h2')
        var h3 = document.createElement('h3')
        var a = document.createElement('a')
        var link = document.createTextNode('View Tune')
        a.appendChild(link)
        a.title = 'View Tune'
        a.href = `/api/looneytunes/${data[i].id}/view/`
        var img = new Image()
        img.src = `${data[i].img}`
        img.alt = `${data[i].name}`
        var name = document.createTextNode(data[i].name)
        h2.appendChild(name)
        var birth = document.createTextNode(data[i].birthDay)
        h3.appendChild(birth)
        node.appendChild(h2)
        node.appendChild(h3)
        node.appendChild(a)
        node.appendChild(img)
        document.getElementById('tune').appendChild(node)
    }
}

async function getSquishy() {
    var response = await fetch(`${squish}`)
    var data = await response.json()
    console.log("full squish api data: ", data)
    for (var i = 0; i < data.length; i++) {
        var node = document.createElement('div')
        var h2 = document.createElement('h2')
        var img = new Image()
        img.src = `${data[i].img}`
        img.alt = `${data[i].name}`
        img.alt = `${data[i].name}`
        var name = document.createTextNode(data[i].name)
        h2.appendChild(name)
        node.appendChild(h2)
        node.appendChild(img)
        document.getElementById('squishy').appendChild(node)
    }
}
async function getOneTune(i) {
    var response = await fetch(`${tune}`)
    var data = await response.json()
    console.log("full tune api data: ", data)
    i = i-1
    // console.log("pull back just name: ", data[i].name)
        // console.log(data[i])
        if (data[i].spouse){
            data[i].spouse
            console.log("if true", data[i].spouse)
        } else {
            data[i].spouse = "still a single pringle"
            console.log("if false", data[i].spouse)
        }
        var node = document.createElement('div')
        var h1 = document.createElement('h1')
        var h3 = document.createElement('h3')
        var p = document.createElement('p')
        var head = document.createTextNode(`You chose ${data[i].name}`)
        h1.appendChild(head)
        var img = new Image()
        img.src = `${data[i].img}`
        img.alt = `${data[i].name}`
        var birth = document.createTextNode(data[i].birthDay)
        var voiceSpouse = document.createTextNode(`${data[i].name} was voiced by ${data[i].voice} and if married the spouses name was ${data[i].spouse}`)
        p.appendChild(voiceSpouse)
        h3.appendChild(birth)
        node.appendChild(h1)
        node.appendChild(h3)
        node.appendChild(img)
        node.appendChild(p)
        document.getElementById('tune').appendChild(node)
}