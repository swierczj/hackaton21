const errorData = JSON.data;

const stackIconUrl = "https://img.icons8.com/color/96/000000/stackoverflow.png"

const createErrorPanel = (postAuthor, content, votes, url, i) => {  
  // creating elements
  let errorContainer = document.createElement("div")
  errorContainer.setAttribute('class', 'errorContainer')

  let errorHeader = document.createElement('div')
  errorHeader.setAttribute('class', 'errorContainer__errorHeader')
  
  let headerImg = document.createElement('img')
  headerImg.setAttribute('src', stackIconUrl)
  headerImg.setAttribute('width', '50px')
  headerImg.setAttribute('height', '50px')

  let headerParagraphsContainer = document.createElement('div')
  headerParagraphsContainer.setAttribute('class', 'flxbox flxbox--column flxbox--alignStart')

  let errorDetails = document.createElement('div')
  errorDetails.setAttribute('class', 'errorContainer__errorDetails')
  
  let paragraphBestAnswear = document.createElement('p')
  paragraphBestAnswear.setAttribute('class', 'fontLarge primaryText bold')
  
  let paragraphAuthor = document.createElement('p')
  paragraphAuthor.setAttribute('class', 'fontLarge')
  
  let answearContent = document.createElement('div')
  answearContent.setAttribute('class', 'answear pad')
  
  let paragraphVotes = document.createElement('p')
  paragraphVotes.setAttribute('class', 'primaryText bold')

  let buttonContainer = document.createElement('div')
  buttonContainer.setAttribute('class', 'flxbox')

  let anchorButton = document.createElement('a')
  anchorButton.setAttribute('class', 'button debug')
  anchorButton.setAttribute('href', url)

  // setting inner html
  
  paragraphBestAnswear.innerHTML = "Best Answer"
  paragraphAuthor.innerHTML = `User: ${postAuthor}`
  answearContent.innerHTML = content
  paragraphVotes.innerHTML = `${votes} votes`
  
  anchorButton.innerHTML = "check thread"
  
  headerParagraphsContainer.appendChild(paragraphBestAnswear)
  headerParagraphsContainer.appendChild(paragraphAuthor)

  errorHeader.appendChild(headerImg)
  errorHeader.appendChild(headerParagraphsContainer)

  errorDetails.appendChild(answearContent)
  errorDetails.appendChild(paragraphVotes)
  buttonContainer.appendChild(anchorButton)
  errorDetails.appendChild(buttonContainer)

  errorContainer.appendChild(errorHeader)
  errorContainer.appendChild(errorDetails)

  document.getElementById(`errorContainer${i}`).appendChild(errorContainer)
}

errorData.forEach((value, i) => {
  console.log(value, i)
  let errorContainer = document.createElement('div')
  errorContainer.setAttribute('class', 'flxbox flxbox--wrap')
  errorContainer.setAttribute('id', `errorContainer${i}`)
  let errorName = document.createElement('h3')
  errorName.innerHTML = value.errorName
  errorContainer.appendChild(errorName)
  document.getElementById("errorsContainer").appendChild(errorContainer)
  value.answers.forEach(answer => createErrorPanel(answer.author, answer.answerContent, answer.votes, answer.url, i))
})
