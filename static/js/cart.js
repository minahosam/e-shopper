var update = document.getElementsByClassName('update-cart')
for (var i = 0; i < update.length; i++) {
    update[i].addEventListener('click', function () {
        var produactId = this.dataset.product
        var action = this.dataset.action
        console.log(produactId, action, user)
        if (user === 'AnonymousUser') {
            addcookie(produactId,action)
        } else {
            updateCart(produactId, action)
        }
    })
}

function addcookie(produactId,action){
    console.log('user is not authenticated')
    if(action == 'add'){
        console.log('add')
        if (CART[produactId]  == undefined) {
            CART[produactId]={'quantity':1}   
        }else{
            CART[produactId]['quantity'] += 1
        }
    }
    if (action == 'add2') {
        CART[produactId]['quantity'] += 1
    }
    if (action == 'remove') {
        CART[produactId]['quantity'] -= 1
        if (CART[produactId]['quantity'] <= 0) {
            delete CART[produactId]
        }
    }
    console.log(CART)
    document.cookie='cart='+JSON.stringify(CART)+';domain=;path=/'
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