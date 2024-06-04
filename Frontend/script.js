const scrapeButton = document.querySelector('.scrape-button');
const newDivsContainer = document.getElementById('other-divs');
// const scrapedDiv = document.getElementById('scraped-data')
// const tendingList = document.getElementById('trending-titles')
var loading = false;

scrapeButton.addEventListener('click', handleScrapeClick);

function handleScrapeClick() {
    const startTime = 
    loading = true;
    scrapeButton.disabled = true;
    fetch('http://127.0.0.1:5000/scrape_data')
    .then(res => res.json())
    .then(data => {
        const dataObject = data

        //Dynamic
        const newDiv = document.createElement('div');
        newDiv.classList.add('recieved-data')

        const heading = document.createElement('h3')
        heading.textContent = "These are the most happening topics as on " + dataObject['scrape_end_time']

        const newList = document.createElement('ol');

        const ipAdrress = document.createElement("h3")
        ipAdrress.textContent = "The IP address used for this query was " + dataObject['ip']

        const jsonHeading = document.createElement("h3")
        jsonHeading.textContent = "JSON Extract from MongoDB !"

        const objectDiv = document.createElement('div');
        objectDiv.innerHTML = JSON.stringify(data)

        const runAgain = document.createElement('button');
        runAgain.classList.add('scrape-button');
        runAgain.textContent = 'Run query again'
        runAgain.addEventListener('click', handleScrapeClick);
        // Rigth Now
        // scrapedDiv.textContent = JSON.stringify(data)
        // scrapeButton.disabled = false;
        console.log(dataObject)
        console.log(typeof(dataObject))
        for (const key in dataObject) {
            if (key.startsWith('trend')) {
              const trendItem = dataObject[key];
              console.log(trendItem)  
              // Create a new list item element
              const listItem = document.createElement('li');
              listItem.textContent = trendItem;
          
              // Add the list item to the trend list
              newList.appendChild(listItem);
            }
          }

          newDiv.appendChild(heading);
          console.log("heading");
          newDiv.appendChild(newList);
          console.log("newList");
          newDiv.appendChild(ipAdrress);
          console.log("ip");
          newDiv.appendChild(jsonHeading);
          console.log("json");
          newDiv.appendChild(objectDiv);
          console.log("object div");
          newDiv.appendChild(runAgain);
          console.log("run again");

          newDivsContainer.appendChild(newDiv);
          console.log("final");
    })
    .catch(e => {
        console.error(error)
    })
}