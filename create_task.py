//Inserting the columns from the Car Finder Data
var model = getColumn("Car Finder Data", "Model Name");
var price = getColumn("Car Finder Data", "Price");
var picture = getColumn("Car Finder Data", "Image");
var topSpeed = getColumn("Car Finder Data", "Top Speed (mph)");

//Creating the filter lists
var filterModel = [];
var filterPrice = [];
var filterPicture = [];
var filterTopSpeed = [];

var carType;
var minPrice;
var maxPrice;
var minTopSpeed;

//Code for the dropdown
onEvent("genreDropdown", "change", function( ) {
  carType = getProperty("genreDropdown", "text");
  if(carType == "Supercar" || carType == "Hypercar"){
    showElement("topSpeedInput");
  }
});
onEvent("genreDropdown", "change", function(carType) {
  carType = getProperty("genreDropdown", "text");
  if(carType == "Ultra-luxury"){
    hideElement("topSpeedInput");
  }
});

//Code for the price and top speed inputs
onEvent("minPriceInput", "change", function( ) {
  minPrice = getText("minPriceInput");
  console.log(minPrice);
  return minPrice;
});
onEvent("maxPriceInput", "change", function( ) {
  maxPrice = getText("maxPriceInput");
  console.log(maxPrice);
  return maxPrice;
});
onEvent("topSpeedInput", "change", function( ) {
  minTopSpeed = getText("topSpeedInput");
  console.log(minTopSpeed);
  return minTopSpeed;
});

onEvent("searchButton", "click", function( ) {
  if(minTopSpeed == undefined){
    minTopSpeed = 0;
  }
  search(minPrice,maxPrice,minTopSpeed);
});

onEvent("optionImage1", "click", function( ) {
  setScreen("finalScreen");
  setProperty("finalLabel","text",filterModel[0]);
  setProperty("finalImage","image",filterPicture[0]);
  setProperty("finalLabel2","text","Price:  $"+filterPrice[0]);
  if(carType != "Ultra-luxury"){
    setProperty("finalLabel3","text","Top Speed:  "+filterTopSpeed[0]+" MPH");
  } else{
    hideElement("finalLabel3");
  }
});
onEvent("optionImage2", "click", function( ) {
  setScreen("finalScreen");
  setProperty("finalLabel","text",filterModel[1]);
  setProperty("finalImage","image",filterPicture[1]);
  setProperty("finalLabel2","text","Price:  $"+filterPrice[1]);
  if(carType != "Ultra-luxury"){
    setProperty("finalLabel3","text","Top Speed:  "+filterTopSpeed[1]+" MPH");
  } else{
    hideElement("finalLabel3");
  }
});
onEvent("optionImage3", "click", function( ) {
  setScreen("finalScreen");
  setProperty("finalLabel","text",filterModel[2]);
  setProperty("finalImage","image",filterPicture[2]);
  setProperty("finalLabel2","text","Price:  $"+filterPrice[2]);
  if(carType != "Ultra-luxury"){
    setProperty("finalLabel3","text","Top Speed:  "+filterTopSpeed[2]+" MPH");
  } else{
    hideElement("finalLabel3");
  }
});
onEvent("optionImage4", "click", function( ) {
  setScreen("finalScreen");
  setProperty("finalLabel","text",filterModel[3]);
  setProperty("finalImage","image",filterPicture[3]);
  setProperty("finalLabel2","text","Price:  $"+filterPrice[3]);
  if(carType != "Ultra-luxury"){
    setProperty("finalLabel3","text","Top Speed:  "+filterTopSpeed[3]+" MPH");
  } else{
    hideElement("finalLabel3");
  }
});

function search(minPrice,maxPrice,minTopSpeed) {
  if(minPrice == undefined){
    minPrice = 0;}
  if(maxPrice == undefined){
    maxPrice = 100000000;}
  if(minTopSpeed == undefined){
    minTopSpeed = 0;}
  if(carType == "Supercar"){
    for (var i = 0; i < 5; i++) {
      if(price[i] >= minPrice){
        console.log("append");
        appendItem(filterModel,model[i]);
        appendItem(filterPrice,price[i]);
        appendItem(filterPicture,picture[i]);
        appendItem(filterTopSpeed,topSpeed[i]);
        if(i == 5 && filterModel.length == 0){
          noResults();
        }
    } }
    for (var o = 0; o < filterModel.length; o++) {
      console.log(filterPrice[o] +" less than "+ maxPrice +"?");
      if(filterPrice[o] >= maxPrice){
        console.log("remove");
        removeItem(filterModel,o);
        removeItem(filterPrice,o);
        removeItem(filterPicture,o);
        removeItem(filterTopSpeed,o);
        o--;
        if(filterModel.length == 0){
          noResults();
        }
    } }
    console.log(filterModel);
    for (var u = 0; u < filterModel.length; u++) {
      console.log(filterTopSpeed[u] + " is less than " + minTopSpeed[u]);
      if(filterTopSpeed[u] < minTopSpeed){
        removeItem(filterModel,u);
        removeItem(filterPrice,u);
        removeItem(filterPicture,u);
        removeItem(filterTopSpeed,u);
        u--;
        if(filterModel.length == 0){
          noResults();
        }
   } }
    updateScreen();
  }
  if(carType == "Hypercar"){
   for (var n = 11; n < 16; n++) {
      console.log(price[n] + " greater than " + minPrice);
      if(price[n] >= minPrice){
        console.log("append");
        appendItem(filterModel,model[n]);
        appendItem(filterPrice,price[n]);
        appendItem(filterPicture,picture[n]);
        appendItem(filterTopSpeed,topSpeed[n]);
        console.log(filterModel);
        if(n == 15 && filterModel.length == 0){
          noResults();
        }
    } }
    for (var m = 0; m < filterModel.length; m++) {
      console.log(filterPrice[m] +" less than "+ maxPrice +"?");
      if(filterPrice[m] >= maxPrice){
        console.log("remove");
        removeItem(filterModel,m);
        removeItem(filterPrice,m);
        removeItem(filterPicture,m);
        removeItem(filterTopSpeed,m);
        m--;
        if(filterModel.length == 0){
          noResults();
        }
    } }
    console.log(filterModel);
    for (var q = 0; q < filterModel.length; q++) {
      console.log(filterTopSpeed[q] + " is less than " + minTopSpeed[q]);
      if(filterTopSpeed[q] < minTopSpeed){
        removeItem(filterModel,q);
        removeItem(filterPrice,q);
        removeItem(filterPicture,q);
        removeItem(filterTopSpeed,q);
        q--;
        if(filterModel.length == 0){
          noResults();
        }
   } }
    updateScreen(); 
  }
  if(carType == "Ultra-luxury"){
     for (var y = 6; y < 11; y++) {
      console.log(price[y] + " greater than " + minPrice);
      if(price[y] >= minPrice){
        console.log("append");
        appendItem(filterModel,model[y]);
        appendItem(filterPrice,price[y]);
        appendItem(filterPicture,picture[y]);
        appendItem(filterTopSpeed,topSpeed[y]);
        console.log(filterModel);
        if(y == 10 && filterModel.length == 0){
          noResults();
        }
    } }
    for (var x = 0; x < filterModel.length; x++) {
      console.log(filterPrice[x] +" less than "+ maxPrice +"?");
      if(filterPrice[x] >= maxPrice){
        console.log("remove");
        removeItem(filterModel,x);
        removeItem(filterPrice,x);
        removeItem(filterPicture,x);
        removeItem(filterTopSpeed,x);
        x--;
        if(filterModel.length == 0){
          noResults();
        }
    } }
    console.log(filterModel);
    updateScreen();
} }

function updateScreen() {
  var three = false;
  var four = false;
  
  if(filterModel.length > 1){
    setScreen("optionScreen");
    setProperty("optionLabel1", "text",filterModel[0]);
    setProperty("optionImage1","image",filterPicture[0]);
    setProperty("optionLabel2","text",filterModel[1]);
    setProperty("optionImage2","image",filterPicture[1]);
    if(filterModel.length > 2){
      setProperty("optionLabel3","text",filterModel[2]);
      setProperty("optionImage3","image",filterPicture[2]);
      three = true;
    }
    if(filterModel.length > 3){
      setProperty("optionLabel4","text",filterModel[3]);
      setProperty("optionImage4","image",filterPicture[3]);
      four = true;
    }
    if(four == false){
      hideElement("optionLabel4");
    }
    if(three == false){
      hideElement("optionLabel3");
    }
  } else if(filterModel.length == 1){
    setScreen("finalScreen");
    setProperty("finalLabel", "text",filterModel[0]);
    setProperty("finalImage","image",filterPicture[0]);
    setProperty("finalLabel2","text","Price:  $"+filterPrice);
    if(carType == "Ultra-luxury"){
      hideElement("finalLabel3");
    } else{
      setProperty("finalLabel3","text","Top Speed:  "+filterTopSpeed+" MPH");
  } }
}

function noResults() {
  setScreen("finalScreen");
  hideElement("finalImage");
  hideElement("finalLabel2");
  hideElement("finalLabel3");
  setProperty("finalLabel","height",150);
  setProperty("finalLabel","text","There are no cars in the dataset that fit the user inputs.");
}
