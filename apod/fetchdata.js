function getData() {
  let birthday = document.getElementById("input-date").value;
  let test = document.forms.birthdayform.date.value;

  if (test == '')
    return false;
  else
    console.log(test);
    fetch('https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&date=' + birthday)

    .then(response => {
      return response.json()
    })
    .then(data => {
      console.log(data)
      document.getElementById("title").textContent = data.title;
      document.getElementById("photo-date").textContent = data.date;
      document.getElementById("pic").src = data.hdurl;
      document.getElementById("caption").textContent = data.explanation;
    })
    .catch(err => {
      console.log(err)
    })
    return true;;
  
}
