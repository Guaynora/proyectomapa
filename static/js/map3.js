let locationsInfo = []

const getLocations = ()=>{
    fetch('http://127.0.0.1:5000/iglesias')
    .then(response => response.json())
    .then(locations => {
        console.log(locations)

        locations.forEach(location => {
            let locationData = {
                position:{lat:location.punto.coordinates[0],lng:location.punto.coordinates[1]},
                name:location.nombre                
            }
            console.log(locationData)
            locationsInfo.push(locationData)
        })
        if(navigator.geolocation){
            navigator.geolocation.getCurrentPosition((data)=>{
                let ubicacion = {
                    lat: data.coords.latitude,
                    lng: data.coords.longitude
                }
                initMap(ubicacion)
            })
        }
    })
}

//let map
const initMap = (obj) =>{
    let map = new google.maps.Map(document.getElementById('map'),{
        zoom:13,
        center:obj
    })

    let marker = new google.maps.Marker({
        position:obj,
        title:'Tu ubicacion'
    })
    marker.setMap(map)

    let markers = locationsInfo.map( (location) =>{
        return new google.maps.Marker({
            position: location.position,
            map:map,
            title:location.name
        })
    })
}

getLocations()


