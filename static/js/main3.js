const country=document.getElementById('country')
const countrySelect=document.getElementById('countrySelect')
const contrySelect=document.getElementById('contrySelect')
const state=document.getElementById('state')
const stateSelect=document.getElementById('stateSelect')
const countryChange=country.addEventListener('change',event=>{
    console.log(event.target.value)
    const selectedCountry = event.target.value
    state.innerHTML=""
    // state.textContent="-- State / Province / Region --"

    $.ajax({
        type:'GET',
        url:`/checkout/country/${selectedCountry}`,
        success:function(response){
            console.log(response.data)
            const countryState=response.data
            countryState.map(item =>{
                var option = document.createElement("option");
                option.value = item.state_name;
                option.text = item.state_name;
                state.appendChild(option);
            
            })
        },
        error:function(error){
            console.log(error)
        }
    })
})