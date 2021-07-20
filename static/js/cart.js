var update = document.getElementsByClassName('update-cart')
for (var i = 0; i < update.length; i++) {
    update[i].addEventListener('click', function () {
        var produactId = this.dataset.product
        var action = this.dataset.action
        console.log(produactId, action, user)
        if (user === 'AnonymousUser') {
            console.log('user is not authenticated')
        } else {
            updateCart(produactId, action)
        }
    })
}

function updateCart(produactId, action){
    var url = '/updateCart/'
    fetch(url,{
            method: 'POST',
            headers: {
                'content-type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({
                'produactId': produactId,
                'action': action
            }),
        })
        .then((response) => {
            return response.json()
        })
        .then((data) => {
            console.log('data',data)
            location.reload()
        })
}