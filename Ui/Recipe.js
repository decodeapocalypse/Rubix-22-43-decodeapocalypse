
let inputsearch = document.getElementById("inputsearch");

let button1 = document.getElementById("button1");

//add an event listener to the button that runs the function sendAPIRequest when its clicked
 button1.addEventListener("click", ()=> {
     console.log("button pressed")
     sendApiRequest(inputsearch.value)
 })


//an asynchronous function to fetch data from the api
async function sendApiRequest(inputsearch){
    let APP_ID = "4e9b58e6"
    let API_KEY = "ab5272b2beba38274cca9407b4647a4f"
    let response = await fetch(` https://api.edamam.com/search?app_id=${APP_ID}&app_key=${API_KEY}&q=${inputsearch}`);
    console.log(response)
    let data = await response.json()
    console.log(data)
    useApiData(data)
}


//function that does something with the data recieved from the api. the name of the function should be customised to whatever your doing with that api

function useApiData(data){
  let menuItem='';
  for (let i = 0;i < 10; i++) {
  menuItem=menuItem+`
      <div class="card" style="width: 18rem;">
      <img src="${data.hits[i].recipe.image}" class="card-img-top" alt="...">
      <div class="card-body">
          <h5 class="card-title">${data.hits[i].recipe.label}</h5>
          <p class="card-text">${data.hits[0].recipe.dishType}</p>
          <button class="btn1" style = "width: 30px height:20px ">
          <a href="${data.hits[i].recipe.source}" class="btn0">
          <div class="btn1text">
          Get recipe
          </div></a>
          </button>
      </div>
  </div>
  `
  }
  document.querySelector("#content").innerHTML=menuItem;
  
};

